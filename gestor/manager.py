""" Administrador de clientes """
import helpers
import re

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'dni': '15J'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'dni': '48H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'dni': '28Z'})


def show(client):
    """ Muestra por pantalla un cliente de forma amigable """

    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")


def show_all():
    """ Recorre la lista de clientes y los muetra uno a uno """
    for client in clients:
        show(client)


def find():
    """ Busca un cliente y lo devuelve junto a su índice """

    dni = input("Introduce el DNI del cliente\n> ")

    for i, client in enumerate(clients):

        if client['dni'] == dni:
            show(client)
            return i, client

    print("No se ha encontrado ningún cliente con ese DNI")


def is_valid(dni):
    """
    Hace diferentes validaciones en el campo dni

    >>> is_valid('48H')  # No válido, en uso
    False
    >>> is_valid('X82')  # No válido, incorrecto
    False
    >>> is_valid('21A')  # Válido
    True
    """

    # Comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['dni'] == dni:
            return False

    return True


def add():
    """ Añade un cliente a la lista de clientes """

    client = dict()

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:

        print("Introduce DNI (2 números y 1 carácter en mayúscula)")
        dni = helpers.input_text(3, 3)

        if is_valid(dni):
            client['dni'] = dni
            break

        print("DNI incorrecto o en uso")

    clients.append(client)


def edit():
    """ Modifica el nombre y apellido de un cliente a partir del dni """

    i, client = find()

    if client:

        print(f"Introduce nuevo nombre ({client['nombre']})")
        clients[i]['nombre'] = helpers.input_text(2, 30)

        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2, 30)

        return True

    return False


def delete():
    """ Borra un cliente de la lista a partir del dni """

    i, client = find()

    if client:
        client = clients.pop(i)
        return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

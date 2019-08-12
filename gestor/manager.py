import re
import gestor.helpers as helpers


class Client:

    nombre: str
    apellido: str
    dni: str

    def __init__(self, nombre: str, apellido: str, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellido}"


class Manager:

    clients: list = []

    @staticmethod
    def show_client(client: Client):
        """ Muestra por pantalla un client de forma amigable """
        print(client)

    @staticmethod
    def show_clients():
        """ Recorre la lista de clients y los muetra uno a uno """
        if Manager.clients == []:
            print("No hay clients disponibles.")
        else:
            for client in Manager.clients:
                Manager.show_client(client)

    @staticmethod
    def add():
        """ Añade un client a la lista de clients """

        print('Introduce nombre (De 2 a 30 caracteres)')
        nombre = helpers.input_text(2, 30)
        print('Introduce apellido (De 2 a 30 caracteres)')
        apellido = helpers.input_text(2, 30)
        while True:
            print("Introduce DNI (2 números y 1 carácter en mayúscula)")
            dni = helpers.input_text(3, 3)
            if Manager.is_valid(dni):
                Manager.clients.append(Client(nombre, apellido, dni))
                break
            else:
                print("DNI incorrecto o en uso")
                dni = None

    @staticmethod
    def is_valid(dni: str):
        """
        Hace diferentes validaciones en el campo dni
        >>> Manager.is_valid('48H')  # No válido, en uso
        False
        >>> Manager.is_valid('X82')  # No válido, incorrecto
        False
        >>> Manager.is_valid('21A')  # Válido
        True
        """
        if not re.match('[0-9]{2}[A-Z]', dni):
            return False
        for client in Manager.clients:
            if client.dni == dni:
                return False
        return True

    @staticmethod
    def find():
        """ Busca un client y lo devuelve junto a su índice """
        dni = input("Introduce el dni del client\n> ")
        for i, client in enumerate(Manager.clients):
            if client.dni == dni:
                Manager.show_client(client)
                return i, client
        print("No se ha encontrado ningún client con ese DNI")
        return None, None

    @staticmethod
    def delete():
        """ Borra un client de la lista a partir del dni """
        i, client = Manager.find()
        if client:
            client = Manager.clients.pop(i)
            return True
        return False

    @staticmethod
    def edit():
        """ Modifica el nombre y apellido de un client a partir del dni """
        i, client = Manager.find()
        if client:
            print(f"Introduce nuevo nombre ({client.nombre})")
            Manager.clients[i].nombre = helpers.input_text(2, 30)
            print(f"Introduce nuevo apellido ({client.apellido})")
            Manager.clients[i].apellido = helpers.input_text(2, 30)
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'Manager': Manager})

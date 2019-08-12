""" Menú del programa """

from manager import Manager
import helpers


class Menu:

    @staticmethod
    def loop():
        while True:

            helpers.clear()

            print("========================")
            print("  BIENVENIDO AL GESTOR  ")
            print("========================")
            print("[1] Listar clientes     ")
            print("[2] Mostrar cliente     ")
            print("[3] Añadir cliente      ")
            print("[4] Modificar cliente   ")
            print("[5] Borrar cliente      ")
            print("[6] Salir               ")
            print("========================")

            option = input("> ")

            helpers.clear()

            if option == '1':
                print("Listando los clientes...\n")
                Manager.show_clients()
            if option == '2':
                print("Mostrando un cliente...\n")
                Manager.find()
            if option == '3':
                print("Añadiendo un cliente...\n")
                Manager.add()
                print("Cliente añadido correctamente\n")
            if option == '4':
                print("Modificando un cliente...\n")
                if Manager.edit():
                    print("Cliente modificado correctamente\n")
            if option == '5':
                print("Borrando un cliente...\n")
                if Manager.delete():
                    print("Cliente borrado correctamente\n")
            if option == '6':
                print("Saliendo...\n")
                break

            input("\nPresiona ENTER para continuar...")

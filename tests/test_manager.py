import unittest
from unittest.mock import patch

from gestor.manager import Client, Manager


class TestManager(unittest.TestCase):

    def setUp(self):
        Manager.clients = [
            Client('Marta', 'Pérez', '15J'),
            Client('Manolo', 'López', '48H'),
            Client('Ana', 'García', '28Z')
        ]

    def testAddClient(self):
        add_client_inputs = ['Héctor', 'Costa', '39J']
        with patch('builtins.input', side_effect=add_client_inputs):
            Manager.add()
        self.assertEqual(len(Manager.clients), 4)
        self.assertEqual(Manager.clients[-1].nombre, 'Héctor')

    def testDeleteClient(self):
        cliente_a_eliminar = Manager.clients[0]
        delete_client_inputs = [cliente_a_eliminar.dni]
        self.assertEqual(len(Manager.clients), 3)
        with patch('builtins.input', side_effect=delete_client_inputs):
            Manager.delete()
        self.assertEqual(len(Manager.clients), 2)
        self.assertTrue(Manager.clients[0] != cliente_a_eliminar)
        self.assertEqual(Manager.clients[0].nombre, 'Manolo')
        self.assertEqual(Manager.clients[-1].nombre, 'Ana')

    def testEditClient(self):
        edit_client_input = ['15J', 'Javier', 'Rosales']
        with patch('builtins.input', side_effect=edit_client_input):
            self.assertTrue(Manager.edit())
        self.assertEqual(Manager.clients[0].nombre, 'Javier')

    def testFindClient(self):
        find_client_edit = ['15J']
        with patch('builtins.input', side_effect=find_client_edit):
            self.assertEqual(Manager.find(), (0, Manager.clients[0]))

    def testDniIsValid(self):
        self.assertFalse(Manager.is_valid('48H'))
        self.assertFalse(Manager.is_valid('X82'))
        self.assertFalse(Manager.is_valid('23223S'))
        self.assertFalse(Manager.is_valid('13FF'))
        self.assertTrue(Manager.is_valid('21A'))


if __name__ == '__main__':
    unittest.main()

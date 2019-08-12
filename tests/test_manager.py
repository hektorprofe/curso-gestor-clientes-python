import unittest
from unittest.mock import patch

from gestor.manager import Manager, Client


class TestManager(unittest.TestCase):

    def setUp(self):
        Manager.clients = [
            Client('Marta', 'Pérez', '15J'),
            Client('Manolo', 'López', '48H'),
            Client('Ana', 'García', '28Z')
        ]

    def testAddClient(self):
        add_client_inputs = ['Héctor', 'Costa', '39J']
        with patch('builtins.input',  side_effect=add_client_inputs):
            Manager.add()
        self.assertEqual(len(Manager.clients), 4)
        self.assertEqual(Manager.clients[-1].nombre, 'Héctor')


if __name__ == '__main__':
    unittest.main()

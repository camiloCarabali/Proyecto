'''
Juan Camilo Carabali Caracas
Alejandro Rosas Cuesta
Creacion de pruebas unitarias a los modelos Rol y Login del proyecto.
'''

from django.test import TestCase
from .models import *
import unittest

class TestPrueba(unittest.TestCase):


    def test_uno(self):
        nombre = Rol.objects.create(nombre="prueba")
        self.assertEqual(str(nombre), "prueba")

    def test_dos(self):
        login1 = Login.objects.create(username = "prueba1", password = "12345")
        self.assertEqual(str(login1), "prueba1", "12345")

if __name__ == '__main__':
    unittest.main()

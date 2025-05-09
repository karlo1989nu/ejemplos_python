import unittest

# Funciones a probar
def suma(a, b):
    return a + b

def es_par(numero):
    return numero % 2 == 0

def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Clase de pruebas unitarias
class TestFunciones(unittest.TestCase):
    # Prueba para la función suma
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    # Prueba para la función es_par
    def test_es_par(self):
        self.assertTrue(es_par(4))
        self.assertFalse(es_par(5))
        self.assertTrue(es_par(0))

    # Prueba para la función encontrar_maximo
    def test_encontrar_maximo(self):
        self.assertEqual(encontrar_maximo(1, 2, 3), 3)
        self.assertEqual(encontrar_maximo(10, 5, 7), 10)
        self.assertEqual(encontrar_maximo(-1, -2, -3), -1)

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
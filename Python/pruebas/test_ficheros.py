import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from utilidades.ficheros import existe_ruta, es_fichero, es_directorio, obtener_extension


class TestFicheros(unittest.TestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.fichero = os.path.join(self.directorio.name, "nota.txt")
        with open(self.fichero, "w") as f:
            f.write("hola")

    def tearDown(self):
        self.directorio.cleanup()

    def test_existe_ruta(self):
        self.assertTrue(existe_ruta(self.fichero))
        self.assertFalse(existe_ruta(os.path.join(self.directorio.name, "no_existe")))

    def test_es_fichero_y_es_directorio(self):
        self.assertTrue(es_fichero(self.fichero))
        self.assertFalse(es_directorio(self.fichero))
        self.assertTrue(es_directorio(self.directorio.name))
        self.assertFalse(es_fichero(self.directorio.name))

    def test_obtener_extension(self):
        self.assertEqual(obtener_extension(self.fichero), "txt")

    def test_obtener_extension_de_ruta_inexistente(self):
        self.assertIsNone(obtener_extension(os.path.join(self.directorio.name, "no_existe.txt")))


if __name__ == "__main__":
    unittest.main()

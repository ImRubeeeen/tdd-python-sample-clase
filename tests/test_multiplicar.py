# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación resta
    def test_multiplicar(self):
        assert multiplicar(6,3) == 18
        assert multiplicar(8,3) == 24
        assert multiplicar(9,1) == 9
        assert multiplicar(10,9) == 90
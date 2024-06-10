# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación resta
    def test_multiplicar(self):
        assert multiplicacion(6,3) == 18
        assert multiplicacion(8,3) == 24
        assert multiplicacion(9,1) == 9
        assert multiplicacion(10,9) == 90
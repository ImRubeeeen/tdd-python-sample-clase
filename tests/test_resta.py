# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación resta
    def test_resta(self):
        assert resta(6,3) == 3
        assert resta(8,3) == 5
        assert resta(9,1) == 8
        assert resta(10,9) == 1
from calculadora import sumar, resta, division, multi
import pytest

def test_suma ():
    assert sumar(3,2) == 5

def test_resta ():
    assert resta (10,5) == 5

def test_division ():
    assert division (10,5) == 2

def test_multiplic ():
    assert multi (2,5) == 10

#Con esta función pruebo el value error que declaré en la división.

def test_divisionCero ():
    with pytest.raises(ValueError):
        division(2,0)

# Decoradores

# a) Fixture: Prepara datos reutilizables
''' Se ejecuta antes de tu prueba para preparar datos, objetos o estado, y, opcionalmente, después para
limpiarlos. Reduce repetición y centraliza la configuración.'''

# El fixture me devuelve num enteros
@pytest.fixture
def numeros_enteros():
    return 10,20

# Implementación de una funcion test usando el fixture
def test_sumarEnteros(numeros_enteros):
    a,b = numeros_enteros
    assert sumar(a,b)== 30

# b) Parametrize: Permite probar múltiples combinaciones sin duplicar funciones

@pytest.mark.parametrize("a,b,resultado",
                         [
                             (2,3,5),
                             (5,5,10),
                             (3,3,6)
                         ]
)

def test_conParametrize(a,b,resultado):
    assert sumar(a,b) == resultado

# c) markers <etiqueta>

@pytest.mark.smoke
def test_sumar_smoke():
    assert sumar (1,2) == 3


from calculator import sumar, restar, multiplicar, dividir
import pytest


def test_sumar():
    assert sumar(2,3) == 5   # ✅ correcto

def test_multiplicar():
    assert multiplicar(2,3) == 6


def test_dividir_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10,0)
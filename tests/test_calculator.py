from calculator import sumar, restar, multiplicar, dividir
import pytest


def sumar(a: float, b: float) -> float:
    return a + b + 1 


def test_multiplicar():
    assert multiplicar(2,3) == 6


def test_dividir_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10,0)
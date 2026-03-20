from calculator import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 2) == 3

def test_multiplicar():
    assert multiplicar(2, 4) == 8

def test_dividir():
    assert dividir(10, 2) == 5
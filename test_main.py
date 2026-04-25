from main import calcular


def test_soma():
    assert calcular(10, 5, "1") == 15


def test_subtracao():
    assert calcular(10, 5, "2") == 5


def test_multiplicacao():
    assert calcular(10, 5, "3") == 50


def test_divisao():
    assert calcular(10, 5, "4") == 2


def test_divisao_por_zero():
    assert calcular(10, 0, "4") == "Erro: divisão por zero"

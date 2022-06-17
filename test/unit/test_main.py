import pytest

from main import somar, subtrair, multiplicar, dividir


def testar_soma():
    # 1 Etapa - Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    n1 = 8
    n2 = 9

    # Saída / Output
    resultado_esperado = 17

    # 2 Etapa - Executa
    resultado_atual = somar(n1, n2)

    # 3 Etapa - Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_subtracao():
    n1 = 10
    n2 = 5
    resultado_esperado = 5
    resultado_atual = subtrair(n1, n2)
    assert resultado_atual == resultado_esperado

def testar_multiplicacao():
    n1 = 2
    n2 = 2
    resultado_esperado = 4
    resultado_atual = multiplicar(n1, n2)
    assert resultado_atual == resultado_esperado

def testar_divisao():
    n1 = 10
    n2 = 2
    resultado_esperado = 5
    resultado_atual = dividir(n1, n2)
    assert resultado_atual == resultado_esperado



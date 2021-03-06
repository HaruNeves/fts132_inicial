import csv

import pytest

from main import somar, subtrair, multiplicar, dividir, calcular_area_do_circulo, calcular_volume_do_paralelograma


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


# anotação par utilizar como massa de teste
@pytest.mark.parametrize('raio, resultado_esperado', [
    # valores
    (1, 3.14),  # teste número 1
    (2, 12.56),  # teste número 2
    (3, 28.26), # teste número 3
    (4, 50.24),  #teste número 4
    ('a', 'Falha no calculo - Raio não é um número'), #teste número 5, teste negativo
    (' ', 'Falha no calculo - Raio não é um número'),  # teste número 6, teste negativo
])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentamos para que os parametros sejam lidos
    # raio = 2
    # resultado_esperado = 12.56

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado


#Ler dados ded um csv para usar no teste seguinte
def ler_dados_csv():
    dados_csv = [] #criação de uma lista vazia
    nome_arquivo = 'C:/Users/Jaque/PycharmProjects/fts132_inicial/test/database/massa_caixa.csv' # local e nome do arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  #repetir a leitura até o fim do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id, largura, comprimento, altura, resultado_esperado', ler_dados_csv())
def testar_calcular_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):
    '''
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    '''
    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))
    assert resultado_atual == int(resultado_esperado)
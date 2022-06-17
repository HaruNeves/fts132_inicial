import pytest

#Definições
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


#Requisições
if __name__ == '__main__':
    resultado = somar(5, 7)
    print(f'A soma é {resultado}')

    resultado = subtrair(7, 5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar(5, 7)
    print(f'A multiplicação é {resultado}')

    resultado = dividir(7, 2)
    print(f'A divisão é {resultado}')


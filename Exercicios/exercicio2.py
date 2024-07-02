"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    numero = input('digite um número para verificarmos se é par ou ímpar:')
    numero = int(numero)

    if numero % 2 == 0:
        print('esse número é par')
    elif numero % 2 != 0:
        print('esse número é ímpar')
except:
    print('esse não é um número inteiro')


"""
Faça uma calculadora com 4 operações: soma, subtração, divisão e multiplicação.
"""

while True:
    print('Você deseja fazer: SOMA')
    print('Você deseja fazer: SUBTRAÇÃO')
    print('Você deseja fazer: MULTIPLICAÇÃO')
    print('Você deseja fazer: DIVISÃO')
    print('Você deseja: SAIR')
    opção = input('digite a opção:')
    if opção == 'SOMA' or opção == 'soma':
        print('Digite o primeiro valor:')
        valor_1 = input()
        print('Digite o segundo valor:')
        valor_2 = input()
        if valor_1.isnumeric() and valor_2.isnumeric():
            print(f'{valor_1} + {valor_2} = {int(valor_1) + int(valor_2)}\n')
        else:
            print('valor inserido não é um número\n')
        break
    elif opção == 'SUBTRAÇÃO' or opção == 'SUBTRACAO' or opção == 'subtração' or opção == 'subtracao':
        print('Digite o primeiro valor:')
        valor_1 = input()
        print('Digite o segundo valor:')
        valor_2 = input()
        if valor_1.isnumeric() and valor_2.isnumeric():
            print(f'{valor_1} - {valor_2} = {int(valor_1) - int(valor_2)}\n')
        else:
            print('valor inserido não é um número\n')
        break
    elif opção == 'MULTIPLIAÇÃO' or opção == 'MULTIPLICACAO' or opção == 'multiplicação' or opção == 'multiplicação':
        print('Digite o primeiro valor:')
        valor_1 = input()
        print('Digite o segundo valor:')
        valor_2 = input()
        if valor_1.isnumeric() and valor_2.isnumeric():
            print(f'{valor_1} * {valor_2} = {int(valor_1) * int(valor_2)}\n')
        else:
            print('valor inserido não é um número\n')
        break
    elif opção == 'DIVISÃO' or opção == 'DIVISAO' or opção == 'divisão' or opção == 'divisao': 
        print('Digite o primeiro valor:')
        valor_1 = input()
        print('Digite o segundo valor:')
        valor_2 = input()
        if valor_1.isnumeric() and valor_2.isnumeric():
            print(f'{valor_1} / {valor_2} = {int(valor_1) / int(valor_2)}\n')
        else:
            print('valor inserido não é um número\n')
        break
    elif opção == 'SAIR' or opção == 'sair':
        print('saindo...')
        break
    else:
        print('opção invalida')
        break

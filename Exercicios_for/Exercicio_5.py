# ""
# Escreva um programa que calcula o fatorial de um número fornecido pelo usuário.
# ""

numero_fornecido = input('Digite um numero para descobrir o fatorial:')
fatorial = 0
for numero_fornecido in range (int(numero_fornecido),1,-1):
    if numero_fornecido >= 2:
        fatorial += numero_fornecido * (numero_fornecido - 1)
    elif numero_fornecido >= 1:
        fatorial = fatorial 
    else:
        break
print(f'{fatorial}')
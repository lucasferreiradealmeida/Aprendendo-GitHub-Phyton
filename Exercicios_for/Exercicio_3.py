# ""
# Escreva um programa que imprime a tabuada de um número fornecido pelo usuário (por exemplo, a tabuada do 5).
# ""

numero_tabuada = input("Digite o numero que voce quer saber a tabuada:")

for i in range(1,11):
    print(f'{numero_tabuada} * {i} = {int(numero_tabuada) * int(i)}')

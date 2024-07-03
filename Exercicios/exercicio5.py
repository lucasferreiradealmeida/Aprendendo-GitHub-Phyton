"""
Faça um programa que coloque um * entre cada caractere de uma string digitada pelo usuário e mostre-o.
"""

nome = input('digite seu nome:')
i = 0
resultado = "*"

while i < len(nome):
    resultado += nome[i] + "*"
    i += 1

print(resultado)




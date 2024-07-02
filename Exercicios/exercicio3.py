"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = input('digite a hora:')
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('bom dia 0-11')
    elif hora >= 12 and hora <= 17:
        print('boa tarde 12-17')
    elif hora >= 18 and hora <= 23:
        print('boa noite 18-23')
except:
    print('hora invalida')
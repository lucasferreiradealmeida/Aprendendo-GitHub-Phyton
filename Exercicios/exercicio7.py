"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'lucas'
letra_acertada = ''
somatorio = 0


while True:
    letra_digitada = input("Digite uma letra:")
    if len(letra_digitada) != 1:
        print('Digite apenas uma letra')
        continue
    somatorio += 1

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
    else:
        print('Essa letra não está dentro da palavra secreta')

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra secreta:{palavra_formada}')
    print(f'Somatorio: {somatorio}')

    if palavra_formada ==  palavra_secreta:
        os.system('cls')
        print('VOCÊ ACERTOU!')
        print(f'A palavra era:{palavra_secreta}')
        print(f'O numero de tentativas foi:{somatorio}')

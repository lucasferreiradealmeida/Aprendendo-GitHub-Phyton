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

palavra_secreta = 'Lucas'

while True:
    letra_digitada = input("Digite uma letra:")
    if len(letra_digitada) != 1 and letra_digitada != ' ':
        print('Digite apenas uma letra')
    else:
        if letra_digitada in palavra_secreta:
            letra_acertadas += letra_digitada
        for letra_secreta in palavra_secreta:
            print(letra_secreta)
        

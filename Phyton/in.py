#in é um operador utilizado para verificar se um elemento está presente em uma sequência
nome = input('digite o seu nome:')
encontrar = input('me fale o que deseja encontrar:')

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
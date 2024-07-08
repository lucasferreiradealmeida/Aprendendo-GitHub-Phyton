# Exemplos de uso do laço for em Python

# 1. Iterando sobre uma sequência de números usando range()
# O range(5) gera uma sequência de números de 0 a 4
print("Iterando sobre uma sequência de números:")
for i in range(5):
    print(i)

# 2. Iterando sobre uma lista
# A lista pode conter qualquer tipo de elementos
lista = [10, 20, 30, 40, 50]
print("\nIterando sobre uma lista:")
for elemento in lista:
    print(elemento)

# 3. Iterando sobre uma string
# Cada caractere na string é iterado individualmente
texto = "Python"
print("\nIterando sobre uma string:")
for caractere in texto:
    print(caractere)

# 4. Usando enumerate() para obter índices e valores
# Enumerate retorna um par (índice, valor) para cada item na lista
print("\nUsando enumerate para obter índices e valores:")
lista_com_indices = ['a', 'b', 'c']
for indice, valor in enumerate(lista_com_indices):
    print(f"Índice: {indice}, Valor: {valor}")

# 5. Iterando sobre duas listas ao mesmo tempo usando zip()
# Zip combina duas listas, permitindo iterar sobre ambas simultaneamente
print("\nIterando sobre duas listas com zip:")
lista_numeros = [1, 2, 3]
lista_letras = ['x', 'y', 'z']
for numero, letra in zip(lista_numeros, lista_letras):
    print(f"Número: {numero}, Letra: {letra}")

# 6. Iterando sobre um dicionário
# Iterando sobre as chaves de um dicionário
dicionario = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}
print("\nIterando sobre um dicionário (chaves):")
for chave in dicionario:
    print(f"Chave: {chave}, Valor: {dicionario[chave]}")

# Iterando sobre os itens (pares chave-valor) de um dicionário
print("\nIterando sobre um dicionário (itens):")
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

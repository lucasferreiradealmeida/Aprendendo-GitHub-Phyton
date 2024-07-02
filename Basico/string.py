#aspas simples
print('Lucas Ferreira')
print(1,'Lucas "Ferreira"')
#aspas duplas
print("Lucas Ferreira")
print(2,"Lucas 'Ferreira'")
# print("Lucas "Ferreira") #errado,não compila
#escape
print("Lucas \"Ferreira\"")
#r
print(r"Lucas \"Ferreira")


#Formatacao de strings


nome = 'lucas'
altura = 1.71
dinheiro = 10000000.5
peso = 69
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.1f} de altura' # :.(numero)f   serve para voce decidir quantos numeros apos a ponto voce quer mostrar
print(linha_1)
linha_2 = f'{nome} tem {altura:.3f} de altura'
print(linha_2)
linha_3 = f'{nome} tem {dinheiro:,.3f} de altura' # :,.(numero)f   serve para voce seperar as casas
print(linha_3)

a = 'AAAAA'
b = 'BBBBB'
c = 1.5
string = 'b={1} a={0} b={1} c={2:.2f} c={2:.5f}'
formato = string.format(a,b,c) # a = INDICE 0 b = INDICE 1 c = INDICE 2(que nem vetor)
print(formato)

#função para contar string

variavel = 'lucas'
print(len(variavel))

#fatiamento

variavel = 'lucas ferreira'
print(variavel[0:7:1])
variavel_invertida = 'lucas ferreira'
print(variavel_invertida[::-1])
#Print


print(7,10,2003, sep="-", end="\n")
print("Licas")
print(10,2003, sep="-", end="##")
print("Lucas")


#String


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


#Numeros


print(    type(10)   )
print(    type(1.0)   )
print(type(0),type(0.0),type('lucas'))


#Boolean


print(10 == 10)
print(10 == 11)
print(10 != 11)
print(10 < 11)
print(10 <= 11)
print(10 > 11)
print(10 >= 11)
print(type(10 == 10))


#Correção de tipos


# print('1'+ 1)    (ESTÁ ERRADO)
print(int('1') + 1)
print(float('1') + 1)
print(str(1) + 'e')


#Variaveis

nome = 'lucas'
idade = 20
maior_de_idade = idade >= 18
print('nome:', nome ,'idade:', idade)
print(maior_de_idade)


#Peculiaridades matematica


divisao = 10 / 3 #float
print(divisao)
divisao_inteira = 10 // 3
print(divisao_inteira)
exponenciacao = 2 ** 10
print(exponenciacao)


#concatenacao e repeticao


concatenacao = 'Lucas ' + 'Ferreira ' + 'de ' + 'Almeida'
print(concatenacao)
a_dez_vezes = 'a' * 10
print(a_dez_vezes)


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


#formatação de strings

a = 'AAAAA'
b = 'BBBBB'
c = 1.5
string = 'b={1} a={0} b={1} c={2:.2f} c={2:.5f}'
formato = string.format(a,b,c) # a = INDICE 0 b = INDICE 1 c = INDICE 2(que nem vetor)
print(formato)


#input


nome = input('qual é o seu nome?')
print(f'o seu nome é{nome=}')

numero_1=input('me fale o primeiro numero')
numero_2=input('me fale o segundo numero')

int_numero_1=int(numero_1)
int_numero_2=int(numero_2)

print(f'a soma dos numeros é:{int_numero_1 + int_numero_2}')
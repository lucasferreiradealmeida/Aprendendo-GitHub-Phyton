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

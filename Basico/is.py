# is = é
# is not = não é
#none = não valor
# id = endereço na memoria

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça nada")

if passou_no_if is None:    
    print("Nao passou no if")
else:
    print("Passou no if")
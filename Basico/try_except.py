#parecido com if e else porém ele sai se der erro
#try:executa o que estiver dentro
#except:trata o erro

numero_str = input('vou dobrar o numero que vc quiser:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_float} é {numero_float * 2}')
except:
    print('você não digitou um numero')

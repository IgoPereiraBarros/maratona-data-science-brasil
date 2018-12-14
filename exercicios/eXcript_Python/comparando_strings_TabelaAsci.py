'''if 'a' > 'X':
    print('Sim')
else:
    print('Não')

if 'a' > '9':
    print('Sim')
else:
    print('Não')'''

#print(ord('o')) # passo uma caracter por parametro e esta funcao retorna o valor correspondendo a mesma
#print(chr(111)) # passo um numero por parametro e esta funcao retorna o caracter correspodende ao mesmo

for c in range(123):
    asci = str(c) + ' - ' + chr(c)
    print(asci)


from datetime import date
from time import sleep
ano = int(input('Digite um ano para verificar se é Bissexto ou não, ou 0(zero) para verificar o ano atual:  '))
print('Verificando...')
sleep(3)
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

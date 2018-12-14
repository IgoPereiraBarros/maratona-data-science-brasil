from datetime import date as d
ano_nascimento = int(input('Informe o ano de nascimento: '))

atual = d.today().year
idade = atual - ano_nascimento

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')




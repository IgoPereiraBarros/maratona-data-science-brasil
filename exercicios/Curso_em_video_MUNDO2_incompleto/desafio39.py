from datetime import date as d

ano_nascimento = int(input('Informe seu ano de nascimento: '))
atual = d.today().year
idade = atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, idade, atual))

if idade == 18:
    print('Hora de se alistar')
elif idade < 18:
    print('Aianda vai se alistar')
    print('Ainda falta {} anos para se alistar'.format(18 - idade))
    print('Portanto, seu aliastamento sera em {}'.format(atual + (18 - idade)))
elif idade > 18:
    print('Passou do tempo de alistamento')
    print('Ja passou {} anos da idade certa do alistamento '.format(idade - 18))
    print('Portanto, seu alistamento foi em {}'.format(atual - (idade - 18)))

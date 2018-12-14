nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Reprovado')
elif 5.0 <= media <= 6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')

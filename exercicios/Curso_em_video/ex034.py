sal = float(input('Digite o valor o seu salário R$: '))
if sal > 1200:
    sal = sal + (sal * 0.1)
    print('Seu novo salário, com aumento de 10% ficou {:.2f}'.format(sal))
else:
    sal = sal + (sal * 0.15)
    print('Seu novo salário, com aumento de 15% ficou {:.2f}'.format(sal))

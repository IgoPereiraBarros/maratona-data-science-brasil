n1 = float(input('Digite suu aprimeira nota: '))
n2 = float(input('Digite seu segunda nota: '))
m = (n1 + n2) / 2
print('Sua media foi {:.2f}'.format(m))
print('Média boa' if m >= 6 else 'Média ruim')

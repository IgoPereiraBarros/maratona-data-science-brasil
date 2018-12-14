lar = float(input('Digite o valor da  largura da parede: '))
alt = float(input('Digite o valor da altura da parede: '))
a = lar * alt
print('Sua parede tem dimenção de {} x {} e sua área mede {} m²'.format(lar, alt, a))
tinta = a / 2
print('Para pintar essa parede inteira precisará de {} litros de tinta'.format(tinta))
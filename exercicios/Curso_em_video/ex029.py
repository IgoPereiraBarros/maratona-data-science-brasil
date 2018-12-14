vel = float(input('Informe a velocidade em que anda no seu carro: '))

if vel > 80:
    print('MULTADO!')
    multa = (vel - 80) * 7
    print('Valor da multa foi {}'.format(multa))
print('Diriga com cuidado e bastante atenção! Cuide-se!')

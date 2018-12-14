altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')

print('IMC: {}'.format(imc))
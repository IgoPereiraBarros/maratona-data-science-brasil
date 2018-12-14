binario = []

number = int(input('Digite um número inteiro'))

while number >= 1:
    resto = int(number) % 2
    number /= 2
    binario.append(resto)

binario.reverse()
print(binario)

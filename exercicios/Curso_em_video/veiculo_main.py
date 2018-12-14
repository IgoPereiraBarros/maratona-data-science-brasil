from Samuel import Veiculo as v

opcao = v.menu()

while 1 <= opcao < 4:
    if opcao == 1:
        v.criar_veiculo()
    elif opcao == 2:
        v.andar()
    elif opcao == 3:
        v.nivel_gasolina()
    elif opcao == 3:
        v.adcionar_gasolina()
    opcao = v.menu()


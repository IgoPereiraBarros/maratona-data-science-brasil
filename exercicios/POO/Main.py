from Simulador import *


def main():
    semente = int(input('Digite a semente para gerar números pseudos-aleatórios: '))
    jogo = Simulador(semente)

    fim = False
    while not fim:
        jogo.sorteio()
        opcao = input('Deseja utilizar o volume sorteado (s/n)? ')

        if opcao == 's' or opcao == 'S':
            fim = jogo.deposito()  # retorna True caso o balde fique cheio
        else:
            fim = True
        jogo.finaliza()


main()

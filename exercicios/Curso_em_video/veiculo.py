

class Veiculo(object):
        nome_veiculo = 0

        def __init__(self, nome, consumo_combustivel):
            self.nome = nome
            self.consummo_combustivel = consumo_combustivel
            self.quantidade_combustivel = 0


        def getNome(self):
            return self.nome

        def setNome(self, nome):
            self.nome = nome

        nome = property(
            fget=getNome,
            fset=setNome
        )

        def getConsumo_Combustivel(self):
            return self.consummo_combustivel

        def setConsumo_Combustivel(self, consumo_combustivel):
            self.consummo_combustivel = consumo_combustivel

        comsumo_combustivel = property(
            fget=getConsumo_Combustivel,
            fset=setConsumo_Combustivel
        )

        def getQuantidade_Combustivel(self):
            return self.quantidade_combustivel

        def setQuantidade_Combustivel(self, quantidade_combustivel):
            self.quantidade_combustivel = quantidade_combustivel

        quantidade_combustivel = property(
            fget=getQuantidade_Combustivel,
            fset=setQuantidade_Combustivel
        )

        @staticmethod
        def menu():
            print('\n' + '-='*9 + 'MENU' + '-='*9)
            print('1 - Criar veículo')
            print('2 - Andar')
            print('3 - Verificar nível atual da gasolina')
            print('4 - Adicionar gasolina')
            print('-=' * 20)
            op = int(input('\nO que deseja realizar? '))
            return op

        def criar_veiculo(self, nome):
            self.nome = str(input('Digite o nome do veículo: '))
            self.setNome(nome)

        @staticmethod
        def andar():
            gasosa = 12
            '''if Veiculo.getQuantidade_Combustivel() > 0:
                Veiculo.setConsumo_Combustivel = Veiculo.getConsumo_Combustivel() - 12'''

        @staticmethod
        def nivel_gasolina():
            return print('Nível atual da gasolina: {} L'.format(Veiculo.getConsumo_Combustivel))
        @staticmethod
        def adcionar_gasolina():
            return print('Adcionar gasosa')


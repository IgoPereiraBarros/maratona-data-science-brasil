class Veiculo:

	pass

class Carro(Veiculo):
	pass

class Trem(Veiculo):
	pass

class CarroTrem(Carro, Trem):
	pass

print(CarroTrem.__mro__)
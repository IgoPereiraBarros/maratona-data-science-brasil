'''
Decorator --> é uma função que que recebe outra função como parâmetro, gera uma nova função que adiciona algumas
			  funcionalidades à função original e a retorna essa função.

* Adiciona um comportamento a um objeto ja existente em tempo de execução.
* Agrega dinamicamente responsabilidades adicionais a um objeto
'''

'''def modificar(funcao):
	def sub(a, b):
		return a - b
	return sub

@modificar # aqui estou passando as funcionalidades do função modificar() a função somar(), com isso, ha uma substituição de tarefas
def somar(a, b):
	return a + b

print(somar(2, 3))'''

'''def modificar(funcao):
	def sum_par(a, b):
		if a % 2 == 0 or b % 2 == 0:
			return a + b
		return a - b
	return sum_par

@modificar
def somar(a, b):
	return a + b

print(somar(1, 1))'''

def meu_decorator(fat):
    def fat(x):
        cont = x
        f = 1
        while cont > 0:
            f *= cont
            cont -= 1
        return f
    return fat
    

@meu_decorator
def dobro(x):
    return 2 * x

print(dobro(5))
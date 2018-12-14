
class TransacaoInvalida(Exception):

	def __init__(self, saldo_atual, qtd):
		super().__init__('sua conta está vazia {}'.format(qtd))
		self.saldo_atual = saldo_atual
		self.qtd = qtd

	def excesso(self):
		return self.qtd - self.saldo_atual

try:
	t = TransacaoInvalida(20, 12)
	raise TransacaoInvalida(t.saldo_atual, t.qtd)
except TransacaoInvalida as e:
	if t.qtd >= t.saldo_atual:
		print('Você não tem saldo suficente, falta R$ {}, 00 '.format(e.excesso()))
	else:
		print('Isso foi enbaraçoso')
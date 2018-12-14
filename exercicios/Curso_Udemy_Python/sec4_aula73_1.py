import sec4_aula73
import logging

class Usuario:

	def __init__(self, usuario, senha):
		self.usuario = usuario
		self.senha = senha
		self.dict_user = {'1': 'Igo', '2': 'Luana', '3': 'Afonso', '4': 'Dina'}

		formatt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		#logging.basicConfig(nome do arquivo a ser gravado, o tipo de test, tipo de gravação do arquivo, horaEdata-nome-root-message)
		logging.basicConfig(filename="testes.log", level=logging.DEBUG, filemode='w', format=formatt, datefmt='%d/%m/%Y %I:%M:%S %p')

		self.logger = logging.getLogger(__name__)

	def alterar_senha(self, nova_senha):
		self.senha = nova_senha
		self.logger.info('Senha alterada!')

	def auth(self, usuario, senha):
		if self.usuario != usuario or self.senha != senha:
			self.logger.warning('Tentativa de fazer login inválido!')
			return False
		return True

	def get_usuario_by_id(self, usuario_id):
		user = self.dict_user.get(usuario_id, None)
		if user is None:
			self.logger.error('Id do usuário não existe: {}'.format(usuario_id))
			return None
		return user

	def abrir_arquivo_usuario(self):
		try:
			open('/path/to/does/not/exist', 'rb')
		except (SystemExit, KeyboardInterrupt):
			raise
		except Exception as e:
			self.logger.exception('Erro: {}'.format(e))

	def algoritmo_complex(self, items):
		for i, items in enumerate(items):
			# faz algum complexo algoritmo_complex
			self.logger.debug('{} iterador; item = {}'.format(i, items))


if __name__ == '__main__':
	u = Usuario('igo', '123')
	u.alterar_senha('1234')
	u.auth('igo', '12')
	u.get_usuario_by_id('8')
	u.abrir_arquivo_usuario()
	u.algoritmo_complex([1,2,3])
	sec4_aula73.test_execucao()


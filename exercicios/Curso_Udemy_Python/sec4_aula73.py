import logging

def test_execucao():

	formatt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	#logging.basicConfig(nome do arquivo a ser gravado, o tipo de test, tipo de gravação do arquivo, horaEdata-nome-root-message)
	logging.basicConfig(filename="testes.log", level=logging.DEBUG, filemode='w', format=formatt, datefmt='%d/%m/%Y %I:%M:%S %p')

	'''logging.info('Mensagem de informação')
	logging.debug('Mensagem de debug')
	logging.error('Mensagem de erro')'''

	#logger = logging.getLogger(__name__)
	logger = logging.getLogger(__file__)

	'''logger.info('Mensagem de informação')
				logger.debug('Mensagem de debug')
				logger.error('Mensagem de erro')
			'''
if __name__ == '__main__':
	test_execucao()
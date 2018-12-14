from sec6_aula91_1_db import DataBase

if __name__ == '__main__':
	database = DataBase()

	database.connects()
	database.create_table()
	#database.insert_client('Igo Pereira Barros', 123, 1111123442, 'igorestacioceut@gmail.com')
	#database.insert_client('Maria Dina Pereira', 1234, 11111111100, 'dina@gmail.com')
	#database.insert_client('Maria Luana Pereira Barros', 12345, 22222222200, 'marialuana@gmail.com')
	#database.insert_client('Afonso da Paz Barros', 123456, 33333333300, 'afonso@gmail.com')
	#database.buscar_client('33333333300')
	#database.buscar_client('111.111.111-00')
	#database.buscar_client('222.222.222-00')
	#database.buscar_client('1111123442')
	#database.buscar_email('igorestacioceut@gmail.com')
	#database.delete_client('1111123442')
	print(database.login('Igo Pereira Barros', '123'))
	database.disconnect()
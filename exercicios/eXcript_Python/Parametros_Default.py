def login(sistema, user='root', pas='123'):
    if user == 'root' and pas == '123':
        print('Login efetuado com sucesso')
    else:
        print('Usuário ou senha incorretos')

login()
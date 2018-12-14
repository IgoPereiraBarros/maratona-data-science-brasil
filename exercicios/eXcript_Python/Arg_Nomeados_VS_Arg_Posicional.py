def mini_cadastro(nome, sobrenome, idade, sexo):
    print('Nome: {}, Sobrenome: {}, Idade: {}, Sexo: {}'.format(nome, sobrenome, idade, sexo))

mini_cadastro('Igor', sobrenome='Pereira', idade=21, sexo='M')

mini_cadastro(idade=21,   # como aqui tem um conceito de chave - valor(dicionario), nao importa a ordem declarada, a chamada sempre identificará a ordem dos argumentos.
              sexo='M',
              nome='Igo',
              sobrenome='Barros')

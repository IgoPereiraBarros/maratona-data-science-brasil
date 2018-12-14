'''
Quando utilizar Mixins?

1) Se vc desejar reutilizar uma determinada feature em várias classes diferentes
2) Para melhorar a modularidade

Mixins é uma forma controlada de adicionar funcionalidades  as classes

Propriedades:
1) não deve ser extendida
2) não deve ser instanciada

Em python, o conceito de Mixins é implementada utilizando herança multipla.

'''

class Livro(object):

	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo

class LivroHTMLMixim(object):

	def redenrizar(self):
		return ('<html>\n<title>%s</title>\n<body>\n%s\n</body>\n</html>') % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixim):
	pass

livro_html = LivroHTML('HTML COMO PROGRAMAR', 'Web Desing')

print(livro_html.redenrizar())
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pessoa(Base):

	__tablename__ = 'pessoa'
	id = Column(Integer, primary_key=True)
	nome = Column(String(100), nullable=False)

	def __repr__(self):
		return 'ID: %s, nome: %s' % (self.id, self.nome)

class Endereco(Base):

	__tablename__ = 'endereco'
	id = Column(Integer, primary_key=True)
	nome_rua = Column(String(100))
	bairro = Column(String(100))
	cep = Column(String(20))
	id_pessoa = Column(Integer, ForeignKey('pessoa.id')) # aqui é onde faz o relacionamento com a tabela pessoa
	pessoa = relationship(Pessoa) #Aqui informa qual classe que está relacionando com a classe atual


engine = create_engine('sqlite:///database2.db')

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	#pessoa = Pessoa(id='1', nome='Igor Pereira Barros')
	pessoa2 = Pessoa(id='2', nome='Maria Luana Pereira Barros')

	Session = sessionmaker(bind=engine)
	session = Session()
	#session.add(pessoa)
	session.add(pessoa2)
	session.commit()
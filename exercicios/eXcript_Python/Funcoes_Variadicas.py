def lista_de_argumentos(*args):
    print(args)


def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)


def argumentos(*args, **kwargs):
    print('-=' * 20)
    print(args)
    print(kwargs)


lista_de_argumentos(1, 2, 3, 4, 5)

lista_de_argumentos_associativos(um=1, dois=1, tres=3, quadro=4)

argumentos(1, 2, 3, 4, um=1, dois=2, tres=3, quadro=4)

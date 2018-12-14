import requests
import json



def requisicao(title):
    try:
        req = requests.get('http://www.omdbapi.com/?t={}&type=movie'.format(title))
        j_dict = json.loads(req.text)
        return j_dict
    except Exception as e:
        print('Erro na conexão')
        return None

def print_details(filme):
    print('exemplo: {}'.format(filme['Title']))


sair = False
while not sair:
    op = input('Entre com um filme: ').lower()

    if op == 'sair':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('filme não encontrado')
        else:
            print_details(filme)

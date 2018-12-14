from time import  sleep
cidade = str(input('Informe o nome de uma cidade: ')).strip()
print('Vamos verificar se a cidade digitada começa com o nome Santo...')
sleep(5)
if cidade[0] in 'Santo' and cidade.upper() or cidade.lower():
    print('Sim')
else:
    print('Não')
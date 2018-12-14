frase = 'Curso em Vídeo de Python'
frase1 = '     Igo Pereira Barros        '

print("""Allows your Windows Python program to play and stop MP3s, "
      "without opening an external player or requiring any external "
      "programs. A very simple interface for the common case (playing an entire MP3),"
      " with an API for more complex tasks (e.g. playing from seconds 30 to 45 of an MP3).""")


# =============== Fatiamento ===================
print(frase[9]) # imprimi o caracter no índice [9]
print(frase[3:10]) # imprimi os caracter do índice 3 ao 10, só que não imprimi o último caracter que é o [10]
print(frase[15:25]) # imprimi os caracter de índice [15] ao [25], como essa frase vai até o índice 24, o último caracter é impresso
print(frase[7:25:2]) # imprimi os caracter de índice [7] ao [25] (o tamanho da frase é 24), pulando de 2 em 2
print(frase[:10]) # quando não tem o primeiro índice, significa que inicia do índice 0 e vai até o 10
print(frase[13:]) # quando não tem o último índice indica que vai até o final dos caracter, nesse caso o último caracter é impresso

# ================== Análise ====================
print(frase[5::4]) # comeca no indice 5 vai ate o final, pulando de 4 em 4
print(frase.__len__()) # indica a quantidade de indices que a frase contém (comprimento da frase)
#ou
print(len(frase)) # aqui é a mesma situação de cima
print(frase.count('o')) # indica quantas letras o (minúsculo) contém na frase
print(frase.count('o', 0, 15)) # indica quantas letras o (minusculas) entre os indices 0 e 15 contém
print(frase.upper().count('O')) # aqui primeiro eu coloco os o's em Maúsculos e depois conto quantos tem, inicialmente não tinha nenhum
print(frase.find('rso')) # indica o primeiro indice do intervalo dos cacacteres entre as  letras ('rso')
print(frase.find('Android')) # quando ele não acha uma string na frase analisada ele retorna (-1), indicando que não achou essa string
print('Curso' in frase) # verifica se o caracter passo tem na frase analisada, o retorno é dado em booleano (True ou False)

# ================== Transformação ===============
print(frase.replace('Python', 'Android')) # onde tiver a palavra Python na frase será substituído pela palrava Android
print(frase.upper()) # coloca todas as letras em Maiúsculo
print(frase.lower()) # coloca todas as letras em Minúsculo
print(frase.capitalize()) # coloca a primeira letra da frase inteira em Maiúsculo
print(frase.title()) # coloca a primeira letra depois de algum espaço em Maiúsculo
print(frase1.strip()) # remove os espaços que cotém nas extremidades da frase
print(frase1.rstrip()) # remove os espaços apenas da extremidade da direita
print(frase1.lstrip()) # remove os espaços apenas da extremidade da esquerda

# ================ Divisão ====================

print(frase.split()) # onde tiver espaço ele coloca uma divisão e separa todas as palavras, e cada palavra terá seu próprio indice de início e fim
                     # e cada palavra terá seu próprio índice único, por exemplo, a palavras ['Curso'] terá indice 0, pois é a primeira palavra da frase

# =================== Junção ===================
print('='.join(frase)) # ele sepada as palavras com o símbolo passado

# =============== Exemplos ===============
divi = frase.split()
print(divi[0]) # aqui mostra a palavra do indice 0
print(divi[0][2]) # aqui mostra a letra que tem indice 2 da frase que tem indice 0

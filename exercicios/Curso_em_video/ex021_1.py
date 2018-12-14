from pygame import mixer

print('='*20)
print(' 1 - Nome da musica')
print(' 2 - Nome da musica')
print(' 3 - Nome da musica')
print(' 4 - Nome da musica')
print('='*20)

musica = input('Informe o número correspodente a música que vc queria ouvir: ')
mp3 = input('Informe o formato da múscia: ')
escolha = musica + mp3

mixer.init()
mixer.music.load(escolha)
mixer.music.play()
input('=====================Aperte ENTER caso queira parar a música========================')

from pygame import mixer, event
mixer.init() #iniciando o uso da biblioteca do pygame
mixer.music.load('ex1.mp3') #busca a música
mixer.music.play() #inicia a música
input()
event.wait()  #encerra a música quando acabar

''''while mixer.music.get_busy():
    time.Clock().tick(10)'''

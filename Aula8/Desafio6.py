#from playsound import _playsoundNix

#_playsoundNix('teste.mp3')


from pygame import mixer

mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()
input('Agora você escuta?')



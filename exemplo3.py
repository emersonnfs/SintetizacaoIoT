from gtts import gTTS
from pygame import mixer

audio = gTTS("É nóis que voa, bruxão",lang='pt')
audio.save("bruxao.mp3")
mixer.init()
mixer.music.load("bruxao.mp3")
mixer.music.play()
input("quer terminar?")
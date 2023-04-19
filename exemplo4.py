from gtts import gTTS
import os

audio = gTTS("É nóis que voa, bruxão",lang='pt',slow=True)
audio.save("bruxao.mp3")
os.system("bruxao.mp3")
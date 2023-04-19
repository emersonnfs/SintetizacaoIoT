import pyttsx3

robo = pyttsx3.init()
robo.setProperty('rate', 140)
robo.setProperty('volume', 1.0)

#for voz in robo.getProperty('voices'):
#    robo.setProperty('voice', voz.id)
#    print(voz.id)
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
robo.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
msg = "hello"
robo.say(msg)
robo.runAndWait()
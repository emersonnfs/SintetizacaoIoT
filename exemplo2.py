import pyttsx3
from datetime import datetime
meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
agora = datetime.now()
hora = agora.hour
minuto = agora.minute

dia = datetime.today().day
mes = datetime.today().month
ano = datetime.today().year

msg = "Now it's " + str(hora) + " " + str(minuto) + "p.m."
msg += " on" + meses[mes] + " " + str(dia) + " " + str(ano)
robo = pyttsx3.init()

robo.setProperty('rate', 140)
robo.setProperty('volume', 1.0)
robo.say(msg)
robo.runAndWait()
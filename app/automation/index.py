import email
import smtplib

import smtplib
import email.message

def enviar_email():  
    caminho_html = "app/automation/template.html"
    with open(caminho_html, "r", encoding="utf-8") as f:
        corpo_email = f.read()

    msg = email.message.Message()
    msg['Subject'] = "Teste Deploy actions!"
    msg['From'] = "thaliaguedes1199@gmail.com"
    msg['To'] = "thaliaguedes1199@gmail.com"
    password = "tvwnvtpyskdfysul"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')



if __name__ == "__main__":
    enviar_email()
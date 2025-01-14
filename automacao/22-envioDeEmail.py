# PYTHON - AUTOMAÇÃO - ENVIAR E-MAILS EM MASSA ATRAVÉS DO OUTLOOK
# import win32com.client as win32
#
# outlook = win32.Dispatch('outlook.application')
# lista_emails = ["wbommc@gmail.com", "copiadorabgmax@gmail.com", "automacao@bgmax.com.br"]
# for email_env in lista_emails:
#     email = outlook.CreateItem(0)
#     email.To = email_env
#     email.Subject = "Curso de Automação com Python-Selenium"
#     email.HTMLBody = "Este é um e-mail teste do curso de automação com Python - Selenium"
#     anexo = r"C:\Treinamentos Python\Marketing\Python - Módulo IV.jpeg"
#     email.Attachments.Add(anexo)
#     email.Send()
# print("Emails Enviados")

# Em ambiente linux é necessario utilizar SMTP
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()
password = os.getenv('SENHA_APP')
email = os.getenv('MEU_EMAIL')
with open("email_body.html", "r", encoding='utf-8') as file:
    body = file.read()


lista_emails = ["wilson@teste.com", "copiadaora@teste.com", "automacao@bgmax.com.br", "danieltisantos@gmail.com"]
for email_env in lista_emails:
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email_env
    msg['Subject'] = "Curso de Automação com Python-Selenium"

    msg.attach(MIMEText(body, 'html'))

    with open("/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/bgmax.png", 'rb') as logo:
        logo_part = MIMEImage(logo.read())
        logo_part.add_header('Content-ID', '<logo>')
        msg.attach(logo_part)

    anexo = "/home/zenxbr/Downloads/Daniel_JS._Python.pdf"
    with open(anexo, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={anexo}')
        msg.attach(part)

    # Conectando ao servidor SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(msg['From'], email_env, msg.as_string())
        print(f"E-mail enviado para {email_env}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {email_env}: {e}")
    finally:
        server.quit()

print("Emails Enviados")

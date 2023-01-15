import smtplib
import datetime 

## Les parametres d'authentification
gmail_user = 'chris.lyon.tech@gmail.com'
gmail_password = '$Amiga2000!'

## Time stamp 
ts = datetime.datetime.now().strftime("le %X à %x")

## les parametres du messages
from_user = gmail_user
to_user = ['test@chrislyon.fr', 'christophe.bonnet@groupe-sra.fr']
sujet = 'TEST DE MESSAGE '+ts
corps = """

Bonjour 
je suis un essai et le corps du message

Cordialement
Chris

"""

## La construction du message et l'encodage
email = """\
From: %s
To: %s
Subject: %s

%s
""" % (from_user, ", ".join(to_user), sujet, corps)

email_text = email.encode( encoding='UTF-8', errors='ignore')

## La connexion et l'envoi du message via gmail
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    try:
        server.login(gmail_user, gmail_password)
    except:
        print("Erreur sur l'authentification")
    server.sendmail(from_user, to_user, email_text)
    server.close()

    print('Envoi email effectué')
except:
    print('Problème envoi email')

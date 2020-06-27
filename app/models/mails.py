from flask_mail import Message
from ..constantes import MAIL_USERNAME
from flask import url_for
from ..app import mail

class Classe_mails():
    @staticmethod
    def send_reset_email(user):
        token = user.get_reset_token()
        msg = Message("Changement de mot de passe",
                      sender=MAIL_USERNAME,
                      recipients=[user.mail])
        msg.body = f'''Pour modifier votre mot de passe, cliquez sur le lien suivant:
    	{url_for('reset_token', token=token, _external=True)}

    Si vous n'êtes pas à l'origine de cette demande, veuillez ne pas tenir compte de cet email.

    Email généré automatiquement, merci de ne pas y répondre.
    '''
        mail.send(msg)

    @staticmethod
    def send_cataloguer_contact_mail(user, numero_inventaire, objet, message, copie):
        recipients = [MAIL_USERNAME]
        if copie == True:
            recipients.append(user.mail)
        msg = Message(str(numero_inventaire) + " -- " + objet,
                      sender=MAIL_USERNAME,
                      recipients=recipients)
        msg.body = message
        mail.send(msg)
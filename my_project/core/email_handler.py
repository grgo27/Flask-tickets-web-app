from flask_mail import Message
from my_project import mail
from my_project import sender_email

def send_winner_notification_email(email):
    msg = Message('Congratulations! You are a winner!',
                  sender=sender_email,
                  recipients=[email])
    
    msg.body = 'You have won the prize! Congratulations!'
    
    mail.send(msg)
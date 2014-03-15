from threading import Thread

from flask import render_template
from flask.ext.mail import Message

from app import mail
from config import ADMINS


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

@async
def send_async_email(msg):
    mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
    #FIXME need fix async send mail
    #send_async_email(msg)


def follower_notification(followed, follower):
    #NOTE change %s to format
    send_mail("[microblog] %s is now following you!" % follower.nickname,
              ADMINS[0],
              [follower.email],
              render_template('follower_email.txt',
                              user=followed, follower=follower),
              render_template('follower_email.html',
                              user=followed, follower=follower))

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLE = True
SECRET_KEY = 'you-will-never-guess'

#mail server setting
MAIL_SERVER = 'smtp.mail.ru'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'your_name@list.ru'
MAIL_PASSWORD = 'your_password'

# admin list
ADMINS = ['admin@example.com']

# pagination
#POSTS_PER_PAGE = 3

# full text search
#WHOOSH_BASE = os.path.join(basedir, 'search.db')

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

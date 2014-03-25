import os.path as op

from app import admin, db
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
from .models import User, Post

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin.add_view(MyView(name='Hello'))

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))

path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

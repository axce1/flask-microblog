import os.path as op

from app import app, db
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin,expose, AdminIndexView
from flask.ext.admin.contrib.fileadmin import FileAdmin
from .models import User, Post
from flask import url_for, redirect, request
from wtforms import form, fields, validators
from flask.ext import login


class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        #if user is None:
        #    raise validators.ValidationError('Invalid user')

        #if user.nickname != self.password.data:
        #    raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(nickname=self.login.data).first()


class MyModelView(ModelView):

    def is_accessible(self):
        if login.current_user.is_authenticated() and \
           login.current_user.role == 1:
            return True


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if (login.current_user.is_anonymous) or \
           (login.current_user.is_authenticated()):
            return redirect(url_for('.login_view'))

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        #if helpers.validate_form_on_submit(form):
            #user = form.get_user()
            #print (user)
            #if user.id == 1:
            #login.login_user(user)

        #if login.current_user.role==1:
        #    return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="#">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))



admin = Admin(app, 'Web-Admin', index_view=MyAdminIndexView(), \
              base_template='admin_base.html')

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Post, db.session))
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

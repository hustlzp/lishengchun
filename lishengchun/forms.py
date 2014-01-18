# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .uploadsets import workimages
from . import config


class WorkForm(Form):
    """Form for add & edit work"""
    type_id = SelectField('类别', [DataRequired('作品类别不能为空')], coerce=int)
    title = TextField('标题', [DataRequired('作品标题不能为空')])
    desc = TextAreaField('简介', description='选填')
    image = FileField('图片')
    #image = FileField('图片', [FileRequired('作品图片不能为空'), FileAllowed(workimages)])


class SigninForm(Form):
    username = TextField('用户名', [DataRequired('用户不能为空')])
    password = PasswordField('密码', [DataRequired('密码不能为空')])

    def validate_password(self, field):
        if self.username.data != config.AUTH_USERNAME or field.data != config.AUTH_PASSWORD:
            raise ValueError('用户名或密码错误')
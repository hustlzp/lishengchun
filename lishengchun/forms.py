# coding: utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .uploadsets import workimages


class WorkForm(Form):
    """Form for add & edit work"""
    type_id = SelectField('类别', [DataRequired('作品类别不能为空')], coerce=int)
    title = TextField('标题', [DataRequired('作品标题不能为空')])
    desc = TextAreaField('简介', description='选填')
    image = FileField('图片')
    #image = FileField('图片', [FileRequired('作品图片不能为空'), FileAllowed(workimages)])
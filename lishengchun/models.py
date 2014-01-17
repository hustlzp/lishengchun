# coding: utf-8
import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from .uploadsets import workimages

db = SQLAlchemy()


class WorkType(db.Model):
    """作品种类"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    show_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "WorkType %s" % self.name


class Work(db.Model):
    """作品"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    desc = db.Column(db.Text)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    image = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'))
    type = db.relationship('WorkType',
                           backref=db.backref('works', lazy='dynamic',
                                              order_by="desc(Work.created)"))

    @property
    def url(self):
        return workimages.url(self.image)

    def __repr__(self):
        return "Work %d" % self.title
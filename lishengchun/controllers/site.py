# coding: utf-8
from flask import render_template, Blueprint
from ..models import WorkType, Work

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """首页"""
    works = Work.query.order_by(Work.created.desc())
    return render_template('site/index.html', works=works)


@bp.route('/about')
def about():
    """关于"""
    return render_template('site/about.html')
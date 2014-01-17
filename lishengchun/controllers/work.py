# coding: utf-8
from flask import render_template, Blueprint
from ..models import Work

bp = Blueprint('work', __name__)


@bp.route('/<int:work_id>')
def view(work_id):
    """作品页"""
    work = Work.query.get_or_404(work_id)
    return render_template('work/work.html', work=work)
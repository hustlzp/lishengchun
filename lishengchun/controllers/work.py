# coding: utf-8
from flask import render_template, Blueprint
from ..models import Work, WorkType

bp = Blueprint('work', __name__)


@bp.route('/<int:work_id>')
def view(work_id):
    """作品页"""
    work = Work.query.get_or_404(work_id)
    return render_template('work/work.html', work=work)

@bp.route('/type/<int:type_id>')
def type(type_id):
    """作品类别页"""
    work_type = WorkType.query.get_or_404(type_id)
    return render_template('work/work_type.html', work_type=work_type)
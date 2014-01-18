# coding: utf-8
import os
from flask.ext.uploads import extension
from flask import render_template, Blueprint, request, redirect, url_for, session
from ..uploadsets import workimages
from PIL import Image
from ..forms import WorkForm, SigninForm
from ..models import db, Work, WorkType
from ..utils import random_filename

bp = Blueprint('admin', __name__)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        session.permanent = True
        session['role'] = 'admin'
        return redirect(url_for('site.index'))
    return render_template('admin/signin.html', form=form)


@bp.route('/signout')
def signout():
    session.pop('role', None)
    return redirect(url_for('site.index'))


@bp.route('/add_work', methods=['GET', 'POST'])
def add_work():
    """添加作品"""
    form = WorkForm()
    form.type_id.choices = [(t.id, t.name) for t in WorkType.query]
    if form.validate_on_submit():
        filename, w, h = save_image(request.files['image'], workimages)
        work = Work(image=filename, width=w, height=h, title=form.title.data,
                    type_id=form.type_id.data, desc=form.desc.data)
        db.session.add(work)
        db.session.commit()
        return redirect(url_for('work.view', work_id=work.id))
    return render_template('admin/add_work.html', form=form)


@bp.route('/work/<int:work_id>/edit', methods=['GET', 'POST'])
def edit_work(work_id):
    """编辑作品"""
    work = Work.query.get_or_404(work_id)
    form = WorkForm(obj=work)
    form.type_id.choices = [(t.id, t.name) for t in WorkType.query]
    if form.validate_on_submit():
        if form.image.has_file():
            filename, w, h = save_image(request.files['image'], workimages)
            work.image = filename
            work.width = w
            work.height = h
        work.title = form.title.data
        work.type_id = form.type_id.data
        work.desc = form.desc.data
        db.session.add(work)
        db.session.commit()
        return redirect(url_for('work.view', work_id=work_id))
    return render_template('admin/edit_work.html', work=work, form=form)


@bp.route('/work/<int:work_id>/delete')
def delete_work(work_id):
    work = Work.query.get_or_404(work_id)
    db.session.delete(work)
    db.session.commit()
    return redirect(url_for('site.index'))


def save_image(file_storage, upload_set):
    """获取上传图片的size，并保存"""
    image = Image.open(file_storage.stream)
    if image.mode != "RGB":
        image = image.convert("RGB")
    w, h = image.size
    ext = extension(file_storage.filename)
    filename = '%s.%s' % (random_filename(), ext)
    path = os.path.join(upload_set.config.destination, filename)
    image.save(path)
    return filename, w, h
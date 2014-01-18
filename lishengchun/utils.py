# coding: utf-8
import uuid
from flask import session


def random_filename():
    """生成伪随机文件名"""
    return str(uuid.uuid4())


def check_admin():
    """判断是否为管理员"""
    if 'role' not in session:
        return False
    if session['role'] != 'admin':
        session.pop('role', None)
        return False
    return True
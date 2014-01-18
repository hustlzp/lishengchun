# coding: utf-8
from functools import wraps
from flask import g, abort
from .utils import check_admin


class AdminPermission(object):
    def __call__(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            if not self.check():
                return self.deny()
            return func(*args, **kwargs)
        return decorator
 
    def check(self):
        """判断是否满足权限条件"""
        return check_admin()
 
    def deny(self, next_url=""):
        abort(403)

admin_permission = AdminPermission()
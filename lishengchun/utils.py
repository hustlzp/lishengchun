# coding: utf-8
import uuid


def random_filename():
    """生成伪随机文件名"""
    return str(uuid.uuid4())
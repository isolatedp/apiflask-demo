# src/blueprints/default.py
from apiflask import APIBlueprint
from flask import url_for, redirect

from src.controllers.defalut_controller import DefaultController

default_bp = APIBlueprint('default', __name__, url_prefix='/')

@default_bp.get('/')
def index():
    """
    跳轉到 API 文件頁面
    """
    return redirect(url_for('openapi.docs'))

@default_bp.get('/health')
def health(*args, **kwargs):
    """
    健康檢查端點
    """
    return DefaultController().get_health(args, kwargs)

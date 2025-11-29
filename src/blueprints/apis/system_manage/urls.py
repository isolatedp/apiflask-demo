# src/blueprints/apis/system_manage/urls.py
from apiflask import APIBlueprint
from .role_manage.urls import role_manage_bp
from .user_manage.urls import user_manage_bp
from .function_manage.urls import function_manage_bp


system_manage_bp = APIBlueprint("system_manage", __name__, url_prefix="/system-manage")
system_manage_bp.register_blueprint(role_manage_bp)
system_manage_bp.register_blueprint(user_manage_bp)
system_manage_bp.register_blueprint(function_manage_bp)

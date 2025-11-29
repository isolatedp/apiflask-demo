# src/blueprints/apis/urls.py
from apiflask import APIBlueprint
from controllers.api_health_controller import ApiHealthController
from .system_manage.urls import system_manage_bp

api_bp = APIBlueprint("apis", __name__, url_prefix="/apis")

@api_bp.get("/health-check/")
def health_check():
    return ApiHealthController().get_system_health()

api_bp.register_blueprint(system_manage_bp)

# src/blueprints/root_bp.py
from apiflask import APIBlueprint
from flask import redirect, url_for

from services.utils import generate_response
from services.enums import StatusEnums

root_bp = APIBlueprint('root', __name__, url_prefix='/')
@root_bp.get('/')
def index():
    return redirect(url_for('apis.health_check'))

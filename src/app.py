# src/app.py
from apiflask import APIFlask

from .configs import Configs
from .extends import extends


def create_app() -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object(Configs)
    extends.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app: APIFlask) -> None:
    from .blueprints.default import default_bp
    app.register_blueprint(default_bp)

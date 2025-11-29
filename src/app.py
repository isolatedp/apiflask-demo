# src/app.py
from apiflask import APIFlask
from configs import Configs


def create_app():
    app = APIFlask(__name__)
    app.config.from_object(Configs)
    
    register_blueprints(app)
    return app

def register_blueprints(app: APIFlask):
    from blueprints.root_bp import root_bp
    from blueprints.apis.urls import api_bp
    
    app.register_blueprint(root_bp)
    app.register_blueprint(api_bp)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
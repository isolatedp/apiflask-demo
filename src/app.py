# src/app.py
from apiflask import APIFlask


def create_app():
    app = APIFlask(__name__)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
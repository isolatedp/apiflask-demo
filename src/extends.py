# src/extends.py
from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


class Extends:
    db = SQLAlchemy()
    cors = CORS()

    def init_app(self, app: APIFlask):
        self.db.init_app(app)
        self.cors.init_app(app)
        return self
    
extends = Extends()
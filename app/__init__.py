from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from . import proyecto

    app.register_blueprint(proyecto.bp)

    return app
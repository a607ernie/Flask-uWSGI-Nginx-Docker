from flask import Flask,Blueprint
from app.api.api_test import api_test


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_test)

    return app

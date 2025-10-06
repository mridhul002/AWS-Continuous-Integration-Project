# app/__init__.py
from flask import Flask
from .web import register_routes

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

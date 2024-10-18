from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importer et attacher les routes à l'application
    from .routes import init_routes
    init_routes(app)

    return app

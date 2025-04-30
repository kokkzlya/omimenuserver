from flask import Flask
from flask_cors import CORS

from src.app.blueprints.auth import bp as auth_bp
from src.app.blueprints.products import bp as products_bp
from src.app import auth_guard, di
from src.infra.repositories.postgres import db

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    di.init_app(app)
    auth_guard.login_manager.init_app(app)

    return app

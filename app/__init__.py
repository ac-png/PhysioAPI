from flask import Flask
from app.db import db
from app.config import Config
from app.routes import init_routes
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    init_routes(app)

    return app

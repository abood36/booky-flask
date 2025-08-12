from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .config import Config
from .extensions import db, migrate, csrf
from .main import main as main_blueprint

def create_app(config_class=None):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config_class or Config)

    # initialise extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # register blueprints
    app.register_blueprint(main_blueprint)

    return app

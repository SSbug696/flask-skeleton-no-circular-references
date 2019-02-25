import os
from flask import Flask
from flask_migrate import Migrate
from .models import *
from .views import bp

app = Flask(__name__, instance_relative_config=True)


def create_app():
    migrate = Migrate()
    config_file = os.environ.get('APP_CONFIG_FILE')

    if config_file is None:
        raise 'Config file is not exist'

    app.config.from_object('instance.default')
    app.config.from_pyfile('%s.py' % config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(bp)

    return app

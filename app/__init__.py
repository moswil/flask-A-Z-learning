from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

import flask_restful as restful
import flask_login as login

from app.utils.logger import Logger

import config

app = Flask(__name__)
if app.config.get('ENV') == 'production':
    app.config.from_object(config.ProductionConfig)
elif app.config.get('ENV') == 'staging':
    app.config.from_object(config.StagingConfig)
elif app.config.get('ENV') == 'development':
    app.config.from_object(config.DevelopmentConfig)
else:
    app.config.from_object(config.TestingConfig)


rest_api = restful.Api(app=app, prefix='/api/v1')
db = SQLAlchemy(app=app)
ma = Marshmallow(app=app)
bcrypt = Bcrypt(app=app)

LOGGER = Logger().get_logger()

from app.errors import handlers  # noqa
from app import routes  # noqa

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

from app.users.models import AppUser  # noqa


# initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app=app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(AppUser).get(user_id)


init_login()

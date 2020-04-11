import tldextract

from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow

import flask_restful as restful
import flask_login as login

from app.utils.logger import Logger

import config as app_configs

app = Flask(__name__)
if app.config.get('ENV') == 'production':
    app.config.from_object(app_configs.ProductionConfig)
elif app.config.get('ENV') == 'staging':
    app.config.from_object(app_configs.StagingConfig)
elif app.config.get('ENV') == 'development':
    app.config.from_object(app_configs.DevelopmentConfig)
else:
    app.config.from_object(app_configs.TestingConfig)


rest_api = restful.Api(app=app, prefix='/api/v1')
db = SQLAlchemy(app=app)
ma = Marshmallow(app=app)

LOGGER = Logger().get_logger()

from app.errors import handlers  # noqa
from app import routes  # noqa

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

# from app.organisation.resolver import OrganisationResolver  # noqa


# def get_domain():
#     # TODO: Remove this test-related hack!
#     if app.config.get('ENV') == 'testing' and 'HTTP_ORIGIN' not in request.environ and 'HTTP_REFERER' not in request.environ:
#         return 'org'

#     origin = request.environ.get('HTTP_ORIGIN', '')
#     if not origin:  # Try to get from Referer header
#         origin = request.environ.get('HTTP_REFERER', '')
#         LOGGER.debug(f'No ORIGIN header, falling back to Referer: {origin} ')

#     if origin:
#         domain = tldextract.extract(origin).domain
#     else:
#         LOGGER.warning('Could not determine origin domain')
#         domain = ''

#     return domain


# @app.before_request
# def populate_organisation():
#     domain = get_domain()
#     LOGGER.info(f'Origin Domain: {domain}')  # TODO: remove this after testing

#     g.organisation = OrganisationResolver.resolve_from_domain(domain)


# Flask Admin Config

from app.users.models import User  # noqa


# initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app=app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


init_login()

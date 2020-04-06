from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

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

db = SQLAlchemy(app=app)


from app import routes, models  # noqa

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

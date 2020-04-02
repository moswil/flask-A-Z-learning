from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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
migrate = Migrate(app=app, db=db)


from app import routes, models  # noqa

from flask import Flask

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


from app import routes  # noqa

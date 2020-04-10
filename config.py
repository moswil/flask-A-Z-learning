import os
from dotenv import load_dotenv


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv('env/.env')
    DEBUG = os.getenv('DEBUG')
    TESTING = os.getenv('TESTING')
    CSRF_ENABLED = os.getenv('CSRF_ENABLED')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    SMTP_USERNAME = os.getenv('SMTP_USERNAME', None)
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', None)
    SMTP_SENDER_NAME = os.getenv('SMTP_SENDER_NAME', None)
    SMTP_SENDER_EMAIL = os.getenv('SMTP_SENDER_EMAIL', None)
    SMTP_HOST = os.getenv('SMTP_HOST', None)
    SMTP_PORT = os.getenv('SMTP_PORT', None)


class ProductionConfig(Config):
    load_dotenv('env/prod.env', override=True)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class StagingConfig(Config):
    load_dotenv('env/staging.env', override=True)
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(Config):
    load_dotenv('env/dev.env', override=True)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class TestingConfig(Config):
    load_dotenv('env/testing.env', override=True)
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

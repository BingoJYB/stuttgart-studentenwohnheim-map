from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = environ.get('TESTING')
    DEBUG = environ.get('DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    # URL
    BASE_URL = environ.get('BASE_URL')
    HOUSING_URL = environ.get('HOUSING_URL')

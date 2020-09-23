import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    # URL
    WOHNUNG_URL = os.getenv('WOHNUNG_URL')

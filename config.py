import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_HOSTNAME = os.getenv('FLASK_HOSTNAME')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    # URL
    BASE_URL = os.getenv('BASE_URL')
    HOUSING_URL = os.getenv('HOUSING_URL')

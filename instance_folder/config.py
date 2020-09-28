import os


APP_ROOT = os.path.join(os.path.dirname(__file__), '..')


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.urandom(16)

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')

    # URL
    BASE_URL = os.getenv('BASE_URL')
    WOHNUNG_URL = BASE_URL + os.getenv('WOHNUNG_RELATIVE_URL')

    # Image
    IMAGE_FOLDER = APP_ROOT + os.getenv('IMAGE_FOLDER')

from pathlib import Path

from flask import current_app


def get_image_url(image_url):
    return current_app.config['BASE_URL'] + image_url


def get_downloaded_image_path(wohnung_name):
    return current_app.config['IMAGE_FOLDER'] + '/' + wohnung_name


def check_image_folder_exist():
    Path(current_app.config['IMAGE_FOLDER']).mkdir(parents=True, exist_ok=True)

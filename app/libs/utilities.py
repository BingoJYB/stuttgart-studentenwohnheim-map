import os

from flask import current_app


def get_image_url(image_url):
    return current_app.config['BASE_URL'] + image_url


def get_downloaded_image_path(wohnung_name):
    return current_app.config['IMAGE_FOLDER'] + wohnung_name


def check_image_folder_exist():
    if not os.path.exists(current_app.config['IMAGE_FOLDER']):
        os.makedirs(current_app.config['IMAGE_FOLDER'])

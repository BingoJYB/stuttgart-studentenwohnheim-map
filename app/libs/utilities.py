import os

from flask import current_app


def get_image_url(image_url):
    return current_app.config['BASE_URL'] + image_url


def get_wohnung_detail_url(detail_url):
    return current_app.config['BASE_URL'] + detail_url


def get_downloaded_image_path(wohnung_name):
    return current_app.config['IMAGE_FOLDER'] + wohnung_name


def check_image_folder_exist():
    if not os.path.exists(current_app.config['IMAGE_FOLDER']):
        os.makedirs(current_app.config['IMAGE_FOLDER'])


def get_wohnung_url():
    return current_app.config['BASE_URL'] + current_app.config['WOHNUNG_RELATIVE_URL']


def get_map_api_key():
    return current_app.config['MAP_API_KEY']

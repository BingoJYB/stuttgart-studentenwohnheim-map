import requests
import cssutils
from bs4 import BeautifulSoup


class WebScraper(object):

    def __init__(self, url):
        page = requests.get(url)
        self.bs = BeautifulSoup(page.content, 'html.parser')

    def parse_page(self):
        room_image_urls = list()
        room_images = self.bs.find_all('div', class_='result-image')
        for image in room_images:
            background_image = cssutils.parseStyle(
                image['style'])['background-image']
            room_image_url = background_image.replace(
                'url(', '').replace(')', '')
            room_image_urls.append(room_image_url)
        room_info = self.bs.find_all('div', class_='result-text')

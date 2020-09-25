import requests
import cssutils
import shutil
from multiprocessing import Pool
from bs4 import BeautifulSoup

from app.models.wohnung import Wohnung
from app.models.studentenwohnheim import Studentenwohnheim
from app.libs.utilities import get_downloaded_image_path, get_image_url, check_image_folder_exist


class WebScraper(object):

    def __init__(self, url):
        page = requests.get(url)
        self.bs = BeautifulSoup(page.content, 'html.parser')
        self.studentenwohnheim = Studentenwohnheim()

    def parse_page(self):
        wohnung_results = self.bs.find_all('div', class_='housing-result-item')

        for wohnung_result in wohnung_results:
            wohnung_image = wohnung_result.find('div', class_='result-image')
            wohnung_image_url = cssutils.parseStyle(wohnung_image['style'])[
                'background-image'].replace('url(', '').replace(')', '')

            wohnung_info = wohnung_result.find('div', class_='result-text')
            wohnung_name = wohnung_info.find('h3').text
            address = wohnung_info.find_all('p')[0].find_all('span')
            address = ', '.join(list(map(lambda x: x.text, address)))
            price = wohnung_info.find_all('p')[1].text
            wohnung_details_link = wohnung_info.find('a')['href']

            wohnung = Wohnung(wohnung_image_url, wohnung_name,
                              address, price, wohnung_details_link)
            self.studentenwohnheim.wohnungen.append(wohnung)

    def __download_image(self, image_url, wohnung_name):
        real_image_url = get_image_url(image_url)
        image = requests.get(real_image_url, stream=True)
        image_path = get_downloaded_image_path(wohnung_name)

        with open(image_path, 'wb') as file:
            shutil.copyfileobj(image.raw, file)

    def download_images(self):
        pool = Pool()
        image_urls = [
            wohnung.image_url for wohnung in self.studentenwohnheim.wohnungen]
        wohnung_names = [
            wohnung.name for wohnung in self.studentenwohnheim.wohnungen]

        check_image_folder_exist()

        for image_url, wohnung_name in zip(image_urls, wohnung_names):
            pool.apply_async(self.__download_image,
                             args=(image_url, wohnung_name))

        pool.close()
        pool.join()

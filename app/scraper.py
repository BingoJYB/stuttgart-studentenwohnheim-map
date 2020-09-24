import requests
import cssutils
from bs4 import BeautifulSoup

from app.models.wohnung import Wohnung
from app.models.studentenwohnheim import Studentenwohnheim


class WebScraper(object):

    def __init__(self, url):
        self.studentenwohnheim = Studentenwohnheim()
        page = requests.get(url)
        self.bs = BeautifulSoup(page.content, 'html.parser')

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

        return self.studentenwohnheim

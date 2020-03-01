import requests
import cssutils
from bs4 import BeautifulSoup


class WebScraper(object):

    def __init__(self, url):
        page = requests.get(url)
        self.bs = BeautifulSoup(page.content, 'html.parser')

    def parse_page(self):
        housing_results = self.bs.find_all('div', class_='housing-result-item')
        houses = list()

        for housing_result in housing_results:
            housing_image = housing_result.find('div', class_='result-image')
            housing_image_url = cssutils.parseStyle(housing_image['style'])[
                'background-image'].replace('url(', '').replace(')', '')

            housing_info = housing_result.find('div', class_='result-text')
            housing_name = housing_info.find('h3').text
            address = housing_info.find_all('p')[0].find_all('span')
            address = ', '.join(list(map(lambda x: x.text, address)))
            price = housing_info.find_all('p')[1].text
            housing_details_link = housing_info.find('a')['href']

            house = {
                'image': housing_image_url,
                'name': housing_name,
                'address': address,
                'price': price,
                'detail': housing_details_link
            }
            houses.append(house)

        return houses

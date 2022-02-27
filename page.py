import requests
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url):
        self.html = requests.get(url)
        soup = BeautifulSoup(self.html.content, 'html.parser')
        self.title = soup.find('h1').text
        self.image_url = 'http://books.toscrape.com' + soup.find('img')['src'].removeprefix('../..')
        self.category = soup.findAll('li')[2].text.replace('\n', '')
        self.product_description = soup.find('article', {'class': 'product_page'}).select('p')[3].text
        product_info = soup.findAll('tr')
        self.upc = product_info[0].find('td').text
        self.price_excluding_tax = product_info[2].find('td').text
        self.price_including_tax = product_info[3].find('td').text
        self.number_available = product_info[5].find('td').text
        self.review_rating = product_info[6].find('td').text

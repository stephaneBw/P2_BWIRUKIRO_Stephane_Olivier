import requests
from bs4 import BeautifulSoup


class Page:
    def __init__(self, url):
        self.url = url  # l'URL de la page
        html = requests.get(self.url)
        soup = BeautifulSoup(html.content, 'html.parser')

        self.title = soup.find('h1').text  # titre du livre
        # scraper l’URL de l’image de couverture du livre
        self.image_url = 'http://books.toscrape.com' + soup.find('img')['src'].removeprefix('../..')
        # récupérer la category à laquelle appartient le livre
        self.category = soup.findAll('li')[2].text.replace('\n', '')
        # récupérer la description du livre
        self.product_description = soup.find('article', {'class': 'product_page'}).select('p')[3].text

        # récupérer les infos relatives au livre
        product_info = soup.findAll('tr')
        self.upc = product_info[0].find('td').text  # code produit du livre
        self.price_excluding_tax = product_info[2].find('td').text  # prix hors taxe du livre
        self.price_including_tax = product_info[3].find('td').text  # prix avec taxe du livre
        self.number_available = product_info[5].find('td').text  # le nombre de livres disponibles
        self.review_rating = product_info[6].find('td').text  # evaluation du livre


p = Page('http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')
liste = [p.url, p.title, p.image_url, p.category, p.upc, p.price_including_tax,
         p.price_excluding_tax, p.number_available, p.review_rating]
[print(i) for i in liste]

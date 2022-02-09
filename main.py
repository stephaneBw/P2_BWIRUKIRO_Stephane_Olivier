import requests
from bs4 import BeautifulSoup
import page

url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
response = requests.get(url)  # request
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')

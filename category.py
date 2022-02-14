import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
category_link = []  # list des liens vers les categories

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find('ul', {'class': 'nav nav-list'}).select('li')
    for i in ul:
        a = i.find('a')
        category_link.append(a['href'])
    del category_link[0]

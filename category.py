import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
category_link = []  # list des liens vers les categories

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find('ul', {'class': 'nav nav-list'}).select('li')

    # boucle pour recuperer les liens vers les categories de livres
    for i in ul:
        a = i.find('a')
        category_link.append(a['href'])

    del category_link[0]  # enlever le premier lien car il renvoie à l'ensemble des livres


def category_page(category_url):
    """
    :param category_url: prend en entrée l’url d’une category
    :return: la liste des urls des livres de la category en question
    """
    reponse = requests.get(category_url)
    if reponse.ok:
        category_soup = BeautifulSoup(reponse.text, 'html.parser')

        # ul verifie si la categorie s'étend sur plusieurs pages
        ul = category_soup.find('ul', {'class': 'pager'})
        print(ul)

        links = []  # list contenant les liens des livres d'une categorie
        tag_links = category_soup.findAll('h3')
        for tl in tag_links:
            a = tl.find('a')
            links.append(url + 'catalogue' + a['href'].removeprefix('../../..'))
        if ul is None:
            break
        if ul is not None:
            next_page = ul.find('li', {'class': 'next'}).find('a')
            next_page_url = category_url.removesuffix('index.html') + next_page['href']
            ul = None
            category_page(next_page_url)

        return links


print(category_page(category_url=url + category_link[0]))

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)
category_link = []  # list des liens vers les categories

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find('ul', {'class': 'nav nav-list'}).select('li')

    # boucle pour récupérer les liens vers les categories de livres
    for i in ul:
        a = i.find('a')
        category_link.append(a['href'])

    del category_link[0]  # enlever le premier lien, car il renvoie à l'ensemble des livres


def category_page(category_url, links=None, count=1):
    """
    :param count: cette variable compte le nombre de pages parcourues
    :param links: list qui va contenir les liens de tous les livres
    :param category_url: prend en entrée l’url d’une category
    :return: la liste des urls des livres de la category en question
    """
    if links is None:
        links = []

    reponse = requests.get(category_url)
    if reponse.ok:
        category_soup = BeautifulSoup(reponse.text, 'html.parser')

        # récupérer les infos sur la page
        links.append(by_page_category(category_url))

        # autre_page vérifie si la catégorie s’étend sur plusieurs pages
        autre_page = category_soup.find('ul', {'class': 'pager'})

        if autre_page is None:
            pass

        # s'il y a d’autres pages, les récupérer
        else:
            # next_page verify si le lien trouvé renvoie à la page suivante ou non
            next_page = autre_page.find('li', {'class': 'next'})

            # si le lien renvoie à la page précédente
            if next_page is None:
                pass

            # si le lien renvoie à la page suivante
            else:
                next_page_link = next_page.find('a')
                # page_extension va aider à supprimer les extensions des pages webs précédents
                page_extension = ('page-' + str(count) + '.html')
                if 'index.html' in category_url:
                    count = count + 1
                    category_url.removesuffix('index.html')
                    category_page(category_url.removesuffix('index.html') +
                                  next_page_link['href'], links, count)

                else:
                    count = count + 1
                    category_url.removesuffix(page_extension)
                    category_page(category_url.removesuffix(page_extension) +
                                  next_page_link['href'], links, count)

    return links


def by_page_category(lien):
    """
    :param lien: lien d'une seule page à scraper
    :return: liste des livres sur une page de la category
    """
    reponse = requests.get(lien)
    if reponse.ok:
        category_soup = BeautifulSoup(reponse.text, 'html.parser')

        links = []  # list contenant les liens des livres d'une page par category
        tag_links = category_soup.findAll('h3')
        for tl in tag_links:
            a = tl.find('a')
            links.append(url + 'catalogue' + a['href'].removeprefix('../../..'))
        return links

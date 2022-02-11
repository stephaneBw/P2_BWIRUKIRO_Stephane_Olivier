import requests
from bs4 import BeautifulSoup


def info_from_page(page_url):
    """
    :param page_url: prend en entrée un lien vers une page internet
    La fonction collecte les infos se trouvant sur la page
    :return: une liste qui contient les infos collectées
    """
    info = []  # list qui va contenir les infos scrapées
    response = requests.get(page_url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')

        # recuperation de l'url de l'image de couverture
        image = soup.find('img')
        image_url = 'http://books.toscrape.com' + image['src'].removeprefix('../..')

        # recuperation de la categorie auquel appartient le livre
        category_li = soup.findAll('li')
        category = category_li[2].text.removeprefix('\n').removesuffix('\n')

        # recuperation du titre du livre
        title = soup.find('h1')
        info = [page_url, title.text]  # premiere partie des infos scrapées

        # recuperer les infos qui sont dans la partie 'Product information'
        product_info = soup.findAll('tr')
        for i in product_info:
            th = i.find('th')
            if th.text != 'Tax' and th.text != 'Product Type':
                td = i.find('td')
                info.append(td.text)

        # ajouter de l'image_url et de la categorie dans la liste info
        info.append(category)
        info.append(image_url)
    return info

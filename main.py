import csv
import requests
from bs4 import BeautifulSoup
from page import info_from_page
from category import category_link, category_page

# demander a l’utilisateur de choisir s’il veut avoir les infos par categories
choix = input("Voulez vous voir les infos par categorie de livre ? si oui entrez 1"
              "si non entrez 2 : ")

url = 'http://books.toscrape.com/catalogue/'

# La list qui contient l'en-tête des infos scrapées
info_id = ['product_page_url', 'title', 'universal_ product_code (upc)',
           'price_including_tax', 'price_excluding_tax', 'number_available',
           'review_rating', 'product_description', 'category', 'image_url']

if choix == '1':
    page = 'page-' + input('Entrez le numero de la page que vous voulez consulter: ') + '.html'

    response = requests.get(url + page)  # request
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        tag_links = soup.findAll('h3')

        infos = []  # list qui va contenir les infos scrapées
        links = []  # list qui va cntenir les links vers les livres se trouvant sur une page

        # boucle pour recuperer les liens des livres se trouvant sur une page
        for tl in tag_links:
            a = tl.find('a')
            links.append(url + a['href'])

        # boucle pour recuperer les infos d’un seul livre à la fois
        for link in links:
            info_source = info_from_page(link)
            infos.append(info_source)

        # creation du fichier csv
        with open('product_info.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(info_id)
            for i in infos:
                writer.writerow(i)

if choix == '2':
    for cl in category_link:
        liens = category_page(url.removesuffix('catalogue/') + cl)
        #print(liens)
        nom_fichier = str(cl[25:].removesuffix('/index.html'))
        category_infos = []

        for lien in liens:
            by_category_info = info_from_page(lien)
            #print(by_category_info)
            category_infos.append(by_category_info)
            #print(category_infos)

        #with open(nom_fichier, 'w') as csvfile:
            #writer = csv.writer(csvfile)
            #writer.writerow(info_id)
            #for i in category_infos:
                #writer.writerow(i)

import csv
from page import Page
from category import category_link, category_page

url = 'http://books.toscrape.com/catalogue/'

# La list qui contient sortie’en-tête des infos scrapes
info_id = ['product_page_url', 'title', 'universal_ product_code (upc)',
           'price_including_tax', 'price_excluding_tax', 'number_available',
           'review_rating', 'product_description', 'category', 'image_url']

for cl in category_link:
    # récupérer tous les liens des livres de la category
    # liens est une liste qui contient, par page, tous les liens de la category
    liens = category_page(url.removesuffix('catalogue/') + cl, links=None)

    # nom_fichier est le nom que va prendre le fichier csv pour chaque category
    nom_fichier = str(cl[25:].removesuffix('/index.html')) + '.csv'
    category_infos = []  # va contenir les données de tous les livres d’une category

    # pour chaque page de la category
    for page in liens:
        # pour chaque livre de la page
        for lien in page:
            p = Page(lien)  # infos d’un seul livre
            by_category_info = [p.url, p.title, p.upc, p.price_including_tax,
                                p.price_excluding_tax, p.number_available, p.review_rating,
                                p.product_description, p.category, p.image_url]
            category_infos.append(by_category_info)

    # mettre les infos dans un fichier csv
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(info_id)
        for i in category_infos:
            writer.writerow(i)
    print('la category ', nom_fichier, ' est termine')

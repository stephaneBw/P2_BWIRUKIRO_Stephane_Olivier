import csv
from category import category_link, category_page
from page import info_from_page

# demander à l’utilisateur s’il veut consulter les données d’une seule catégorie
# ou s’il préfère avoir les fichiers sur toutes les categories
choix = 3
while True:
    try:
        choix = int(input('\nSi vous voulez seulement consulter une catégorie, entrez 1'
                          '\nsinon entrez 2 et vous aurez toutes les catégories'
                          '\nvotre choix: '))
    except ValueError:
        print('Vous n’avez pas entré un chiffre')
    if choix != 1 and choix != 2:
        print('Vous devez choisir un chiffre qui soit 1 ou 2')
    else:
        break
url = 'http://books.toscrape.com/catalogue/'

# La list qui contient l’en-tête des infos scrapes
info_id = ['product_page_url', 'title', 'universal_ product_code (upc)',
           'price_including_tax', 'price_excluding_tax', 'number_available',
           'review_rating', 'product_description', 'category', 'image_url']

if choix == 1:
    nom_category = []
    count = 0
    for cl in category_link:
        nom_category.append(cl[25:].removesuffix('/index.html'))
    print('voici la liste des category disponibles\n', nom_category)
    choix_category = input('entrez le nom de la category que vous voulez consulter: ')
    for c in nom_category:
        if choix_category == c:
            category_infos = []  # va contenir les données de tous les livres d’une category
            liens = category_page(url.removesuffix('catalogue/') + category_link[count])
            for lien in liens:
                for l in lien:
                    by_category_info = info_from_page(l)  # infos d’un seul livre
                    category_infos.append(by_category_info)
            # mettre les infos dans un fichier csv
            with open((c + '.csv'), 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(info_id)
                for i in category_infos:
                    writer.writerow(i)
        if count == 49:
            print('le mot entré ne correspond à aucune category de la liste')
        count += 1

if choix == 2:
    for cl in category_link:
        liens = category_page(url.removesuffix('catalogue/') + cl, links=None)
        # nom_fichier est le nom que va prendre le fichier csv pour chaque category
        nom_fichier = str(cl[25:].removesuffix('/index.html')) + '.csv'
        category_infos = []  # va contenir les données de tous les livres d’une category

        for lien in liens:
            for l in lien:
                by_category_info = info_from_page(l)  # infos d’un seul livre
                category_infos.append(by_category_info)

        # mettre les infos dans un fichier csv
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(info_id)
            for i in category_infos:
                writer.writerow(i)
        print('la category ', nom_fichier, ' est termine')

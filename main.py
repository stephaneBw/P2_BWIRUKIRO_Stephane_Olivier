import csv
import requests
from bs4 import BeautifulSoup
from page import info_from_page

page = 'page-' + input('Entrez le numero de la page que vous voulez consulter: ') + '.html'
url = 'http://books.toscrape.com/catalogue/'

response = requests.get(url+page)  # request
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_links = soup.findAll('h3')
    info_id = ['product_page_url', 'title', 'universal_ product_code (upc)', 'price_including_tax',
               'price_excluding_tax', 'number_available', 'review_rating', 'product_description', 'category', 'image_url']
    infos = []
    # print('\n' + str(len(tag_links)) + '\n')
    links = []
    # titles = []
    for tl in tag_links:
        a = tl.find('a')
        links.append(url + a['href'])
        # titles.append(a['title'])
    for link in links:
        info_source = info_from_page(link)
        infos.append(info_source)
    with open('product_info.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(info_id)
        for i in infos:
            writer.writerow(i)

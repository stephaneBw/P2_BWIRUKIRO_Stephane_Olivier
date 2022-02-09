import csv
import requests
from bs4 import BeautifulSoup


def info_from_page(page_url):
    """Function scrapes info on the page and write it in a csv file"""
    response = requests.get(page_url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_info = soup.findAll('tr')
        title = soup.find('h1')
        info = [page_url, title.text]
        info_id = ['product_page_url', 'title']
        for i in product_info:
            th = i.find('th')
            td = i.find('td')
            info_id.append(th.text)
            info.append(td.text)
        info_id.remove('Product Type')
        info_id.remove('Tax')
        info.remove('£0.00')
        info.remove('Books')
        print(info_id)
        print(info)
    """
        with open('product_info.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(info_id)
            writer.writerow(info)
    """


info_from_page('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

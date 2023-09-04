from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

def collect_data(url='https://rozetka.com.ua/ua/utsenennye-noutbuki/c83853/'):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    pages = int(soup.find('div', class_='pagination ng-star-inserted').find_all('li', class_='pagination__item ng-star-inserted')[-1].text.strip())
    print(f'[INFO] Total {pages} pages......')
    products = ()
    for page in range(1, pages + 1):
        print(f'[INFO] Scraping {page} page....')
        url = f'https://rozetka.com.ua/ua/utsenennye-noutbuki/c83853/page={page}]/'
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        items = soup.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
        for item in items:
            title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
            link = item.find('a', class_='goods-tile__heading ng-star-inserted').get('href').strip()
            status = item.find('div', class_='goods-tile__availability').text.strip()
            #defect = item.find('div', class_='goods-tile__hidden-holder').find('p', class_='goods-tile__description goods-tile__description_type_text ng-star-inserted')
            try:
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
            except:
                price = 'Something wrong...'
            products += ({
                'title': title,
                'link': link,
                'status': status,
                'price': price
            },)
    return products
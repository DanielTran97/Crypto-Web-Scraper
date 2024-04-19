import requests
import datetime
from bs4 import BeautifulSoup

# For Cryptocurrencies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# paste stock web url from Yahoo Finance
url = 'https://finance.yahoo.com/crypto/'

r = requests.get(url,headers= headers)

soup = BeautifulSoup(r.content, 'lxml')

# simpTblRow
crypto_scrape_data = []

for item in soup.select('.simpTblRow'):
    scrape_dict = {}
    scrape_dict['item_selector'] = item.select('[aria-label=Symbol]')[0].get_text()
    scrape_dict['name_selector'] = item.select('[aria-label=Name]')[0].get_text()
    scrape_dict['price_selector'] = item.select('[aria-label="Price (Intraday)"]')[0].get_text()
    scrape_dict['change_selector'] = item.select('[aria-label=Change]')[0].get_text()
    scrape_dict['changePercentage_selector'] = item.select('[aria-label="% Change"]')[0].get_text()
    scrape_dict['marketCap_selector'] = item.select('[aria-label="Market Cap"]')[0].get_text()
    scrape_dict['Vol_InCurrencyUTC_selector'] = item.select('[aria-label="Volume in Currency (Since 0:00 UTC)"]')[0].get_text()
    scrape_dict['Vol_InCurrencyHour_selector'] = item.select('[aria-label="Volume in Currency (24Hr)"]')[0].get_text()
    scrape_dict['TotalVol_InCurrencyHour_selector'] = item.select('[aria-label="Total Volume All Currencies (24Hr)"]')[0].get_text()
    scrape_dict['Circul_Supply_selector'] = item.select('[aria-label="Circulating Supply"]')[0].get_text()
    scrape_dict['DateTime'] = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    crypto_scrape_data.append(scrape_dict)

# for data in crypto_scrape_data:
#     print(data)

#     print()
#     print('-----------Divider----------')
#     print()













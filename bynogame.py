import requests
import urllib.parse
# from bs4 import BeautifulSoup
from lxml import etree, html
import time
import re
import pandas as pd 
from forex_python.converter import CurrencyRates


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

# df = pd.DataFrame(index=[0,1,2], columns=["Market", "Weapon | Skin (Condition)", "float", "Price", "Native", "Discount"])



url = 'https://www.bynogame.com/tr/search?'
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers = {'user-agent': usr_agent}

usr_inp = 'survival fade ' # input('Search skin: ')
data = {'query': usr_inp}
encoded = urllib.parse.urlencode(query=data)
print(url + encoded)

r = requests.get(url + encoded, headers=headers)
# print(r.content)

doc = html.fromstring(r.content)
tree = etree.ElementTree(doc)

name = tree.xpath('//div[@class="col d-flex flex-column justify-content-center"]/span[@class="font-weight-bolder my-0"]/text()')[0]
print(name)

price = tree.xpath('//h5[@class="font-weight-bolder mb-0 ml-2"]/text()')[0]
# print(price)

url2 = tree.xpath('//small[@class="break-word text-muted"]/text()')[0]
print(url2)

time.sleep(0.5)
# inside the first item
r2 = requests.get("https://www." + url2, headers=headers)

doc2 = html.fromstring(r2.content)
tree = etree.ElementTree(doc2)

float_ = tree.xpath('//td[@class="text-center text-nowrap v-middle"]/text()')
# print(float_)

float_ = remove_values_from_list(float_, '\n')
print(float_[0].replace('\n', ""))

price2 = tree.xpath('//button[@class="btn btn-primary btn-sm game-item-list-purchase-buttons"]/text()')
# print(price2)

price2 = remove_values_from_list(price2, '\n')
price_in_a_lst = re.findall("\d+\.\d+", price2[0])
print(price_in_a_lst[0])



# c.get_rate('USD', 'TRY')


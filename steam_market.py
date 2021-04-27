import requests
import urllib.parse
from lxml import etree, html
import json
from forex_python.converter import CurrencyRates

import lookups

def search_at_steam(currency):
    url = "https://steamcommunity.com/market/search?"
    usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    headers = {'user-agent': usr_agent}

    # Pull the user input
    with open('./data/search_query.txt', 'r') as f:
            usr_inp = f.read()

    steamMarket = lookups.SteamMarket() 
    # Determine if `Stattrak` or `Souvenir` or neither
    usr_inp, tag, tag_2 = steamMarket.category(usr_inp)

    # Setting weapon exterior (condition, wear)
    usr_inp, weapon_exterior = steamMarket.exterior(usr_inp)

    # Search for weapon
    usr_inp, weapon = lookups.we_name(usr_inp)
    weapon_2 = steamMarket.weapon(weapon)

    # Search for skin
    skin = lookups.we_skin(usr_inp)

    data = [ ('q', skin),
            ('category_730_Weapon[]', weapon_2),
            ('category_730_Exterior[]', weapon_exterior),
            ('category_730_Quality[]', tag),
            ('category_730_Quality[]', tag_2),
            ('appid','730') 
    ]
    encoded = urllib.parse.urlencode(query=data)
    # print(url + encoded)
    r = requests.get(url + encoded, headers=headers)

    doc = html.fromstring(r.content)
    tree = etree.ElementTree(doc)

    href_of_item = tree.xpath('//*[@id="resultlink_0"]')
    href_of_item_0 = href_of_item[0].get("href")

    market_name = href_of_item_0[47:]

    #ak47, usps, m4, awp, deagle, ump

    # Now, GET json data
    url2 = "https://steamcommunity.com/market/priceoverview/?"
    data2 = { 'appid':'730',
            'market_hash_name': urllib.parse.unquote(market_name),
            'currency':'1' 
    }
    encoded2 = urllib.parse.urlencode(query=data2)
    # print(url2 + encoded2)
    r2 = requests.get(url2 + encoded2, headers=headers)
    # print(r2.content)

    loaded_json = json.loads(r2.content)
    price = loaded_json['lowest_price']
    # print(price)
    price = float(price[1:])
    c = CurrencyRates()
    usd_to_cur = c.get_rate('USD', currency)
    price = round(price * usd_to_cur, 2)
    sell_now_price = round(price / 1.15, 2)

    # print(['Steam market', weapon, skin, weapon_exterior, 0, price, sell_now_price])
    return ['Steam market', weapon, skin, weapon_exterior, 0, price, sell_now_price, url+encoded]
            



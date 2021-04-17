import requests, urllib.parse
from lxml import etree, html
import json
import ast

import lookups

def search_at_bitskins():

    url = "https://bitskins.com/?"
    usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    headers = {'user-agent': usr_agent}

    # Pull the user input
    with open('./data/search_query.txt', 'r') as f:
        usr_inp = f.read()

    bitskins = lookups.Bitskins()
    # Determine if `Stattrak` or `Souvenir` or neither
    usr_inp, is_no, is_st, is_so = bitskins.category(usr_inp)

    # Setting weapon exterior (condition, wear)
    usr_inp, weapon_exterior = bitskins.exterior(usr_inp)

    # Search for weapon
    usr_inp, weapon = lookups.we_name(usr_inp)

    # Search for skin
    skin = lookups.we_skin(usr_inp)

    data = { 'market_hash_name': skin,
            'advanced': '1',
            'appid':'730',
            'item_wear': weapon_exterior,
            'is_stattrak': is_st,
            'is_souvenir': is_so,
            'item_weapon': weapon,
            'sort_by': 'price',
            'order': 'asc'
    }

    encoded = urllib.parse.urlencode(query=data)
    # print(url + encoded)

    r = requests.get(url + encoded, headers=headers)
    # print(r.content)

    doc = html.fromstring(r.content)
    tree = etree.ElementTree(doc)

    price = tree.xpath('//span[@class="item-price-display"]')
    price = price[0].text_content()
    price = float(price[1:])
    sell_now_price = round(price * 0.95,2)

    # print(["BitSkins", weapon, skin, weapon_exterior, 0, price, sell_now_price])
    return ["BitSkins", weapon, skin, weapon_exterior, 0, price, sell_now_price]


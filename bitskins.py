import requests
import urllib.parse
from lxml import etree, html
import json
from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs, normalized_damerau_levenshtein_distance_seqs

url = "https://bitskins.com/?"
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers = {'user-agent': usr_agent}

#
usr_inp = 'st awp asiimov ww' # input('Search skin: ')
#

if usr_inp[:2] == "st":
    is_st = '1'
    usr_inp = usr_inp[3:]
else:
    is_st = '-1'

if usr_inp[:2] == "so":
    is_so = '1'
    usr_inp = usr_inp[3:]
else:
    is_so = '-1'


"""Setting weapon exterior (condition, wear)"""
weapon_exterior = 'any'

we_exteriors = {
    'fn': 'Factory+New',
    'mw': 'Minimal+Wear',
    'ft': 'Field-Tested',
    'ww': 'Well-Worn',
    'bs': 'Battle-Scarred'
}

weapon_exterior = we_exteriors[usr_inp[-2:]]

# remove the wear from the input string
usr_inp = usr_inp[:-3]


splitted_usr_inp = usr_inp.split(' ')
"""Weapons"""
weapon = ''
weapons = ['Knife', 'Bayonet', 'Flip Knife', 'Gut Knife', 'Karambit', 'M9 Bayonet', 'Huntsman Knife', 'Butterfly Knife', 'Falchion Knife', 'Shadow Daggers', 'Bowie Knife', 'Ursus Knife', 'Navaja Knife', 'Stiletto Knife', 'Talon Knife', 'Classic Knife', 'Paracord Knife', 'Survival Knife', 'Skeleton Knife', 'Nomad Knife', 'CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8 Revolver', 'Tec-9', 'USP-S', 'MAG-7', 'Nova', 'Sawed-Off', 'XM1014', 'M249', 'Negev', 'MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45', 'AK-47', 'AUG', 'FAMAS', 'Galil AR', 'M4A1-S', 'M4A4', 'SG 553', 'AWP', 'G3SG1', 'SCAR-20', 'SSG 08']
ds = normalized_damerau_levenshtein_distance_seqs(splitted_usr_inp[0], map(str.lower, weapons))
min_d = min(ds)
index_of_min = ds.index(min_d)
weapon = weapons[index_of_min]



data = { 'market_hash_name': usr_inp,
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
print(url + encoded)


"""
r = requests.get(url + encoded, headers=headers)
# print(r.content)

doc = html.fromstring(r.content)
tree = etree.ElementTree(doc)

href_of_item = tree.xpath('//*[@id="resultlink_0"]')
href_of_item_0 = href_of_item[0].get("href")

market_name = href_of_item_0[47:]


# Now, GET json data
url2 = "https://steamcommunity.com/market/priceoverview/?"
data2 = { 'appid':'730',
          'market_hash_name': urllib.parse.unquote(market_name),
          'currency':'1' 
}
encoded2 = urllib.parse.urlencode(query=data2)
print(url2 + encoded2)
r2 = requests.get(url2 + encoded2, headers=headers)
print(r2.content)

loaded_json = json.loads(r2.content)
price = loaded_json['lowest_price']
print(price)
"""


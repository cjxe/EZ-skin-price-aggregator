import requests
import urllib.parse
from lxml import etree, html
import json


url = "https://steamcommunity.com/market/search?"
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
headers = {'user-agent': usr_agent}

#
usr_inp = 'awp asiimov ft' # input('Search skin: ')
#

if usr_inp[:2] == "st":
    tag = 'tag_strange'
    usr_inp = usr_inp[3:]
else:
    tag = 'tag_normal'

"""Weapons"""
weapon = 'any'

if weapon == "cz" or "cz75" or "cz75-auto" or "cz75 auto":
    pass

we = {
    "knives": [{
        "bayonet": ["bayonet"],
        "flip knife": ["flip knife", "flip-knife", "flip"],
        "gut knife": ["gut knife", "gut-knife", "gut"],
        "karambit": ["karambit"],
        "m9 bayonet": ["m9 bayonet", "m9-bayonet", "m9"],
        "huntsman knife": ["huntsman knife", "huntsman-knife", "huntsman"],
        "butterfly knife": ["butterfly knife", "butterfly-knife", "butterfly"],
        "falchion knife": ["falchion knife", "falchion-knife", "falchion"],
        "shadow daggers": ["shadow daggers", "shadow-daggers", "shadow", "daggers"],
        "bowie knife": ["bowie knife", "bowie-knife", "bowie"],
        "ursus knife": ["ursus knife", "ursus-knife", "ursus"],
        "navaja knife": ["navaja knife", "navaja-knife", "navaja"],
        "stiletto knife": ["stiletto knife", "stiletto-knife", "stiletto"],
        "talon knife": ["talon knife", "talon-knife", "talon"],
        "classic knife": ["classic knife", "classic-knife", "classic"],
        "paracord knife": ["paracord knife", "paracord-knife", "paracord"],
        "survival knife": ["survival knife", "survival-knife", "survival"],
        "skeleton knife": ["skeleton knife", "skeleton-knife", "skeleton"],
        "nomad knife": ["nomad knife", "nomad-knife", "nomad"]
    }],
        
    "pistols": [{
        "cz75-auto": ["cz75-auto", "cz", "cz75", "cz75 auto"],
        "desert eagle": ["desert eagle", "desert", "eagle", "desert-eagle"],
        "dual berettas": ["dual berettas", "dual", "berettas", "dual-berettas"],
        "five-seven": ["five-seven", "five seven", "five", "seven"],
        "glock-18": ["glock-18", "glock 18", "glock"],
        "p2000": ["p2000", "p 2000"],
        "p250": ["p250", "p 250"],
        "r8 revolver": ["r8 revolver", "r8-revolver", "r8", "revolver"],
        "tec-9": ["tec-9", "tec 9", "tec9"],
        "usp-s": ["usp-s", "usp s", "usp"],
    }],

    "shotguns": [{
        "mag-7": ["mag-7", "mag 7", "mag7"],
        "nova": ["nova"],
        "sawed-off": ["sawed-off", "sawed off", "sawed", "off"],
        "xm1014": ["xm1014", "xm-1014", "xm 1014", "xm"],
    }],

    "machine guns": [{
        "m249": ["m249", "m-249", "m 249"],
        "negev": ["negev"]
    }],

    "smgs": [{
        "mac-10": ["mac-10", "mac 10", "mac10"],
        "mp5-sd": ["mp5-sd", "mp5 sd", "mp5"],
        "mp7": ["mp7", "mp-7", "mp 7"],
        "mp9": ["mp9", "mp-9", "mp 9"],
        "p90": ["p90", "p-90", "p 90", "pro90"],
        "pp-bizon": ["pp-bizon", "ppbizon", "bizon"],
        "ump-45": ["ump-45", "ump 45", "ump45"]
    }],
    
    "assault rifles": [{
        "ak-47": ["ak-47", "ak 47", "ak47"],
        "aug": ["aug"],
        "famas": ["famas"],
        "galil ar": ["galil ar", "galil-ar", "galil"],
        "m4a1-s": ["m4a1-s", "m4a1 s", "m4a1", "m4a1s"],
        "m4a4": ["m4a4"],
        "sg 553": ["sg 553", "sg-553", "sg553"]
    }],

    "sniper rifles": [{
        "awp": ["awp"],
        "g3sg1": ["g3sg1"],
        "scar-20": ["scar-20", "scar 20", "scar20"],
        "ssg 08": ["ssg 08", "ssg-08", "ssg08"]
    }]
}
    





"""Setting weapon exterior (condition, wear)"""
weapon_exterior = 'any'

if ('fn') in usr_inp:
    weapon_exterior = 'tag_WearCategory0'

elif ('mw') in usr_inp:
    weapon_exterior = 'tag_WearCategory1'

elif ('ft') in usr_inp:
    weapon_exterior = 'tag_WearCategory2'

elif ('ww') in usr_inp:
    weapon_exterior = 'tag_WearCategory3'

elif ('bs') in usr_inp:
    weapon_exterior = 'tag_WearCategory4'


# remove the wear from the input string
usr_inp = usr_inp[:-3]

data = { 'q': usr_inp, 
         'category_730_Exterior[]': weapon_exterior,
         'category_730_Quality[]': tag,
         'appid':'730' 
}
encoded = urllib.parse.urlencode(query=data)
print(url + encoded)
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



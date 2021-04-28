from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import urllib.parse
from lxml import etree, html
import time
from forex_python.converter import CurrencyRates

import lookups

def search_at_bynogame(currency):
    url = 'https://www.bynogame.com/tr/oyunlar/csgo/skin?'
    # usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

    # Pull the user input
    with open('./data/search_query.txt', 'r') as f:
        usr_inp = f.read()

    bynogame = lookups.Bynogame()
    # Determine if `Stattrak` or `Souvenir` or neither
    usr_inp, cat_1, cat_2 = lookups.we_category(usr_inp)
    category = bynogame.category(cat_1, cat_2)

    # Setting weapon exterior (condition, wear)
    usr_inp, weapon_exterior = bynogame.exterior(usr_inp)

    # Search for weapon
    usr_inp, weapon = lookups.we_name(usr_inp)

    # Search for skin
    skin = lookups.we_skin(usr_inp, weapon)

    data = {"kw": skin,
            "st": category,
            "ext": weapon_exterior,
            "hb": weapon,
            "srt": "pa"
    }

    encoded = urllib.parse.urlencode(query=data)
    url = url + encoded

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # remove the "#" at the start of the line to launch Chrome in "headless" mode.
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    with open("./data/cached/chrome/chrome_path.txt", "r") as f:
        chrome_driver_path = f.read()
    driver = webdriver.Chrome(executable_path=chrome_driver_path , options=chrome_options)

    driver.get(url)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f'//div[@class="itemCard__info border-bottom-0 text-left"]/h1'))) # wait max of 10sec until the element is loaded

    title = driver.find_element_by_xpath('//div[@class="itemCard__info border-bottom-0 text-left"]/h1').text
    price = driver.find_element_by_xpath('//small[@class="text-bng-grey"]').text

    price = float(price[:-3])
    c = CurrencyRates()
    try_to_cur = c.get_rate("TRY", currency)
    price = round(price * try_to_cur, 2)
    sell_now_price = round(price * 0.925, 2)  # commision rate of bynogame ???

    return ["ByNoGame", title, 0, 0, 0, price, sell_now_price, url+encoded]
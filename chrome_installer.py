from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager(path="./data/cached/chrome").install()
chrome_driver_path = chrome_driver_path.replace('\\','/')

with open("./data/cached/chrome/chrome_path.txt", "w", encoding="utf-8") as f:
    f.write(chrome_driver_path)
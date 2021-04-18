import pandas as pd
import json
import bitskins, steam_market

with open('./data/settings.json') as settings_file:
    config = json.load(settings_file)

print(f"""⚙️  Welcome the 'EZ_PRICE_AGGREATOR'. Check out `./data/settings.json` to configure the settings.""")

usr_inp = input('🔍 Search skin: ')

with open('./data/search_query.txt','w', encoding='utf-8') as f:
    f.write(usr_inp)

df = pd.DataFrame(columns=['market', 'weapon', 'skin', 'wear', 'float', f'buy ({config["currency"]})', 'sell', 'url'])  # only: market, buy, sell, url(?)
df.to_csv('./data/search_result.csv', mode='w', index=False)

print(f'⏳ Searching...')  # searching for  category + weapon + skin + wear
row_1 = steam_market.search_at_steam(search=config['search_at_steam'], currency=config['currency'])  # fix these
new_row = pd.DataFrame([row_1])
new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)

row_2 = bitskins.search_at_bitskins(search=config['search_at_bitskins'], currency=config['currency'])
new_row = pd.DataFrame([row_2])
new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)
print(f'✅ Search done. Check out `./data/search_result.csv` for more info.\n')

df = pd.read_csv('./data/search_result.csv')  # debug
print(df)  # debug



"""
# discount en pahali vs en ucuz site olsun
"""
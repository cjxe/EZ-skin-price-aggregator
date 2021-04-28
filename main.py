import pandas as pd
import json
import bitskins, steam_market, bynogame

with open('./data/settings.json') as settings_file:
    config = json.load(settings_file)

# save the last time data_scraper was run, check if its older than 1 day, if it is run and update the new date

print(f"""⚙️  Welcome the 'EZ_PRICE_AGGREATOR'. Check out `./data/settings.json` to configure the settings.""")

usr_inp = input('🔍 Search skin: ')

with open('./data/search_query.txt','w', encoding='utf-8') as f:
    f.write(usr_inp)

df = pd.DataFrame(columns=['market', 'weapon', 'skin', 'wear', 'float', f'buy ({config["currency"]})', 'sell', 'url'])  # only: market, buy, sell, url(?)
df.to_csv('./data/search_result.csv', mode='w', index=False)

print(f'⏳ Searching...')  # searching for  category + weapon + skin + wear

if config['search_at_steam']:
    row = steam_market.search_at_steam(currency=config['currency'])
    new_row = pd.DataFrame([row])
    new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)
else:
    print(f'⏩ Skipped searching at Steam community market.')

if config['search_at_bitskins']:
    row = bitskins.search_at_bitskins(currency=config['currency'])
    new_row = pd.DataFrame([row])
    new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)
else:
    print(f'⏩ Skipped searching at BitSkins.')

if config['search_at_bynogame']:
    row = bynogame.search_at_bynogame(currency=config['currency'])
    new_row = pd.DataFrame([row])
    new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)
else:
    print(f'⏩ Skipped searching at ByNoGame.')

print(f'✅ Search done. Check out `./data/search_result.csv` for more info.\n')

df = pd.read_csv('./data/search_result.csv')  # debug
print(df)  # debug

print('\n')

"""
# discount en pahali vs en ucuz site olsun
"""
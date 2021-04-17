import pandas as pd
import bitskins, steam_market

usr_inp = input('Search skin: ')

with open('./data/search_query.txt','w') as f:
    f.write(usr_inp)

df = pd.DataFrame(columns=['market', 'weapon', 'skin', 'wear', 'float', 'buy', 'sell'])
df.to_csv('./data/search_result.csv', mode='w', index=False)


row_1 = steam_market.search_at_steam()  # fix these
new_row = pd.DataFrame([row_1])
new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)

row_2 = bitskins.search_at_bitskins()
new_row = pd.DataFrame([row_2])
new_row.to_csv('./data/search_result.csv', index=False, mode='a', header=False)


df = pd.read_csv('./data/search_result.csv')  # debug
print(df)  # debug



"""
search_q = 'awp asiimof ft'

filename = 'search_result.csv'
df = pd.DataFrame(columns=["Market", "Weapon | Skin (Condition)", "Float", "Price", "Native", "Discount"])
# print(df)

# print('##########################################################################################')
dfa = pd.DataFrame([["Steam", "AWP | Asiimov (Field-Tested)", "0.2243", "$81.00", "$81.00", "0%"]],
                     columns=["Market", "Weapon | Skin (Condition)", "Float", "Price", "Native", "Discount"])
df = df.append(dfa, ignore_index=True)
# print(df)

# print('##########################################################################################')
dfa = pd.DataFrame([["Bynogame", "AWP | Asiimov (Field-Tested)", "0.2687", "$69.61", "₺580.00", "25%"]],
                     columns=["Market", "Weapon | Skin (Condition)", "Float", "Price", "Native", "Discount"])
df = df.append(dfa, ignore_index=True)
print(df)


# Native'i sil
# Satin al vs Sat   ekle, sat'ta komisyon dahil olsun
# discount en pahali vs en ucuz site olsun
"""
import pandas as pd
import collections, json

df = pd.read_csv('./data/cached/weapon_n_skin.csv')
dic_w_and_s = collections.defaultdict(list)

grouped = df.groupby(['weapon', 'skin']).groups

for key, value in grouped.items():
    dic_w_and_s[key[0]].append(key[1])

with open('./data/cached/weapons_and_skins.json', 'w', encoding='utf-8') as f:
    json.dump(dic_w_and_s, f, ensure_ascii=False, indent=4)
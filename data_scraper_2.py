import pandas as pd
import requests

DOWNLOAD_ROOT = "https://loot.farm"
CSGO_URL = DOWNLOAD_ROOT + "/fullprice.csv"
df_fullprice = pd.read_csv(CSGO_URL)

df_we = pd.DataFrame(columns=['weapon', 'skin'])
full_names = df_fullprice.index

# import this from ./data/cached/
weapons = ['Knife', 'Bayonet', 'Flip Knife', 'Gut Knife', 'Karambit', 'M9 Bayonet', 'Huntsman Knife', 'Butterfly Knife', 'Falchion Knife', 'Shadow Daggers', 'Bowie Knife', 'Ursus Knife', 'Navaja Knife', 'Stiletto Knife', 'Talon Knife', 'Classic Knife', 'Paracord Knife', 'Survival Knife', 'Skeleton Knife', 'Nomad Knife', 'CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8 Revolver', 'Tec-9', 'USP-S', 'MAG-7', 'Nova', 'Sawed-Off', 'XM1014', 'M249', 'Negev', 'MAC-10', 'MP5-SD', 'MP7', 'MP9', 'P90', 'PP-Bizon', 'UMP-45', 'AK-47', 'AUG', 'FAMAS', 'Galil AR', 'M4A1-S', 'M4A4', 'SG 553', 'AWP', 'G3SG1', 'SCAR-20', 'SSG 08']

all_skins = []

for w in full_names:
    for w2 in weapons:
        if w2.lower() in w.lower():
            all_skins.append(w)

# removing conditions (wear)
all_skins_clean = []

for skin in all_skins:
    if '(' in skin:
        indices = [i for i, c in enumerate(skin) if c == '(']
        all_skins_clean.append(skin[:(max(indices)-1)])
    else:
        all_skins_clean.append(skin)  # skins without condition, vanilla (not painted)
all_skins_clean_v2 = list(set(all_skins_clean))  # removing duplicates


# removing stars, stattraks, souvenir etc.
all_skins_clean_v3 = []

for skin in all_skins_clean_v2:
    skin = skin.replace("Souvenir ", '')
    skin = skin.replace("★ ", '')
    skin = skin.replace("StatTrak™ ", '')
    
    all_skins_clean_v3.append(skin)

all_skins_clean_v3 = list(set(all_skins_clean_v3))


all_skins_clean_v4 = []

for w in all_skins_clean_v3:
    if '|' in w:
        weapon = w[:(w.index('|'))-1]  # "R8 Revolver | Fade" => "R8 Revolver"
        skin = w[(w.index('|'))+2:]  # "R8 Revolver | Fade" => "Fade"
        dict1 = {'weapon':weapon, 'skin':skin}
    else:
        dict1 = {'weapon':w}
    all_skins_clean_v4.append(dict1)

df_we = pd.DataFrame(all_skins_clean_v4, columns=["weapon", "skin"])
drop_values = list(set(df_we['weapon'].unique()) - set(weapons))
df_we = df_we[~df_we['weapon'].isin(drop_values)]
df_we = df_we.fillna({"skin":"(Vanilla)"})
df_we.to_csv('./data/cached/weapon_n_skin.csv', index=False)

"""
dataset = './data/weapon_data.csv'

# Load the `.csv` data if exists
try:
    df = pd.read_csv(dataset)
    print(f'✅ Dataset "{dataset}" found.')  # debug
# if not, create one.
except FileNotFoundError:
    print(f'⏳ Dataset "{dataset}" does not exist! Creating a new one...')  # debug
    df = pd.DataFrame(columns=['collection', 'weapon', 'skin', 'quality', 'drop'])
    df.to_csv(dataset, mode='w', index=False)

# Send a get request to the data.
r = requests.get('https://counterstrike.fandom.com/wiki/Skins/List')
soup = BeautifulSoup(r.content, "lxml")

# Pull the data.
print(f'📥 Downloading the data...')  # debug
rows = []
for tr_tag in soup.find_all('tr'):
    td_tags = tr_tag.find_all('td')
    
    row = []
    for tr_tag in td_tags:
        row.append(tr_tag.getText())

    rows.append(row)
print(f'✅ Finished downloading.')  # debug

# Clean the data by stripping `\n`s.
print(f'🧹 Cleaning the data...')  # debug
rows_2 = []
for row in rows:
    row_2 = []
    for word in row:
        row_2.append(word.rstrip('\n*'))
    rows_2.append(row_2)
print(f'✅ Finished cleaning.')  # debug

# Export the data to the `.csv` file.
print(f'📤 Exporting data...')  # debug
df_e = pd.DataFrame(rows_2[1:])
df_e.dropna(axis=0, how='all', inplace=True)
df_e.to_csv(dataset, index=False, mode='a', header=False)
print(f'✅ Finished exporting...')  # debug

print(f'😴 Program successfully finished. Terminating...')  # debug
"""
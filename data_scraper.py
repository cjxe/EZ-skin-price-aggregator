import pandas as pd
import requests
from bs4 import BeautifulSoup

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
        row_2.append(word.rstrip('\n'))
    rows_2.append(row_2)
print(f'✅ Finished cleaning.')  # debug

# Export the data to the `.csv` file.
print(f'📤 Exporting data...')  # debug
df_e = pd.DataFrame(rows_2[1:])
df_e.to_csv(dataset, index=False, mode='a', header=False)
print(f'✅ Finished exporting...')  # debug

print(f'😴 Program successfully finished. Terminating...')  # debug

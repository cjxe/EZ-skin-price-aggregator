import pandas as pd

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
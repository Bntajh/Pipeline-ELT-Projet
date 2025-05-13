import pandas as pd

# Charger et lire le fichier csv
df = pd.read_csv('/Users/bintadiallo/PycharmProjects/Data_projet/Oct2019/2019_Oct.csv')

# Séparer les catégories
split_df = df['category_code'].str.split('.', expand = True)

df['categorie_1'] = split_df[0] if 0 in split_df.columns else None
df['categorie_2'] = split_df[1] if 1 in split_df.columns else None
df['categorie_3'] = split_df[2] if 2 in split_df.columns else None
df['categorie_4'] = split_df[3] if 3 in split_df.columns else None

print(df.head())




import pandas as pd
import requests
input_file = "C:/Users/19695/Downloads/new_table.csv"
output_file = 'C:/Users/19695/Downloads/new_table2.csv'
df = pd.read_csv(input_file)
def convert_to_smiles(name):
    url = f"https://cactus.nci.nih.gov/chemical/structure/{name}/smiles"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return ''

df['smiles'] = df['Name'].apply(convert_to_smiles)
df.to_csv(output_file, index=False)

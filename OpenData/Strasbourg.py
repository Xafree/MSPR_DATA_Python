import requests
import os

from dotenv import load_dotenv

load_dotenv()

openData = os.getenv('STRASBOURG')

response_strasbourg = requests.get(openData)
open_data_strasbourg = response_strasbourg.json()

data_strasbourg = []

for i in range(len(open_data_strasbourg['records'])):
    data_set = {
        "ville": "Strasbourg",
        "nom": open_data_strasbourg['records'][i]['fields']['nom_parking'],
        "date": open_data_strasbourg['records'][i]['record_timestamp'],
        "place_libres": open_data_strasbourg['records'][i]['fields']['libre'],
        "places_totales": open_data_strasbourg['records'][i]['fields']['total']
    }

    data_strasbourg.append(data_set)

print(data_strasbourg)
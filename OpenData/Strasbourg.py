import requests
import os

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def getURLOpenDataStrasbourg():
    return os.getenv('STRASBOURG')


def getJsonOpenData():
    response_strasbourg = requests.get(os.getenv('STRASBOURG'))
    open_data_strasbourg = response_strasbourg.json()
    return open_data_strasbourg


def DataListeOfCarsParkAboutStrasbourg(dataJson):
    data_strasbourg = []
    for i in range(len(dataJson['records'])):
        data_set = {
            "ville": "Strasbourg",
            "nom": dataJson['records'][i]['fields']['nom_parking'],
            "date": datetime.strptime(dataJson['records'][i]['record_timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'),
            #"date": dataJson['records'][i]['record_timestamp'],
            "place_libres": dataJson['records'][i]['fields']['libre'],
            "places_totales": dataJson['records'][i]['fields']['total']
        }
        data_strasbourg.append(data_set)
    return data_strasbourg


def getDataAboutCarsParkStrasbourg():
    return DataListeOfCarsParkAboutStrasbourg(getJsonOpenData())

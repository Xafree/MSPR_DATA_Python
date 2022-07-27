from datetime import datetime
from re import search

import requests
import json
import os

from dotenv import load_dotenv
from xml.etree import ElementTree

load_dotenv()


def getURLOpenDataMontpellier():
    return os.getenv('MONTPELLIER')


def getjsonOpenData():
    # On récupère les données de L'api de OpenData de Montpellier
    response = requests.get(os.getenv('MONTPELLIER'))

    # print(response.json())
    OpenDataMontpellier = response.json()
    return OpenDataMontpellier

def  switchNameOpenData(name):
    dictionaryOfParkingsName = {
        'ANTI': "Antigone",
        'ARCT': "Arc de Triomphe",
        'COME': "THEATRE COMEDIE",
        'CORU': "Corum",
        'EURO': "Europa",
        'FOCH': "Foch Préfecture",
        'GAMB': "Gambetta",
        'GARE': "Saint Roch",
        'Triangle': "Triangle",
        'Pitot': "PITOT",
        'CIRCE': "Circé Odysseum",
        'SABI': "Sabines",
        'GARD': "Garcia Lorca",
        'SABL': "Notre Dame de Sablassou",
        'MOSS': "Mosson",
        'SJLC': "Saint Jean Le Sec", #Not match
        'MEDC': "Euromédecine ",
        'OCCI': "Occitanie",
        'VICA': "Vicarello", #Not match
        'GAUMONT-EST': "Gaumont EST", #Not match
        'GAUMONT-OUEST': "Gaumont OUEST", #Not match
        'CDGA': "Charles de Gaulle",
        'ARCE': "Arceaux",
        'POLY': "Polygone",
    }
    return dictionaryOfParkingsName.get(name)

def extractFormatJson(JsonOpenDataMontpellier):
    # On parcoure les données de l'API
    urlList = []

    # On parcour les donnée de l'api
    for i in range(len(JsonOpenDataMontpellier['result']['resources'])):
        urlList.append(JsonOpenDataMontpellier['result']['resources'][i]['url'])

    data_montpellier = []

    for i in range(2, len(urlList)):
        res_xml = requests.get(urlList[i])
        if res_xml.content.decode("utf-8") != "":
            root = ElementTree.fromstring(res_xml.content)
            name = switchNameOpenData(root.findtext("Name"))
            data_set = {
                "ville": "Montpellier",
                "nom": name,
                "date": datetime.strptime(root.findtext("DateTime")[0:19], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S'),
                "place_libres": int(root.findtext("Free")),
                "places_totales": int(root.findtext("Total"))
            }
        #data_to_json = json.dumps(data_set)
        data_montpellier.append(data_set)
    return data_montpellier


def getDataAboutCarsParkMontepllier():
    return extractFormatJson(getjsonOpenData())

import requests
import json
import os

from dotenv import load_dotenv
from xml.etree import ElementTree

load_dotenv()


def getURLOpenDataMontpellier():
    return os.getenv('MONTPELLIER')


def getjsonOpenData(Url):
    # On récupère les données de L'api de OpenData de Montpellier
    response = requests.get(Url)

    # print(response.json())
    OpenDataMontpellier = response.json()
    return OpenDataMontpellier


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
            data_set = {
                "ville": "Montpellier",
                "nom": root.findtext("Name"),
                "date": root.findtext("DateTime"),
                "place_libres": root.findtext("Free"),
                "places_totales": root.findtext("Total")
            }
        data_to_json = json.dumps(data_set)
        data_montpellier.append(data_to_json)
    return data_montpellier


def getDataAboutCarsParkMontepllier():
    return extractFormatJson(getjsonOpenData(getURLOpenDataMontpellier))

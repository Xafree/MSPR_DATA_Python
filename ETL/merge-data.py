
#Faire un merge des open data et des data gouv de manière a récupérer le prix longitude et l'atitude
#Data utile dans le gouv = tarif 1h, longitude, lattitude, Adresse? .
#Open data = Nb_place disponible, nb place totale, nom du parking, la ville
#Api_jour férier = récupération des jours férier, jour de l'année (Day of the week énum de lundi à dimanche). peut être les vacances si on a le time frrrrrrr
import pandas as pd

import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
import OpenData.Datagouv as gouv
from dataBase.Connect import Connect
from dataBase.Request import Request

dataTest = {
    "updated_place": '2022-07-07 19:07:30',
    "update_parking": '2022-07-18 19:07:30',
    "nom": 'Parking test',
    "num_siret": 8658975654,
    "ville": "Montpllier",
    "prix": 0.0,
    "longitude": 1540.15,
    "latitude": 4500.152,
    "nb_place_totale": 12000,
    "nb_place_disponible": 900,
    "estgratuit": 0,
}
OpenData_set = {
    "ville": "Strasbourg",
    "nom": "",
    "date": "",
    "place_libres": "",
    "places_totales": ""
}


DataGouv_set ={
    "nom":"",
    "prix": "",
    "longitude":"",
    "latitude": "",
}

FinalData_set ={
    "ville": "",
    "nom": "",
    "date": "",
    "place_libres": "",
    "places_totales": "",
    "prix": "",
    "longitude": "",
    "latitude": "",
}


dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()
datagouv = gouv.getDataAboutCarsParkDataGouv()

dataFrame = pd.DataFrame.from_records(dataMontpellier + dataStrasbourg)

print(dataFrame[22:47].head())
#print(datagouv.head())
finalArray= []
print(dataFrame.iloc[[1]].nom[1])
print(datagouv.iloc[[1]].nom[1])
for i in range(len(dataFrame)):
    for y in range(len(datagouv)):
        if dataFrame.iloc[[i]].nom[1] in datagouv.iloc[[y]].nom[1]:
            FinalData_set = {
                "ville": dataFrame[i]['ville'],
                "nom": datagouv[y]['nom'],
                "date": dataFrame[i]['date'],
                "place_libres": dataFrame[i]['place_libres'],
                "places_totales": dataFrame[i]['places_totales'],
                "prix": datagouv[y]['prix'],
                "longitude": datagouv[y]['longitude'],
                "latitude": datagouv[y]['latitude'],
            }
        finalArray.append(FinalData_set)
print(finalArray)
#finalDataFrame = pd.DataFrame(finalArray)

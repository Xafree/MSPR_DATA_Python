import pandas as pd

import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
import OpenData.Datagouv as gouv
from DateUtilities import DataUtilies

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

DataGouv_set = {
    "nom": "",
    "prix": "",
    "longitude": "",
    "latitude": "",
}

FinalData_set = {
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

print(dataFrame.head())
# print(datagouv.head())
finalArray = []
# print(dataFrame.iloc[[2]].nom[2])
# print(datagouv.iloc[[1]].nom[1])
dateDetails = DataUtilies()
dataFrameDay = dateDetails.dataFrame(dateDetails.getDateUtilitesJson())

for i in range(len(dataFrame)):
    dataFrameName = dataFrame.iloc[[i]].nom[i]
    for y in range(len(datagouv)):
        dataGouvName = datagouv.iloc[[y]].nom[y]
        if dataFrameName == dataGouvName:
            FinalData_set = {
                "ville": dataFrame.iloc[[i]].ville[i],
                "nom": datagouv.iloc[[y]].nom[y],
                "date": dataFrame.iloc[[i]].date[i],
                "place_libres": dataFrame.iloc[[i]].place_libres[i],
                "places_totales": dataFrame.iloc[[i]].places_totales[i],
                "prix": datagouv.iloc[[y]].prix[y],
                "longitude": datagouv.iloc[[y]].longitude[y],
                "latitude": datagouv.iloc[[y]].latitude[y],
                "date_status": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['status'],
                "date_day_name": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['jour'],
                "isFérié": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['férier']
            }
            # print(FinalData_set)
            finalArray.append(FinalData_set)
print(finalArray)
finalDataFrame = pd.DataFrame(finalArray)

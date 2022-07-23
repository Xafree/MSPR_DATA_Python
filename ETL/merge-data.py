import pandas as pd

import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
import OpenData.Datagouv as gouv
from DateUtilities import DataUtilies

dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()
datagouv = gouv.getDataAboutCarsParkDataGouv()

dataFrame = pd.DataFrame.from_records(dataMontpellier + dataStrasbourg)

# print(datagouv.head())
finalArray = []
dateDetails = DataUtilies()
dataFrameDay = dateDetails.dataFrame(dateDetails.getDateUtilitesJson())
FinalData_set = {}
isInsert = 0
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
            isInsert = 1
            finalArray.append(FinalData_set)
    if isInsert == 0:
        print("enter")
        FinalData_set = {
            "ville": dataFrame.iloc[[i]].ville[i],
            "nom": datagouv.iloc[[y]].nom[y],
            "date": dataFrame.iloc[[i]].date[i],
            "place_libres": dataFrame.iloc[[i]].place_libres[i],
            "places_totales": dataFrame.iloc[[i]].places_totales[i],
            "prix": None,
            "longitude":  None,
            "latitude": None,
            "date_status": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['status'],
            "date_day_name": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['jour'],
            "isFérié": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['férier']
        }
        finalArray.append(FinalData_set)
    isInsert = 0

print(finalArray)


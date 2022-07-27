import pandas as pd

import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
import OpenData.Datagouv as gouv
from ETL.DateUtilities import DataUtilies

class MergeData:

    def retrieve(self):
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
                        "nom": dataFrame.iloc[[i]].nom[i],
                        "date": dataFrame.iloc[[i]].date[i],
                        "nb_places_libres": int(dataFrame.iloc[[i]].place_libres[i]),
                        "nb_places_totales": int(dataFrame.iloc[[i]].places_totales[i]),
                        "prix": None if pd.isna(datagouv.iloc[[y]].prix[y]) else datagouv.iloc[[y]].prix[y],
                        "longitude": None if pd.isna(datagouv.iloc[[y]].longitude[y]) else datagouv.iloc[[y]].longitude[y],
                        "latitude": None if pd.isna(datagouv.iloc[[y]].latitude[y]) else datagouv.iloc[[y]].latitude[y],
                        "date_status": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['status'],
                        "date_day_name": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['jour'],
                        "isFerie": 1 if dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['isFerie'] else 0
                    }
                    isInsert = 1
                    finalArray.append(FinalData_set)
            if isInsert == 0:
                print("enter")
                FinalData_set = {
                    "ville": dataFrame.iloc[[i]].ville[i],
                    "nom": dataFrame.iloc[[i]].nom[i],
                    "date": dataFrame.iloc[[i]].date[i],
                    "nb_places_libres": int(dataFrame.iloc[[i]].place_libres[i]),
                    "nb_places_totales": int(dataFrame.iloc[[i]].places_totales[i]),
                    "prix": None,
                    "longitude":  None,
                    "latitude": None,
                    "date_status": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['status'],
                    "date_day_name": dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['jour'],
                    "isFerie": 1 if dateDetails.getDetailOfTheDay(dataFrame.iloc[[i]].date[i], dataFrameDay)['isFerie'] else 0
                }
                finalArray.append(FinalData_set)
            isInsert = 0
        # print(finalArray)
        return finalArray


import datetime
from random import randrange
from ETL.DateUtilities import DataUtilies
import json


numdays = 30
parkingMaxPlaces = 239

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

# print(date_list[0])
# print(date_list[0].strftime('%Y-%m-%d %H:%M:%S'))
# print(date_list)

dateDetails = DataUtilies()
dataFrameDay = dateDetails.dataFrame(dateDetails.getDateUtilitesJson())
parking_data = []

for i in range(0, len(date_list)):

    date = date_list[i].strftime('%Y-%m-%d %H:%M:%S')

    dateStatus = dateDetails.getDetailOfTheDay(date, dataFrameDay)['status']
    dateDayName = dateDetails.getDetailOfTheDay(date, dataFrameDay)['jour']
    isFerie = 1 if dateDetails.getDetailOfTheDay(date, dataFrameDay)['isFerie'] else 0

    nbPlacesLibres = 0
    if (dateStatus == "férié"):
        nbPlacesLibres = randrange(0, (parkingMaxPlaces + 1) - 200)
    elif(dateStatus == "week-end"):
        nbPlacesLibres = randrange(0, (parkingMaxPlaces + 1) - 130)
    else:
        nbPlacesLibres = randrange(150, (parkingMaxPlaces + 1))

    data = {
        "ville": "Montpellier",
        "nom": "Antigone",
        "date": date,
        "nb_places_libres": nbPlacesLibres,
        "nb_places_totales": parkingMaxPlaces,
        "prix": None,
        "longitude": 3.88881893,
        "latitude": 43.60871606,
        "date_status": dateStatus,
        "date_day_name": dateDayName,
        "isFerie": isFerie
    }
    parking_data.append(json.dumps(data, ensure_ascii=False))

print(parking_data)


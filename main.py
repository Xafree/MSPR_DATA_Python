import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
from dataBase.Connect import Connect
from dataBase.Request import Request

dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()

#print(dataStrasbourg)

dataTest = {
    'ville': 'Montpellier',
    'nom': 'Antigone',
    'date': '2022-07-24 19:11:52',
    'nb_places_libres': '0172',
    'nb_places_totales': '0239',
    'prix': None,
    'longitude': 3.88881893,
    'latitude': 43.60871606,
    'date_status': 'week-end',
    'date_day_name': 'dimanche',
    'isFerie': 0
}

print("--Data base --")
#Initialize
connect = Connect()
request = Request()

#requeste

#print(request.create(dataTest))

#request.getOneParkings(dataTest)

request.upsertParkingAndWriteInHistoryTable(dataTest)

print("-- Get Parkings --")
request.getParkings()

print("-- Get Parkings Hist --")
request.getParkingsHist()

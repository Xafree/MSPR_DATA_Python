import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
from dataBase.Connect import Connect
from dataBase.Request import Request
from ETL.MergeData import MergeData

dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()

#print(dataStrasbourg)

dataTest = {
    'ville': 'Montpellier',
    'nom': 'Antigone',
    'date': '2022-07-24 19:11:52',
    'nb_places_libres': 172,
    'nb_places_totales': 239,
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

# request.upsertParkingAndWriteInHistoryTable(dataTest)
# request.customUpsert(dataTest)

# dataMtp = montpellier.getDataAboutCarsParkMontepllier()
# dataStras = strasbourg.getDataAboutCarsParkStrasbourg()
# print(dataMtp)
# print(dataStras)

mergeData = MergeData()
mergedDatas = mergeData.retrieve()
print("SIZE OF MERGED DATAS IS : " + str(len(mergedDatas)))
print(mergedDatas)
for i in range(len(mergedDatas)):
    print("MERGE DATA N° : " + str(i))
    print(mergedDatas[i])
    request.upsertParkingAndWriteInHistoryTable(mergedDatas[i])

# print("-- Get Parkings --")
# request.getParkings()
#
# print("-- Get Parkings Hist --")
# request.getParkingsHist()

import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
from dataBase.Connect import Connect
from dataBase.Request import Request

# dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
# dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()

dataTest = {
    "updated_place": "2022-07-07 19:07:30",
    "update_parking": "2022-07-07 19:07:30",
    "nom": "Parking test",
    "num_siret": 152408603,
    "ville": "Montpllier",
    "prix": 00,
    "longitude": 1540,
    "latitude": 4500,
    "nb_place_totale": 500,
    "nb_place_disponible": 250,
    "estgratuit": 1,

}

print("--Data base --")
connect = Connect()
request = Request()
print(request.create(dataTest))
request.get()

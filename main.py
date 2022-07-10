import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
from dataBase.Connect import Connect
from dataBase.Request import Request

dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()

print("--Data base --")
connect = Connect()
print(connect.getConnection())
request = Request()
print(request.get())

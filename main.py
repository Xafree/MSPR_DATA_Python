import OpenData.Montpellier as montpellier
import OpenData.Strasbourg as strasbourg
import dataBase.resquestDataBase as requestData
import dataBase.connexion as connection

#dataMontpellier = montpellier.getDataAboutCarsParkMontepllier()
#dataStrasbourg = strasbourg.getDataAboutCarsParkStrasbourg()

print("--Data base --")
connect = connection.getConnection()
request = requestData.Request()
request.get(connect)

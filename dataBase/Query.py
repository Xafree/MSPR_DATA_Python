class Query:

    def get(self):
        return "Select * from Parkings"

    def insertIntoParkings(self):
        return "INSERT INTO parkings (updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def insertIntoParkingsHist(self):
        return "INSERT INTO parkings_hist (timestamp_id,updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit,id_parking) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def getOneParkings(self):
        return "SELECT * FROM parkings WHERE num_siret = %s"

    def getParkingsHist(self):
        return "Select * from Parkings_hist"

    def checkIfParkingExist(self):
        return "SELECT id_parking FROM parkings WHERE nom = %s"

    def updateParking(self):
        return "UPDATE parkings SET updated_place=%s, update_parking=%s, nom=%s, num_siret=%s, ville=%s, prix=%s, longitude=%s, latitude=%s, nb_place_totale=%s, nb_place_disponible=%s, estgratuit=%s WHERE id_parking =%s"
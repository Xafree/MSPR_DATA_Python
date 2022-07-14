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

#
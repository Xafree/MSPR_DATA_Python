class Query:

    def get(self):
        return "Select * from parkings"

    def insertIntoParkings(self):
        return "INSERT INTO parkings (ville, nom, update_date, nb_places_libres, nb_places_totales, prix, longitude, latitude, date_status, date_day_name, isFerie) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def insertIntoParkingsHist(self):
        return "INSERT INTO parkings_hist (timestamp_id,ville, nom, update_date, nb_places_libres, nb_places_totales, prix, longitude, latitude, date_status, date_day_name, isFerie, id_parking) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def getOneParking(self):
        return "SELECT * FROM parkings WHERE nom = %s"

    def getParkingsHist(self):
        return "Select * from parkings_hist"

    def checkIfParkingExist(self):
        return "SELECT id_parking FROM parkings WHERE nom = %s"

    def updateParking(self):
        return "UPDATE parkings SET ville=%s, nom=%s, update_date=%s, nb_places_libres=%s, nb_places_totales=%s, prix=%s, longitude=%s, latitude=%s, date_status=%s, date_day_name=%s, isFerie=%s WHERE id_parking =%s"

    # TEST NEW UPSERT
    # def upsertParking(self):
    #     return "INSERT INTO parkings (ville, nom, update_date, nb_places_libres, nb_places_totales, prix, longitude, latitude, date_status, date_day_name, isFerie) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE ville=%s, nom=%s, update_date=%s, nb_places_libres=%s, nb_places_totales=%s, prix=%s, longitude=%s, latitude=%s, date_status=%s, date_day_name=%s, isFerie=%s"
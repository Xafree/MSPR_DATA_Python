GET = "Select * from Parkings"
CREATE = ""
UPDATE = ""
DELETE = ""

#INSERT INTO `parkings` (`id_parking`, `updated_place`, `update_parking`, `nom`, `num_siret`, `ville`, `prix`, `longitude`, `latitude`, `nb_place_totale`, `nb_place_disponible`, `estgratuit`)
# VALUES ('1', '2022-07-07 19:07:30', '2022-07-11 19:07:30', 'Toulouse', '1548754', 'Toulouse', '0', '15478', '15487', '350', '150', '1');
class Query:

    def get(self):
        return "Select * from Parkings"

    def getInserIntoParkings(self):
        return "INSERT INTO parkings (id_parking,updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    #Push data who provided open data
    #data is a variable how have data of parkings
    def post(self, data):

        return "INSERT INTO parkings(`id_parking`, `updated_place`, `update_parking`, `nom`, `num_siret`, `ville`, `prix`, `longitude`, `latitude`, `nb_place_totale`, `nb_place_disponible`, `estgratuit`) " \
               "VALUES ("+data['updated_plac']+","+data['update_parking']+","+data['nom']+","+data['num_siret']+","+data['ville']+","+data['prix']+","+data['longitude']+","+data['latitude']+"," \
               ""+data['nb_place_totale']+","+data['nb_place_disponible']+","+data['estgratuit']+")"
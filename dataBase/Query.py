GET = "Select * from Parkings"
CREATE = ""
UPDATE = ""
DELETE = ""


class Query:

    def get(self):
        return "Select * from Parkings"

    #Push data who provided open data
    #data is a variable how have data of parkings
    def post(self, data):

        return "INSERT INTO parkings VALUES ("+data['updated_plac']+","+data['update_parking']+"," \
               ""+data['nom']+","+data['num_siret']+","+data['ville']+","+data['prix']+","+data['longitude']+","+data['latitude']+"," \
               ""+data['nb_place_totale']+","+data['nb_place_disponible']+","+data['estgratuit']+")"
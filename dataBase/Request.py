# -*- coding: utf-8 -*-

from dataBase.Connect import Connect
from dataBase.Query import Query


# for help i used this website http://www.mukeshkumar.net/articles/python/crud-operations-in-python-with-sql-database

class Request:

    def create(self, data):
        # Get the sql connection
        connection = Connect().getConnection()
        # requete SQL
        try:
            sql = ("INSERT INTO parkings (id_parking,updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

            cursor = connection.cursor()
            # Execute the sql query
            cursor.execute(sql, (data['id_parking'], data['updated_place'], data['update_parking'],
                                 data['nom'], data['num_siret'], data['ville'], data['prix'],
                                 data['longitude'], data['latitude'], data['nb_place_totale'],
                                 data['nb_place_disponible'], data['estgratuit']))
            connection.commit()
            print('Success')
        except:
            print('Somthing Wront, check it')
        # Commit the data
        finally:
            connection.close()

    # get all data from Parkings Table
    def get(self):
        # Get the sql connection
        connection = Connect().getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute(Query().get())

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))

        connection.close()

    def update(self):
        return 0

    def delete(self):
        return 0

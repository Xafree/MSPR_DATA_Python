# -*- coding: utf-8 -*-

from dataBase.Connect import Connect
from dataBase.Query import Query
from datetime import datetime


# for help i used this website http://www.mukeshkumar.net/articles/python/crud-operations-in-python-with-sql-database

class Request:

    def create(self, data):
        # Get the sql connection
        connection = Connect().getConnection()
        query = Query()
        # requete SQL
        try:

            sql = query.insertIntoParkings()
            cursor = connection.cursor()
            # Execute the sql query
            cursor.execute(sql, (data['updated_place'], data['update_parking'],
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


    def getParkings(self):
        # Get the sql connection
        connection = Connect().getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute(Query().get())

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))

        connection.close()

    def upsertParkingAndWriteInHistoryTable(self, data):
        # SQL connect dataBase
        connection = Connect().getConnection()
        # Query Sql we need
        query = Query()

        # We want to push in 'parkings' table and save data in 'parkings_hist'
        #try:
        cursor = connection.cursor()
        sqlCheckIfExist = query.checkIfParkingExist()
        cursor.execute(sqlCheckIfExist,(data['nom'],))
        result = cursor.fetchall()
        print(result)
        try:
            if result == [] :
                sqlParkings = query.insertIntoParkings()
                # Insert data in parkings table
                cursor.execute(sqlParkings, (data['ville'], data['nom'],
                                             data['date'], data['nb_places_libres'], data['nb_places_totales'], data['prix'],
                                             data['longitude'], data['latitude'], data['date_status'],
                                             data['date_day_name'], data['isFerie']))
                # connection.commit()

                # Get id of last request
                sqlGetIdParking = query.getOneParking()
                cursor.execute(sqlGetIdParking, (data['nom'],))
                record = cursor.fetchall()
                id_parkings = record[0][0]

                # push in parkings_Hist to save record
                dt = datetime.now()
                # TimeStamp
                print("Time Stamp : "+ dt.strftime("%Y-%m-%d %H:%M:%S"))
                sqlParkingsHist = query.insertIntoParkingsHist()
                # timestamp_id,updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit, id_parking
                cursor.execute(sqlParkingsHist, (dt.strftime("%Y-%m-%d %H:%M:%S"),data['ville'], data['nom'],
                                             data['date'], data['nb_places_libres'], data['nb_places_totales'], data['prix'],
                                             data['longitude'], data['latitude'], data['date_status'],
                                             data['date_day_name'], data['isFerie'], id_parkings))
                connection.commit()
            else:
                sqlUpdateParking = query.updateParking()
                cursor.execute(sqlUpdateParking, (data['ville'], data['nom'],
                                             data['date'], data['nb_places_libres'], data['nb_places_totales'], data['prix'],
                                             data['longitude'], data['latitude'], data['date_status'],
                                             data['date_day_name'], data['isFerie'],result[0][0]))
                print("here")
                dt = datetime.now()
                # TimeStamp
                print("Time Stamp : "+ dt.strftime("%Y-%m-%d %H:%M:%S"))
                sqlParkingsHist = query.insertIntoParkingsHist()
                # timestamp_id,updated_place, update_parking, nom, num_siret, ville, prix, longitude, latitude, nb_place_totale, nb_place_disponible, estgratuit, id_parking
                cursor.execute(sqlParkingsHist, (dt.strftime("%Y-%m-%d %H:%M:%S"),data['ville'], data['nom'],
                                             data['date'], data['nb_places_libres'], data['nb_places_totales'], data['prix'],
                                             data['longitude'], data['latitude'], data['date_status'],
                                             data['date_day_name'], data['isFerie'], result[0][0]))
                connection.commit()
        except ValueError:
            print(ValueError)
        finally:
            connection.close()

    def getOneParking(self, data):

        connection = Connect().getConnection()
        query = Query()

        cursor = connection.cursor()

        sqlGetIdParkings = query.getOneParking()
        cursor.execute(sqlGetIdParkings, (data['num_siret'],))
        record = cursor.fetchall()
        print(record[0][0])

    def getParkingsHist(self):
        # Get the sql connection
        connection = Connect().getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute(Query().getParkingsHist())

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))
        connection.close()

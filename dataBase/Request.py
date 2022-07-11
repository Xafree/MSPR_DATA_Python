# -*- coding: utf-8 -*-
from dataBase.Connect import Connect
from dataBase.Query import Query



# for help i used this website http://www.mukeshkumar.net/articles/python/crud-operations-in-python-with-sql-database

class Request:

    def create(self, data):

        # Get the sql connection
        connection = Connect().getConnection()

        try:
            query = Query.post("INSERT INTO parkings VALUES (2,'2022-07-07 19:07:30', '2022-07-11 19:07:30', 'Toulon', 1548754, 'TOULON', 0.0, 15478.0, 15487.0, 350, 150, 0")
            cursor = connection.cursor()

            # Execute the sql query
            cursor.execute(query)
            cursor.description
            # Commit the data
            connection.commit()
            print('Data Saved Successfully')

        except:
            print('Something worng, please check')

        finally:
            # Close the connection
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

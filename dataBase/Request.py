# -*- coding: utf-8 -*-
from dataBase.Connect import Connect
from dataBase.Query import Query



# for help i used this website http://www.mukeshkumar.net/articles/python/crud-operations-in-python-with-sql-database

class Request:

    def create(self, data):

        # Get the sql connection
        connection = Connect().getConnection()

        try:
            query = Query.post(data)
            cursor = connection.cursor()

            # Execute the sql query
            cursor.execute(query)

            # Commit the data
            connection.commit()
            print('Data Saved Successfully')

        except:
            print('Somethng worng, please check')

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

import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


class Connect:

    def getConnection(self):
        connection = mysql.connector.connect(host=os.getenv("HOST"), database=os.getenv("DATABASE"),
                                             user=os.getenv("LOGIN"), password=os.getenv("PASSWORD"),
                                             port=os.getenv("PORT"))
        return connection

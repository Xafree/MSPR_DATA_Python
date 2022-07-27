import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


class Connect:

    def getConnection(self):
        connection = mysql.connector.connect(host=os.getenv("HOST_LOCAL"), database=os.getenv("DATABASE_LOCAL"),
                                             user=os.getenv("LOGIN_LOCAL"), password=os.getenv("PASSWORD_LOCAL"),
                                             port=os.getenv("PORT_LOCAL"))
        return connection

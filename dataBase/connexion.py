import requests
import pandas as pd
import numpy as np
import json
import os
import mysql.connector

from dotenv import load_dotenv
from xml.etree import ElementTree
from mysql.connector import Error

load_dotenv()

HOST = os.getenv("HOST_LOCAL")
DATABASE = os.getenv("DATABASE_LOCAL")
USER = os.getenv("LOGIN_LOCAL")
PASSEWORD = os.getenv("PASSWORD_LOCAL")
PORT = os.getenv("PORT_LOCAL")

try:
    connection = mysql.connector.connect(host=HOST, database=DATABASE,
                                         user=USER, password=PASSEWORD,
                                         port=PORT)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("Select * from parkings")
        record = cursor.fetchone()
        print(record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

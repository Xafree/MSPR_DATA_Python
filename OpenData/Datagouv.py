import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def getURL():
    return os.getenv("DATAGOUV")


def getDataGouv(URL):
    df = pd.read_csv(URL, on_bad_lines='skip', sep=';')
    dataGouv = pd.DataFrame(
        {
            'nom': df['nom'],
            'insee': df['insee'],
            'gratuit': df['gratuit'],
            'longitude': df['Xlong'],
            'latitude': df['Ylat'],
            'prix': df['tarif_1h']
        })
    return dataGouv


def getDataAboutCarsParkDataGouv():
    return getDataGouv(getURL())

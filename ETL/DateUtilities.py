import os

import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class DataUtilies:

    def getDateUtilitesJson(self):
        Feriado = requests.get(os.getenv('DATEUTILITES'))
        Feriado.status_code
        listes = Feriado.json()
        listes = [liste["fields"] for liste in listes]
        return listes
    # print(getDateUtilitesJson()).

    def dataFrame(self, listes):
        df_jour = pd.DataFrame(listes)
        return df_jour

    # dataFrame = dataFrame(getDateUtilitesJson())

    def getAllDays(self, df_jour):
        df_jour['statut'].value_counts()
        statut_par_jour = {df_jour['date'][fila]: {'status': df_jour['statut'][fila], 'day': df_jour['jour'][fila]} for
                           fila
                           in range(len(df_jour.index))}
        return statut_par_jour

    # print(getAllDays(getDateUtilitesJson()))

    def status(self, getAllDays, date):
        etat = getAllDays[date]
        return etat['status']

    # print(status(getAllDays(getDateUtilitesJson()),'2020-01-10'))

    def ferie(self, getAllDays, date):
        etat = getAllDays[date]
        reponse = etat == 'férié'
        return reponse

    # print(ferie(getAllDays(getDateUtilitesJson()),'2020-01-10'))

    def fecha_datatime(self, date):
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S')
        return date

    # print(fecha_datatime('2020-01-10'))

    def dayName(self, getAllDays, date):
        day = getAllDays[date]
        return day['day']

    # print(dayName(getAllDays(getDateUtilitesJson()), '2020-01-10'))

    def getDetailOfTheDay(self, date, dataFrame):  # Date format : YYYY-MM-JJ
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        details = {
            'jour': self.dayName(self.getAllDays(dataFrame), date),
            'status': self.status(self.getAllDays(dataFrame), date),
            'isFerie': self.ferie(self.getAllDays(dataFrame), date)
        }
        return details
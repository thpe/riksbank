# Copyright 2018, 2024 Thomas Petig
#
import requests
import json
import pandas as pd

class query:
    def __init__(self, user, key):
        self.user = user
        self.key = key


    def getObservations(self, seriesid, datefrom, dateto):
        q = f'https://api.riksbank.se/swea/v1/Observations/{seriesid}/{datefrom}/{dateto}'
        print(q)
        r = requests.get(q, auth=(self.user, self.key))
        print(r.text)
        so = json.loads(r.text)
        print(so)
        date =  [b['date'] for b in so]
        value =  [b['value'] for b in so]
        df = pd.Series(data=value, index=date)
        return df

    def getCalendarDays(self, datefrom, dateto):
        q = f'https://api.riksbank.se/swea/v1/CalendarDays/{datefrom}/{dateto}'
        r = requests.get(q, auth=(self.user, self.key))
        print(r.text)
        so = json.loads(r.text)
        bankday = [True if b['swedishBankday'] == 'Y' else False for b in so]
        date =  [b['calendarDate'] for b in so]
        week =  [b['weekNumber'] for b in so]
        weekyear = [b['weekYear'] for b in so]
        df = pd.DataFrame({'date': date, 'bankday': bankday, 'week': week, 'weekyear': weekyear}).set_index('date')
        return df

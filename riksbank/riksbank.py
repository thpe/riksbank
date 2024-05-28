""" API abstraction for the swedish central bank """
# Copyright 2018, 2024 Thomas Petig
#
import json
import requests
import pandas as pd

class Query:
    """ query class containing the whole API abstraction """
    def __init__(self, user, key):
        """ init, sets user and key for Rest API """
        self.user = user
        self.key = key


    def get_observations(self, seriesid, datefrom, dateto):
        """ returns a specfic observation for a time intervall """
        querystr = f'https://api.riksbank.se/swea/v1/Observations/{seriesid}/{datefrom}/{dateto}'
        print(querystr)
        req = requests.get(querystr, auth=(self.user, self.key), timeout='100')
        print(req.text)
        jsondata = json.loads(req.text)
        print(jsondata)
        date = [ele['date'] for ele in jsondata]
        value = [ele['value'] for ele in jsondata]
        dfres = pd.Series(data=value, index=date)
        return dfres

    def get_calendar_days(self, datefrom, dateto):
        """ get the requested calendar days """
        querystr = f'https://api.riksbank.se/swea/v1/CalendarDays/{datefrom}/{dateto}'
        req = requests.get(querystr, auth=(self.user, self.key), timeout='100')
        print(req.text)
        jsondata = json.loads(req.text)
        bankday = [ele['swedishBankday'] == 'Y' for ele in jsondata]
        date = [ele['calendarDate'] for ele in jsondata]
        week = [ele['weekNumber'] for ele in jsondata]
        weekyear = [ele['weekYear'] for ele in jsondata]
        dfres = pd.DataFrame({'date': date,
                           'bankday': bankday,
                           'week': week,
                           'weekyear': weekyear}).set_index('date')
        return dfres

# Copyright 2018 Thomas Petig
#
from zeep import Client
from zeep.helpers import serialize_object
import pandas as pd

class query:
    def __init__(self):
        self.client = Client('https://swea.riksbank.se/sweaWS/wsdl/sweaWS.wsdl')


    def getInterestAndExchangeRates(self, groupid, seriesid, datefrom, dateto, average=True, minimum=False, maximum=False, ultimo=False):
        SGS = {
                'groupid': groupid,
                'seriesid': seriesid
                }
        searchRequestParameters = {
                'aggregateMethod': 'W',
                'avg': average,
                'datefrom': datefrom,
                'dateto': dateto,
                'languageid': 'en',
                'max': maximum,
                'min': minimum,
                'searchGroupSeries': [SGS],
                'ultimo': ultimo
                }
        resp = self.client.service.getInterestAndExchangeRates(searchRequestParameters)
        so = serialize_object(resp)['groups'][0]['series'][0]['resultrows']
        df = pd.DataFrame(so)
        df.index = pd.to_datetime(df['date'])
        return df

    def getCalendarDays(self, datefrom, dateto):
        result = self.client.service.getCalendarDays(datefrom, dateto)
        so = serialize_object(result)
        bankday = [True if b['bankday'] == 'Y' else False for b in so]
        date =  [b['caldate'] for b in so]
        week =  [b['week'] for b in so]
        weekyear = [b['weekyear'] for b in so]
        df = pd.DataFrame({'date': date, 'bankday': bankday, 'week': week, 'weekyear': weekyear}).set_index('date')
        return df

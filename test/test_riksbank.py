""" test framework for riksbank """
import os
from riksbank import riksbank


def test_read_observation():
    """ tests to read an observation """
    print('test observations')
    user = os.environ['RIKSBANK_USER']
    key = os.environ['RIKSBANK_KEY']
    query = riksbank.Query(user, key)
    res = query.get_observations('SEKEURPMI', '2024-01-01', '2024-02-01')
    print(res)


def test_read_calendardays():
    """ tests to read calendar days """
    print('test calendar days')
    user = os.environ['RIKSBANK_USER']
    key = os.environ['RIKSBANK_KEY']
    query = riksbank.Query(user, key)
    res = query.get_calendar_days('2024-01-01', '2024-02-01')
    print(res)


if __name__ == "__main__":
    test_read_observation()
    test_read_calendardays()

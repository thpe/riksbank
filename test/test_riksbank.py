import os
from riksbank import riksbank

def test_read_observation():
    print('test observations')
    u = os.environ['RIKSBANK_USER']
    k = os.environ['RIKSBANK_KEY']`
    r = riksbank.query(u, k)
    d = r.getObservations('SEKEURPMI', '2024-01-01', '2024-02-01')
    print(d)
def test_read_calendardays():
    print('test calendar days')
    u = os.environ['RIKSBANK_USER']
    k = os.environ['RIKSBANK_KEY']`
    r = riksbank.query(u, k)
    d = r.getCalendarDays('2024-01-01', '2024-02-01')
    print(d)


if __name__ == "__main__":
    test_read_observation()
    test_read_calendardays()

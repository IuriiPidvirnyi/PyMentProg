import json
from datetime import datetime, timedelta
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('json_path', help='Enter appropriate path to JSON file', type=str)
parser.add_argument('ndays', help='Enter amount of days to be retrieved', type=int)
args = parser.parse_args()

print("\nScript name (path): %s" % str(sys.argv[0]))

json_path = args.json_path
ndays = args.ndays

print ("Path to JSON file: %s" % json_path)
print ("Days to be retrieved in one direction: %i" % ndays)

entered_date = input("\nPlease, enter a date('YYYY-MM-DD'): ")
user_date = datetime.strptime(entered_date, '%Y-%m-%d').date()

def befdates(user_date, ndays):
    bef_user_date = []
    while ndays > 0:
        bef_user_date.append(str(user_date - timedelta(days=ndays)))
        ndays -= 1
    return bef_user_date


def aftdates(user_date, ndays):
    aft_user_date = []
    while ndays > 0:
        aft_user_date.append(str(user_date + timedelta(days=ndays)))
        ndays -= 1
    return list(reversed(aft_user_date))

# print(befdates(user_date, ndays))
# print(aftdates(user_date, ndays))

with open(json_path, "r") as f:
    fd = json.load(f)

# 2013-12-10

print('\nDATE_FROM', fd['DATE_FROM'])
print('DATE_TO', fd['DATE_TO'])
print('STATION_CALL_LETTERS', fd['STATION']['STATION_CALL_LETTERS'])
print('STATION_NAME', fd['STATION']['STATION_NAME'], '\n')

bhh = 0
uhh = 0
ahh = 0
for i in befdates(user_date, ndays):
    for n in fd['ITEMS']:
        if i == n['IMPRESSION_DATE']:
            bhh += n['HH']
        else:
            continue
    print(i, bhh)

for n in fd['ITEMS']:
    if str(user_date) == n['IMPRESSION_DATE']:
        uhh += n['HH']
    else:
        continue
print(str(user_date), uhh)

for i in aftdates(user_date, ndays):
    for n in fd['ITEMS']:
        if i == n['IMPRESSION_DATE']:
            ahh += n['HH']
        else:
            continue
    print(i, ahh)

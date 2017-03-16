import json
from datetime import datetime, timedelta
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('PATH_TO_JSON', help='Enter appropriate path to JSON file', type=str)
args = parser.parse_args()

print("\nScript name (path): %s" % str(sys.argv[0]))

json_path = args.PATH_TO_JSON

print ("\nPath to JSON file: %s" % json_path)

with open(json_path, "r") as f:
    fd = json.load(f)
    for i in fd:
        if i == "DATE_FROM":
            print("\n" + i + ":", fd[i])
    for i in fd:
        if i == "DATE_TO":
            print(i + ":", fd[i])
    for i in fd:
        if i == "STATION":
            for j in fd[i]:
                # print(j)
                if j == "STATION_CALL_LETTERS":
                    print(j + ":", fd[i][j])
            for j in fd[i]:
                if j == "STATION_NAME":
                    print(j + ":", fd[i][j])

    ud = USER_DATE = input("\nPlease, enter a date('YYYY-MM-DD'): ")
    # USER_DATE = "2016-02-28"
    def usrdate(ud):
        user_date = datetime.strptime(ud, '%Y-%m-%d').date()
        bef_user_date = user_date - timedelta(days=1)
        aft_user_date = user_date + timedelta(days=1)
        return bef_user_date, user_date, aft_user_date
    print("A day before entered date: " + str(usrdate(ud)[0]))
    print("A day after entered date: " + str(usrdate(ud)[2]) + "\n")

    bhh = []
    uhh = []
    ahh = []

    for i in fd:
        if i == "IMPRESSION_DATE":
            print(i)
        else:
            for j in fd[i]:
                # print(j)
                if j == "IMPRESSION_DATE":
                    print(j)
                else:
                    for n in j:
                        if n == "HH" and j["IMPRESSION_DATE"] == str(usrdate(ud)[0]):
                            bhh.append(j[n])
                        elif n == "HH" and j["IMPRESSION_DATE"] == str(usrdate(ud)[1]):
                            uhh.append(j[n])
                        elif n == "HH" and j["IMPRESSION_DATE"] == str(usrdate(ud)[2]):
                            ahh.append(j[n])

    print(str(usrdate(ud)[0]) + ':', sum(bhh))
    print(str(usrdate(ud)[1]) + ':', sum(uhh))
    print(str(usrdate(ud)[2]) + ':', sum(ahh))






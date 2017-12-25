import csv
from collections import  namedtuple

filename = "../../source/sitka_weather_date.cvs"
with open(filename) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row',headers)

    for r in f_csv:
        row = Row(*r)
       # print(row[0])



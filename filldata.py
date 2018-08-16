import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "world_health_status.settings")

import django
django.setup()

from django.apps import apps
from map.models import Disease

import csv

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True


# data = csv.reader(open(r"C:\Users\Aadam\Google Drive\Masters\Individual Project\world_health_status\HIV_0000000006_2017.csv", newline=''), delimiter=',')

# disease = Disease()

# for row in data:
#     disease.gho = row[0]
#     disease.year = row[1]
#     disease.numeric = row[5]
#     disease.region = row[2]

with open(r"C:\Users\Aadam\Google Drive\Masters\Individual Project\world_health_status\HIV_0000000006_2017.csv", newline='') as csvfile:
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    csvfile.seek(0)
    data = csv.reader(csvfile)

    #skips first line of headers
    if has_header:
        next(data)


    disease = Disease()

    for row in data:
        # print(', '.join(row))
        disease = Disease()

        disease.gho = row[0]
        disease.year = row[1]
        disease.region = row[2]
        disease.country = row[3]

        if not isBlank(row[4]):
            # print(row[3])
            disease.numeric = row[4]
            # disease.low = row[5]
            # disease.high = row[6]

        # # print(disease.country)
        # disease.save()
        
        try:
            disease.save()
        except:
            print("error on row: " + str(row[3]))


# disease.save()

# print(disease.region)



from tinydb import TinyDB
from tinydb import where
db = TinyDB('data/homework_08.tinyDB')
import json

table = db.table("california_real_estate")

def AverageCost():
    total = 0

    data = table.search((where('price')>='0') & (where('zip')=='95838') & (where('type')=='Residential'))

    AvgNumb = len(data)

    for document in data:
        total = total + float(document['price'])

    Average = str(round(total/AvgNumb,2))

    print(str("The average price of a residental house in zip code 95838 is " + "${:,}".format(float(Average))))

def AverageCostofThree():
    total = 0

    data = table.search((where('beds')>='3') & (where('zip')=='95838'))

    AvgNumb = len(data)

    for document in data:
        total = total + float(document['price'])

    Average = str(round(total/AvgNumb,2))

    print(str("The average price of a three bed home in zip code 95838 is " + "${:,}".format(float(Average))))

def AverageSquareFeet():
    total = 0

    data = table.search((where('sq__ft')>='0') & (where('zip')=='95838'))

    AvgNumb = len(data)

    for document in data:
        total = total + float(document['sq__ft'])

    Average = str(round(total/AvgNumb,0))

    print(str("The average square feet of a home in zip code 95838 is " + "{:,}".format(float(Average))))

def AverageBeds():
    total = 0

    data = table.search((where('beds')>='0') & (where('zip')=='95838'))

    AvgNumb = len(data)

    for document in data:
        total = total + float(document['beds'])

    Average = str(round(total/AvgNumb,0))

    print(str("The average beds of a home in zip code 95838 is " + "{:,}".format(float(Average))))
    
def AverageBaths():
    total = 0

    data = table.search((where('baths')>='0') & (where('zip')=='95838'))

    AvgNumb = len(data)

    for document in data:
        total = total + float(document['baths'])

    Average = str(round(total/AvgNumb,0))

    print(str("The average bathrooms of a home in zip code 95838 is " + "{:,}".format(float(Average))))

def whyman():
    data = table.all()
    total = []
    for document in data:
        if document['zip'] not in total:
            total.append(document['zip'])
    return total

def CostByZipStarter():
    plopper = whyman()
    for zip in plopper:
        AllAverage(zip)
            
def AllAverage(CallZip):
    total = 0

    data = table.search((where('price')>='0') & (where('zip')==CallZip) & (where('type')=='Residential'))

    AvgNumb = len(data)
    TotalHomes = 0
    for document in data:
        total = total + float(document['price'])
        TotalHomes = TotalHomes + 1

    Average = str(round(total/AvgNumb,2))

    print(str("There are " + str(TotalHomes) + " total residential homes in the zip code " + CallZip + " and the average price is " + "${:,}".format(float(Average))))

AverageCost()
AverageBeds()
AverageBaths()
AverageSquareFeet()
AverageCostofThree()
print()
CostByZipStarter()


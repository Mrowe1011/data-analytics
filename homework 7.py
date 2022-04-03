from tinydb import TinyDB
from tinydb import where
from tinydb import Query
db = TinyDB('data/homework_08.tinyDB')
import json
db = TinyDB('data/homework_07.tinyDB')

table = db.table("customers")

data1 = table.all()

print(str(len(data1)) + " total customers records")

data2 = table.search(where('customer')['car']=='toyota')

print()

print(str(len(data2)) + " customers records with Toyota car")

formatted1 = json.dumps(data2,sort_keys=False, indent=4)

print(formatted1)

data3 = table.search((where('customer')['car']=='toyota') & (where('customer')['pet']=='fish'))

print()
print(str(len(data3)) + " customers records with toyota car and pet fish")

formatted2 = json.dumps(data3,sort_keys=False, indent=4)

print(formatted2)

totalDebt = 0

data4 = table.search((where('customer')['debt']>=0) & (where('customer')['car']=='vw'))

for document in data4:
    totalDebt = totalDebt + float(document['customer']['debt'])

print()
print('Customers with vw car')
print('total debt=' + str(totalDebt))

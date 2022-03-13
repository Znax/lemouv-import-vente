import csv
from datetime import datetime
from decimal import Decimal
from vente import Group

print("*** Let's begin ***")
# CSV File

formats = {"day": '%Y-%m-%d', "month": '%Y-%m', "hours": '%Y-%m_%Hh'}
for filename in formats:
    csvfile = open('./ventes.csv', 'r')
    csvreader = csv.DictReader(csvfile)
    products = {}
    groups = {}
    for oneline in csvreader:
        date_time_obj = datetime.strptime(oneline['date'], '%Y-%m-%d %H:%M:%S')
        if oneline['produit_id'] not in products:
            products[oneline['produit_id']] = oneline['description']

        group = date_time_obj.strftime(formats[filename])
        if group not in groups:
            groups[group] = Group(group)
        groups[group].cumul(oneline['produit_id'], Decimal(oneline['prix']))
    # closing csvfile
    csvfile.close()

    products = sorted(products.items(), key=lambda x: x[1])
    header = ['date']

    for key, name in products:
        header.append(name)

    nblines = 0
    pathname = './' + filename + '.csv'
    f = open(pathname, 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    for groupID in groups:
        row = [groupID]
        nblines += 1
        for key, name in products:
            row.append(groups[groupID].getProduct(key).getCumulPrice())
        writer.writerow(row)
    f.close()

    print(filename, ":exported ", nblines, " lines, ", len(products), " products")
print("*** The END ***")

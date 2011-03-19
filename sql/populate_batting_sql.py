import MySQLdb
import csv
import numpy

datadir = "/home/deen/Data/FunStuff/FantasyBaseball/"
df = csv.DictReader(open(datadir+'Batting.csv', 'r'), delimiter = ",", quotechar='\"')

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db = "sabrmetrics")

cursor = conn.cursor()

field_types = []
for fname in df.fieldnames:
    if fname.upper() == "PLAYERID":
        field_types.append('C')
    elif fname.upper() == "TEAMID":
        field_types.append('C')
    elif fname.upper() == "LGID":
        field_types.append('C')
    else:
        field_types.append('I')

categories = []
category_str = ' ( '+df.fieldnames[0].upper()
categories.append(df.fieldnames[0])
for fname in df.fieldnames[1:]:
    category_str += ', ' + fname.upper()
    categories.append(fname)

category_str += ') '
for row in df:
    if field_types[0] == 'C':
        value_str = " ('"+row[categories[0]]+"'"
    else:
        value_str = " ("+row[categories[0]]
    for cat, t in zip(categories[1:], field_types[1:]):
        value = row[cat]
        if value == '':
           value = str(0)
        if t == 'I':
            value_str += ', ' + value
        if t == 'C':
            value_str += ", '" + value +"'"
    value_str += ')'
    #print category_str
    #print value_str
    #raw_input()
    cursor.execute("INSERT INTO batting"+category_str+" VALUES "+value_str)

cursor.close()
conn.commit()
conn.close()


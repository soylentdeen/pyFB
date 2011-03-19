import MySQLdb

datafile = open(raw_input("Enter Team Datafile"), 'r').read().splitlines()

teamInfo = datafile[0].split(',')

teamName = teamInfo[0].strip()
teamID = teamInfo[1].strip()
teamOwner = teamInfo[2].strip()
teamEmail = teamInfo[3].strip()

batters = []
bench = []
sp = []
rp = []
bullpen = []

for line in datafile[1:]:
    l = line.split(',')
    if l[0] == 'b':
        batters.append(l[1].strip())
    elif l[0] == 'bench':
        bench.append(l[1].strip())
    elif l[0] == 'sp':
        sp.append(l[1].strip())
    elif l[0] == 'rp':
        rp.append(l[1].strip())
    elif l[0] == 'bp':
        bullpen.append(l[1].strip())

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db='sabrmetrics')
cursor = conn.cursor()

#category_str = " ( TEAMID, OWNER, OWNEREMAIL"
#value_str = " ( '"+teamID+"', '"+teamOwner+"', '"+teamEmail+"'"
category_str = " (NAME, TEAMID, OWNER, EMAIL"
value_str = " ('"+teamName+"', '"+teamID+"', '"+teamOwner+"', '"+teamEmail+"'"
for i in range(len(batters)):
    category_str += ", BAT"+str(i)
    value_str += ", '"+batters[i]+"'"
for i in range(len(bench)):
    category_str += ", BENCH"+str(i)
    value_str += ", '"+bench[i]+"'"
for i in range(len(sp)):
    category_str += ", SPITCH"+str(i)
    value_str += ", '"+sp[i]+"'"
for i in range(len(rp)):
    category_str += ", RPITCH"+str(i)
    value_str += ", '"+rp[i]+"'"
for i in range(len(bullpen)):
    category_str += ", BULLPEN"+str(i)
    value_str += ", '"+bullpen[i]+"'"

category_str += " ) "
value_str += " )"

cursor.execute("INSERT INTO teams"+category_str+"VALUES"+value_str)

cursor.close()
conn.commit()
conn.close()

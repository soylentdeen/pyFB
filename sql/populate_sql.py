import MySQLdb
import numpy

datadir = "/home/deen/Data/StarFormation/TWA/Covey10/CoveyB59SpeX/"
df = open(datadir+'covey_sources.txt', 'r').read().split('\n')

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db = "TWA_YSOS")

cursor = conn.cursor()

spect_name = []
opt_spt = []
IR_spt = []
twa_num = []

for l in df:
    if (len(l) > 0):
        if (l[0] != ';'):
            line = l.split()
            spect_name.append(line[0])
            opt_spt.append(float(line[1]))
            IR_spt.append(float(line[2]))
            twa_num.append(line[3])

for dat in zip(spect_name, opt_spt, IR_spt, twa_num):
    category_str = ' (name, OPT_SPT, IR_SPT, SXD_clean) '
    value_str = " ('"+dat[3]+"',"+str(dat[1])+","+str(dat[2])+",'"+datadir+dat[0]+"')"
    cursor.execute("INSERT INTO objects"+category_str+"VALUES"+value_str)

cursor.close()
conn.commit()
conn.close()


import MySQLdb
import numpy
import scipy

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db='sabrmetrics')

cursor = conn.cursor(MySQLdb.cursors.DictCursor)

#exec_str = "SELECT NAME, TEAMID, "

#exec_str += " FROM teams"

nbatters = 9

cursor.execute("SELECT * FROM teams")

result_set = cursor.fetchall()

for team in result_set:
    batters = []
    pitchers = []
    for i in range(nbatters):
        if 'BAT'+str(i) in team:
            batters.append(team["BAT"+str(i)])

print batters

TB = 0
HR = 0
SB = 0
H = 0

for batter in batters:
    cursor.execute("SELECT * FROM batting WHERE YEARID = 2010 AND PLAYERID = '"+batter+"'")
    stats = cursor.fetchall()
    if (len(stats) > 0):
        for stint in stats:
            HR += stint["HR"]
            SB += stint["SB"]
            hits = stint["H"]
            xbh = stint["HR"] + stint["3B"] + stint["2B"]
            atbats = stint["AB"]
            singles = hits- xbh
            H += hits
            TB += stint["HR"]*4 + stint["3B"]*3 + stint["2B"]*2 + singles

print "Home Runs: ", HR
print "Total Bases: ", TB
print "Stolen Bases: ", SB
print "Hits : ", H

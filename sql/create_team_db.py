import MySQLdb

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db='sabrmetrics')

cursor = conn.cursor()

cursor.execute ("DROP TABLE IF EXISTS teams")
cursor.execute ("""
    CREATE TABLE teams
    (
       NAME VARCHAR(60)
    )
    """)

batting_slots = 9
batting_bench_slots = 5
starting_pitching_slots = 5
relief_pitching_slots = 3
pitching_bench_slots = 5
#batting_slots = len(batters)
#pitching_slots = len(pitchers)

cursor.execute( "ALTER TABLE teams ADD TEAMID VARCHAR(20);")
cursor.execute( "ALTER TABLE teams ADD OWNER VARCHAR(20);")
cursor.execute( "ALTER TABLE teams ADD EMAIL VARCHAR(30);")
for i in range(batting_slots):
    cursor.execute( "ALTER TABLE teams ADD BAT"+str(i)+" VARCHAR(10);")
for i in range(batting_bench_slots):
    cursor.execute( "ALTER TABLE teams ADD BENCH"+str(i)+" VARCHAR(10);")
for i in range(starting_pitching_slots):
    cursor.execute( "ALTER TABLE teams ADD SPITCH"+str(i)+" VARCHAR(10);")
for i in range(relief_pitching_slots):
    cursor.execute( "ALTER TABLE teams ADD RPITCH"+str(i)+" VARCHAR(10);")
for i in range(pitching_bench_slots):
    cursor.execute( "ALTER TABLE teams ADD BULLPEN"+str(i)+" VARCHAR(10);")
cursor.execute( "ALTER TABLE teams ADD H INT(3);")
cursor.execute( "ALTER TABLE teams ADD AB INT(3);")
cursor.execute( "ALTER TABLE teams ADD BB INT(3);")
cursor.execute( "ALTER TABLE teams ADD TB INT(3);")
cursor.execute( "ALTER TABLE teams ADD SB INT(3);")
cursor.execute( "ALTER TABLE teams ADD HR INT(3);")
cursor.execute( "ALTER TABLE teams ADD AVG FLOAT(5);")
cursor.execute( "ALTER TABLE teams ADD OBP FLOAT(5);")
cursor.execute( "ALTER TABLE teams ADD IP INT(3);")
cursor.execute( "ALTER TABLE teams ADD ER INT(3);")
cursor.execute( "ALTER TABLE teams ADD K INT(3);")
cursor.execute( "ALTER TABLE teams ADD HA INT(3);")
cursor.execute( "ALTER TABLE teams ADD BBA INT(3);")
cursor.execute( "ALTER TABLE teams ADD QS INT(3);")
cursor.execute( "ALTER TABLE teams ADD ERA FLOAT(5);")
cursor.execute( "ALTER TABLE teams ADD WHIP FLOAT(5);")


cursor.close()
conn.commit()
conn.close()


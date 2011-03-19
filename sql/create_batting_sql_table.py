import MySQLdb

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db='sabrmetrics')

cursor = conn.cursor()

cursor.execute ("DROP TABLE IF EXISTS batting")
cursor.execute ("""
    CREATE TABLE batting
    (
       PLAYERID VARCHAR(20)
    )
    """)

cursor.execute( "ALTER TABLE batting ADD YEARID INT(5);")
cursor.execute( "ALTER TABLE batting ADD STINT INT(3);")
cursor.execute( "ALTER TABLE batting ADD TEAMID VARCHAR(10);")
cursor.execute( "ALTER TABLE batting ADD LGID VARCHAR(10);")
cursor.execute( "ALTER TABLE batting ADD G INT(3);")
cursor.execute( "ALTER TABLE batting ADD G_BATTING INT(3);")
cursor.execute( "ALTER TABLE batting ADD AB INT(3);")
cursor.execute( "ALTER TABLE batting ADD R INT(3);")
cursor.execute( "ALTER TABLE batting ADD H INT(3);")
cursor.execute( "ALTER TABLE batting ADD 2B INT(3);")
cursor.execute( "ALTER TABLE batting ADD 3B INT(3);")
cursor.execute( "ALTER TABLE batting ADD HR INT(3);")
cursor.execute( "ALTER TABLE batting ADD RBI INT(3);")
cursor.execute( "ALTER TABLE batting ADD SB INT(3);")
cursor.execute( "ALTER TABLE batting ADD CS INT(3);")
cursor.execute( "ALTER TABLE batting ADD BB INT(3);")
cursor.execute( "ALTER TABLE batting ADD SO INT(3);")
cursor.execute( "ALTER TABLE batting ADD IBB INT(3);")
cursor.execute( "ALTER TABLE batting ADD HBP INT(3);")
cursor.execute( "ALTER TABLE batting ADD SH INT(3);")
cursor.execute( "ALTER TABLE batting ADD SF INT(3);")
cursor.execute( "ALTER TABLE batting ADD GIDP INT(3);")
cursor.execute( "ALTER TABLE batting ADD G_OLD INT(3);")

cursor.close()
conn.close()


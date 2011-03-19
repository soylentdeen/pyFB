import MySQLdb
import numpy
import scipy

conn = MySQLdb.connect(host="localhost", user="deen", passwd="password", db='sabrmetrics')
cursor = conn.cursor()



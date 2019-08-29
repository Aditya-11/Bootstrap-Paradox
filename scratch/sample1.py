import pymysql
import csv
#csv_data = csv.reader(file(‘datafile.csv'))

with open('datafile.csv', 'r') as csvFile:
    csv_data = csv.reader(csvFile)

db = pymysql.connect("localhost","root","password","DELL")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

cursor.execute("DROP TABLE IF EXISTS DELLDB")

sql = """CREATE TABLE DELLDB(
   SNO MEDIUMINT NOT NULL AUTO_INCREMENT,
   commodity  VARCHAR(100)  NOT NULL,
   supplier VARCHAR(100)  NOT NULL,  
   Model_id VARCHAR(100) NOT NULL,
   price FLOAT NOT NULL,
   supplier_rating FLOAT NOT NULL,
   component_rating FLOAT NOT NULL,
   KEY(SNO)
   )"""

cursor.execute(sql)

with open('datafile.csv','r') as csvFile:
    csv_data = csv.reader(csvFile)
    for row in csv_data:
        row[2] = str(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = float(row[5])
        print(row)
        cursor.execute('INSERT INTO DELLDB(commodity,supplier,Model_id,price,supplier_rating,component_rating )' 'VALUES(%s, %s, %s, %s, %s,%s)', row)

db.commit()
db.close()



































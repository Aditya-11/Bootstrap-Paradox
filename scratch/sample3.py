def get_title(url):
  ctr = 0
  for i in range(len(url)):
    if url[i] == "/":
      ctr +=1
    if ctr ==3:
      url_new = url[i+1:]
      break
  for j in range(len(url_new)):
    if url_new[j] == "/":
      url_new = url_new[:j]
      break
  url_new.replace("-"," ")
  return url_new

url1 = get_title("https://www.amazon.com/MSI-GeForce-GTX-1080-GAMING/dp/B01HHBQBLG") 

print(url1)

import pymysql

con = pymysql.connect('localhost', 'root', 
    'password', 'DELL')

with con: 
    cur = con.cursor()
    #cur.execute('SELECT * FROM DELLDB WHERE SNO = "120"')
    #cur.execute('SELECT * FROM DELLDB WHERE SNO = 1')
    cur.execute('SELECT * FROM DELLDB ORDER BY SNO DESC LIMIT 3')
    rows = cur.fetchall()
    print(type(rows))
    for row in rows:
        print("{0} | {1} | {2} | {3} | {4}".format(row[0], row[1], row[2],row[3],row[4]))

import pandas as pd

cur.execute('SELECT * FROM DELLDB')

data = pd.read_sql('SELECT * FROM DELLDB', con=con)

print(data)

import numpy as np

data = data.iloc[:,1:]

budget = 1500
data['rating'] = abs(budget-data['price']) + (10-data['component_rating'])

priority_price = data.sort_values('price', ascending=True).drop_duplicates(['commodity'])
priority_supplier = data.sort_values('supplier_rating', ascending=False).drop_duplicates(['commodity'])
priority_component = data.sort_values('component_rating', ascending=False).drop_duplicates(['commodity'])

print(priority_component)
print(priority_price)
print(priority_supplier)















import pandas as pd
import numpy as np
import pymysql

con = pymysql.connect('localhost', 'root', 
    'password', 'DELL')

cur = con.cursor()

data = pd.read_sql('SELECT * FROM DELLDB', con=con)

#data = pd.read_csv('bom_final_data.csv')
data = data.iloc[:,1:]
"""
Choose case and sub_cases, 
"""
case = 1
sub = 1 # sub cases for case one
budget = 3 # sub cases for case two

"""
Case 1: If the priority is the best in a single feature
a. Lowest Price
b. Highest Supplier rating
c. Highest Commodity rating
"""
if case==1:
    if sub==1:
        case1_html = data.sort_values('price_in_dollars', ascending=True).drop_duplicates(['commodity'])
    elif sub==2:    
        case1_html = data.sort_values('supplier_rating', ascending=False).drop_duplicates(['commodity'])
    else:
        case1_html = data.sort_values('component_rating', ascending=False).drop_duplicates(['commodity'])


"""
Case 2: For a given budget range with supplier and component rating optimization
Four brackets : Below $1000, $1000 - $1500, $1500 - $2000, $2000 - $2500
"""
if case==2:
    if budget==1:
        priority_price_sup = data[(data['component_rating'] >= 6) & (data['supplier_rating'] >= 6)]
        case2_html = priority_price_sup.sort_values(['price_in_dollars','supplier_rating'], ascending=True).drop_duplicates(['commodity'])
    elif budget==2:
        priority_price_sup = data[(data['component_rating'] >= 7) & (data['supplier_rating'] >= 8)]
        case2_html = priority_price_sup.sort_values(['price_in_dollars','component_rating'], ascending=True).drop_duplicates(['commodity'])     
    elif budget==3:
         priority_price_sup = data[(data['component_rating'] >= 9) & (data['supplier_rating'] >= 6)]
         case2_html = priority_price_sup.sort_values(['price_in_dollars','component_rating'], ascending=False).drop_duplicates(['commodity'])
    else:
         priority_price_sup = data[(data['component_rating'] >= 8) & (data['supplier_rating'] >= 8)]
         case2_html = priority_price_sup.sort_values(['price_in_dollars','supplier_rating'], ascending=False).drop_duplicates(['commodity'])
        
print(case1_html['price_in_dollars'].sum())
print(case2_html['price_in_dollars'].sum())

case1_html.to_html('CASE1.html')
case2_html.to_html('CASE2.html')


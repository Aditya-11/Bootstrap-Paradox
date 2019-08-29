from flask import Flask , redirect , url_for , request , render_template
from flask_cors import CORS
import pymysql
import amazonscraper
import pandas as pd
import numpy as np
import pymysql

app = Flask(__name__, template_folder='templates')
CORS(app)

def foo(p):
    con = pymysql.connect('localhost', 'root', 
    'password', 'DELL')
    cur = con.cursor()
    cur.execute('SELECT * FROM DELLDB')
    data = pd.read_sql('SELECT * FROM DELLDB', con=con)

    #data = pd.read_csv('bom_data.csv')
    data = data.iloc[:,1:]

    #data = pd.read_csv('bom_final_data.csv')
    #data = data.iloc[:,1:]
    
    """
    Choose case and sub_cases, 
    """

    case = 1
    sub = p# sub cases for case one
    budget = 3 # sub cases for case two

    """
    Case 1: If the priority is the best in a single feature
    a. Lowest Price
    b. Highest Supplier rating
    c. Highest Commodity rating
    """
    if case==1:
        if sub==1:
           case1_html = data.sort_values('price', ascending=True).drop_duplicates(['commodity'])
           case1_html.to_html('./templates/CASE1.html')
        elif sub==2:    
            case1_html = data.sort_values('supplier_rating', ascending=False).drop_duplicates(['commodity'])
            case1_html.to_html('./templates/CASE1.html')
        else:
            case1_html = data.sort_values('component_rating', ascending=False).drop_duplicates(['commodity'])
            case1_html.to_html('./templates/CASE1.html')

    """
    Case 2: For a given budget range with supplier and component rating optimization
    Four brackets : Below $1000, $1000 - $1500, $1500 - $2000, $2000 - $2500
    """
    if case==2:
        if budget==1:
            priority_price_sup = data[(data['component_rating'] >= 6) & (data['supplier_rating'] >= 6)]
            case2_html = priority_price_sup.sort_values(['price','supplier_rating'], ascending=True).drop_duplicates(['commodity'])
            case2_html.to_html('./templates/CASE2.html')
        elif budget==2:
            priority_price_sup = data[(data['component_rating'] >= 7) & (data['supplier_rating'] >= 8)]
            case2_html = priority_price_sup.sort_values(['price','component_rating'], ascending=True).drop_duplicates(['commodity'])     
            case2_html.to_html('./templates/CASE2.html') 
        elif budget==3:
            priority_price_sup = data[(data['component_rating'] >= 9) & (data['supplier_rating'] >= 6)]
            case2_html = priority_price_sup.sort_values(['price','component_rating'], ascending=False).drop_duplicates(['commodity'])
            case2_html.to_html('./templates/CASE2.html')
        else:
            priority_price_sup = data[(data['component_rating'] >= 8) & (data['supplier_rating'] >= 8)]
            case2_html = priority_price_sup.sort_values(['price','supplier_rating'], ascending=False).drop_duplicates(['commodity'])
            case2_html.to_html('./templates/CASE2.html')

    #case1_html.to_html('./templates/CASE1.html')
    #case2_html.to_html('./templates/CASE2.html')

    if(case==1):
        return 'CASE1.html'
    elif(case==2):
        return 'CASE2.html'
    

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

def pipe_to_db(component,supply1,code_no,prices1,supply_rate1,component_rate1):
    """
    row = []
    row.append(component)
    row.append(supply1)
    row.append(code_no)
    row.append(prices1)
    row.append(supply_rate1)
    row.append(component)
    """
    db = pymysql.connect("localhost","root","password","DELL")
    cursor = db.cursor()
    cursor.execute("""INSERT INTO DELLDB (commodity, supplier, Model_id, price,supplier_rating, component_rating) VALUES ("%s", "%s", "%s", "%s" , "%s" , "%s")""" % (component, supply1, code_no, prices1,supply_rate1,component_rate1))
    #cursor.execute('SELECT * FROM DELLDB ORDER BY SNO DESC LIMIT 3')
    #nested_data = cursor.fetchall()
    db.commit()
    db.close()

    print("!Finish")

@app.route('/priority')
def priority():
    return render_template('priority_price.html')


@app.route('/index1')
def scrap():
    return render_template('index1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/posting',methods = ['POST'])
def posting():
    if request.method == 'POST':
        component = str(request.form['component'])
        product = str(request.form['product'])
        search  = int(request.form['max'])

        print(component)
        print(product)
        print(search)

        try:
            results = amazonscraper.search(product,max_product_nb = search)
        except Exception as e :
            print(e)

        if results is None: 
            print("over")
            return 0

        for result in results:
            code_no = None
            if result.asin is None:
                code_no = '123456'
            else:
                code_no = result.asin

            supply_rate1 = result.rating
            component_rate1 = ((result.rating)/(result.rating+1)) * supply_rate1
            price1 = result.prices_main
            supply1 = get_title(result.url)
            #print(s)
            print(supply_rate1,component_rate1,price1,supply1,component,code_no)
            pipe_to_db(component,supply1,code_no,price1,supply_rate1,component_rate1)

            db = pymysql.connect("localhost","root","password","DELL")
            cursor = db.cursor()
            cursor.execute('SELECT * FROM DELLDB ORDER BY SNO DESC LIMIT 10')
            nested_data = cursor.fetchall()
            #db.commit()
            db.close()
        
        #return render_template('index.html') 
        return render_template('index2.html',nested_data = nested_data)


@app.route('/query/')
def bar():
    price = request.args.get('price')
    p1 = request.args.get('p1') 
    p2 = request.args.get('p2')
    x = ''
    # print(price)
    # print(type(p1))
    # print(type(p2))
    if(price):
        price = int(price)
        x = foo(price)
    elif(p1):
        p1 = int(p1)
        x = foo(p1)
    elif(p2):
        p2 = int(p2)
        x = foo(p2)
    return render_template(x)

if __name__ == '__main__':
    app.run('0.0.0.0',debug = True)



























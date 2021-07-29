from flask import Flask, render_template, request, flash, url_for  
from flask_wtf import FlaskForm
import os 
import mysql.connector
import json

mydb = mysql.connector.connect(
    host = "localhost",
    user = "unisem",
    password = "unisem123",
    database = "unisem_inventory_1"
)

myCursor = mydb.cursor()

def msqlFetch(id):
    print("ID: ",id)
    sql = "SELECT * from components_list WHERE BinNo="+str(id)
    myCursor.execute(sql)
    result = myCursor.fetchall()
    return result



app = Flask(__name__)  
app.secret_key = 'development key'  
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/popup')
def popup():
    return render_template('popup.html')

@app.route('/get-coordinates', methods=['GET', 'POST'])
def thisRoute():
    information = request.data
    information = str(information,'utf-8')
    result = msqlFetch(information)
    jsonResult = json.dumps(result)
    print(jsonResult)
    print(type(jsonResult))
    return "jsonResult"

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.6')
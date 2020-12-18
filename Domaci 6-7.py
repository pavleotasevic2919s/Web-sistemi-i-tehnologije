from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "wsitdomaci",
	
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'

# client = MongoClient("mongodb+srv://admin:admin@cluster0-ixnru.mongodb.net/test?retryWrites=true&w=majority")

@app.route('/')
@app.route('/index')
def index():

	sve = mydb.cursor()
	sve.execute("SELECT * FROM raspored")
	res = sve.fetchall()
	print(res)

	prvi = mydb.cursor()
	prvi.execute("SELECT DISTINCT nastavnik FROM raspored")
	resPrvi = prvi.fetchall()

	drugi = mydb.cursor()
	drugi.execute("SELECT DISTINCT vreme FROM raspored")
	resDrugi = drugi.fetchall()

	return render_template('index.html', raspored = res,prvi=resPrvi, drugi=resDrugi)



if __name__ == '__main__':
	app.run(debug=True)

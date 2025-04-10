from flask import Flask 
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from dbCode import *

app = Flask(__name__)

#-------------------
# Route Home Page
#-------------------


@app.route('/')
def homepage():
    listings = get_top_listings()
    return render_template('index.html', results=listings)





# these two lines of code should always be the last in the file

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True)
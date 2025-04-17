from flask import Flask 
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from dbCode import *
from dynamoCode import *

app = Flask(__name__)

#-------------------
# Route Home Page
#-------------------


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        user = get_user(username)
        
        if user:
            # tells the user that the username they entered is already taken 
            return render_template("signup.html", message="Username already taken.")

        user_data = {
            "username": username,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": request.form["password"]
        }

        create_user(user_data)
        return redirect(url_for("listings"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user(username)

        if user and user.get("password") == password:
            return redirect(url_for("listings"))
        else:
            # Instead of flash, just pass a message directly to the template
            return render_template("login.html", message="Invalid login. Try again.")
    return render_template("login.html")

@app.route("/listings")
def listings():
    listings_data = get_all_listings()
    return render_template("listings.html", listings=listings_data)



# these two lines of code should always be the last in the file

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)

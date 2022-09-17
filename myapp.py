from crypt import methods
from flask import Flask,render_template, request
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("reservation.html")

@app.route("/", methods = ["POST"])
def reservation():
    name = request.form["Name"]
    surename = request.form["Surename"]
    email = request.form["Email"]
    num = request.form["People"]
    date = request.form["Date"]
    connection = sqlite3.connect(currentdirectory + "\Reservation")
    cursor = connection.cursor()
    query = "INSERT INTO Reservation VALUES '{n}', '{sn}', '{ml}', {nm}, {date})".format(n = name, sn = surename, ml = email, nm = num, date = date)
    cursor.execute(query1)
    connection.commit()
 

    

if __name__ == "__main__":
    app.run()
    
from flask import Flask,render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from email.message import Message
import sqlite3 as sql



app = Flask(__name__)

#osposobljavanje baze 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation.db'
#secret key
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize
db = SQLAlchemy(app)


class reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.LargeBinary, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    people = db.Column(db.Integer, nullable=False)
    
    def __init__(self, date, name, surname, email, people):
        self.date = date
        self.name = name
        self.surname = surname
        self.email = email
        self.people = people  


#rute
@app.route('/')
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/meni/')
def meni():
    return render_template('meni.html')

@app.route('/reservation/')
def reservation():
    return render_template('reservation.html')

@app.route('/shop/')
def shop():
    return render_template('shop.html')


#slanje emaila nakon prijave na newsletter
@app.route("/index", methods=["POST"])
def send_message_from_index_page():
    name = request.form.get("name")
    email = request.form.get("email")
    email_name=Message("Newsletter subscription", sender=email, recipients=["babicdaria1@gmail.com"])
    email_name.body=("Thank you for subscribing to our newsletter. By subscribing, You will be receiving discount codes and updates about our special events.")
    
    email.send(email_name)
    success_statement="Thank you!"
    return render_template("index.html", success_statement=success_statement)
    
app.testing=False 

@app.route('/reservation/', methods=['POST'])
def confirm():
    
    res = reservation(date, name, surname, email, people)
    db.session.add(res)
    db.session.commit()
    
    return render_template("reservedform.html")
    


if __name__ == "__main__":
    app.run(debug=True)

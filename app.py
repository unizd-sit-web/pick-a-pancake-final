import email
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
import sqlite3
from flask_mail import Mail, Message

app = Flask(__name__)

#email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'pickapancake1@gmail.com'
app.config['MAIL_PASSWORD'] = 'Web@1mail'
mail = Mail(app)

#newsletter form
@app.route('/newsletter', methods=[ 'GET', 'POST'])
def newsletter():
    if request.method == 'GET':
        return '<form action="/" method="POST"><input name="name" placeholder="Name"><input name="email" placeholder="E-mail"><input type="submit"></form>'
    
    email = request.form['email']
    msg = Message('Confirm email', sender='pickapancake1@gmail.com', recipients=[email])
    msg.body = 'You have successfully suscribed to our newsletter!'
    mail.send(msg)
    return render_template('newsletter.html')


#database
connection=sqlite3.connect("reservation.db")
cursor = connection.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation.db'
#secret key
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize
db = SQLAlchemy(app)

#creating database
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    quantitiy = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date)
    
    def __init__(self, name, surname, email, quantity, date):
        self.name = name
        self.surname = surname
        self.email = email
        self.quantitiy = quantity
        self.date = date


#routes
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

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

#reservation form
@app.route('/reservedform/', methods=["POST"])
def reservedform():
    name = request.form.get("name")
    surname = request.form.get ("surname")
    email = request.form.get ("email")
    quantity = request.form.get("people")
    date = request.form.get("date")
    
    res = Reservation(name, surname, quantity, email, date)
    db.session.add(res)
    db.session.commit()

    
    return render_template ('reservedform.html')

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

from email.policy import default
from wsgiref.validate import validator
from flask import Flask,render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from email.message import Message


app = Flask(__name__)

#osposobljavanje baze 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation.db'
#secret key
app.config['SECRET_KEY'] = "secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize
db = SQLAlchemy(app)


class reservations(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.String(10), nullable=False)
    table_mark=db.Column(db.String(10), nullable=False)
    name=db.Column(db.String(60), nullable=False)
    email=db.Column(db.String(60), nullable=False)

@app.route("/reservation", methods=["POST"])
def table_reservation():
    name=request.form.get("name")
    surname=request.form.get("surname")
    date=request.form.get("date")
    table_mark=request.form.get("table_mark")
    email_res=request.form.get("email_res")
    unique=False
    return render_template("reservation.html")

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

'''@app.route('/form/', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    return render_template ('form.html')'''

#slanje emaila nakon prijave na newsletter
@app.route("/index", methods=["POST"])
def send_message_from_index_page():
    name = request.form.get("first_name")
    email = request.form.get("email")
    email_name=Message("Newsletter subscription", sender=email, recipients=["babicdaria1@gmail.com"])
    email_name.body=("Thank you for subscribing to our newsletter. By subscribing, You will be receiving discount codes and updates about our special events.")
    
    email.send(email_name)
    success_statement="Thank you!"
    return render_template("index.html", success_statement=success_statement)
    
app.testing=False 

@app.route('/reservedform/', methods=["POST"])
def reservedform():
    first_name = request.form.get("Name")
    surname = request.form.get ("Surname")
    quantitiy = request.form.get ("Number of people")
    email = request.form.get("E-mail")
    return render_template ('reservedform.html')
    submit = SubmitField("submit")


if __name__ == "__main__":
    app.run(debug=True)

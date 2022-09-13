
from turtle import title
from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'pan cake'


@app.route('/', methods=['get'])
def index():
    title = "Pick a Pancake"
    return render_template('index.html', title=title)

@app.route('/index.html/')
def redir():
    return redirect('/')

@app.route('/about/')
def about():
    title = "About us"
    return render_template('about.html', title=title)

@app.route('/menu/')
def menu():
    title = "Menu"
    return render_template('menu.html', title=title)

@app.route('/reservation/')
def reservation():
    title = "Reservation"
    return render_template('reservation.html', title=title)

@app.route('/shop/')
def shop():
    title = "Shop"
    return render_template('shop.html', title=title)

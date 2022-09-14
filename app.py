from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
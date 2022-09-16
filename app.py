from flask import Flask, render_template, request


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

@app.route('/form/', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    return render_template ('form.html')

@app.route('/reservedform/', methods=["POST"])
def reservedform():
    first_name = request.form.get("name")
    surename = request.form.get ("surename")
    quantitiy = request.form.get ("quantity")
    email = request.form.get("email")
    return render_template ('reservedform.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/philosophy')
@app.route('/zen')
def zen():
    return render_template("zen.html")
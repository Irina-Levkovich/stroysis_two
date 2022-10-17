from flask import Flask, request, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/jcb')
def jcb():
    return render_template("JCB.html")



@app.route('/house')
def house():
    return render_template("house.html")



@app.route('/beton')
def beton():
    return render_template("beton.html")



@app.route('/exkavator')
def exkavator():
    return render_template("exkavator.html")


@app.route('/price')
def price():
    return render_template("price.html")


@app.route('/test')
def test():
    return render_template("test.html")



if __name__ == '__main__':
    app.run(debug=True)
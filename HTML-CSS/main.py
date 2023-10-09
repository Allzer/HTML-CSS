import sqlite3
import os
from flask import Flask, render_template, request, g

#Конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'rjffkjbdskf,1735'

app = Flask(__name__)


#обработчик главной страницы сайта

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/featback")
def feadback():
    return render_template("featback.html")

if __name__ == "__main__":
    app.run(debug=True)
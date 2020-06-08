from flask import Flask, render_template, jsonify
from swapi_consumer import Swapi
import views
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/people")
def people():
    return views.people()


@app.route("/starships")
def starships():
    return views.starships()

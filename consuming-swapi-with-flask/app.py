from flask import Flask, render_template, jsonify, request
from swapi_consumer import Swapi
import views
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/people", methods=['GET', 'POST'])
def people():
    return views.people(request)


@app.route("/starships")
def starships():
    return views.starships()

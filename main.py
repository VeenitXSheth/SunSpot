from sunmodel import getSunPos
from app import main
from sunmodel import update_avg_degree, get_month_range

# Import Meteostat library and dependencies
from flask import Flask, render_template, request, make_response, redirect
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gfg', methods=['POST'])
def gfg():

    inputCity = request.form.get('city')
    print(inputCity)

    x = main(inputCity)
    
    return render_template('index.html', optimal_rotation=f"{update_avg_degree()}°", optimal_times=get_month_range(x[0]), lat=x[1], long=x[2], city=x[3])



app.run(host="0.0.0.0", port=80)

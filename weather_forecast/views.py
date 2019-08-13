from flask import render_template, request
import requests
from weather_forecast import app
from .forms import LocationForm


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form['location']
        url = u"http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ea3e4ab8dc7a6ff89fc800753ce9c2c3".format(location)
        r = requests.get(url).json()

        context = {
            'location': location,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'image': r['weather'][0]['icon'],
        }
        return render_template('result.html', context=context)

    form = LocationForm()
    return render_template('home.html', form=form)

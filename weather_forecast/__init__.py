from flask import Flask
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('DJANGO_SECRET_KEY')

from weather_forecast import views

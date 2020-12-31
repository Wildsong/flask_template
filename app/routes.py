from flask import render_template, redirect, flash
from app import app
#from app.forms import CasesForm
from config import Config

import os
#from arcgis.gis import GIS
#from arcgis.features import FeatureLayer
#import pandas as pd

from datetime import datetime
#from pytz import timezone
#from tzlocal import get_localzone
#from utils import local2utc

VERSION = 'flask template 1.0'

portal_url      = Config.PORTAL_URL
portal_user     = Config.PORTAL_USER
portal_password = Config.PORTAL_PASSWORD
table_url       = Config.TABLE_URL

# This will prevent the app from starting
# if it's missing required environment settings.
assert portal_url
assert portal_user
assert portal_password
assert table_url

county_centroid = {"x": -123.74, "y": 46.09}
time_format = "%m/%d/%Y %H:%M"
error = "ERROR 99999"

def parsetime(s) :
    """ Parse a time string and return a datetime object. """
    return datetime.strptime(s, time_format)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')

# That's all!

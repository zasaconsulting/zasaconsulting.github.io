# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:17:57 2020

@author: ale
"""
import fileinput
import sys
import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt
#%matplotlib qt
from urllib.request import urlopen
import json
import plotly.express as px 
import pandas as pd
import requests 
import plotly.graph_objects as go
from plotly.offline import plot
from datetime import date


while True:
     try:
         geoprov = 'C:/Users/ale/OneDrive/Ale/COVID/dash_project_italy/limits_IT_provinces.json'
         f = open(geoprov, 'r')
         break
     except OSError as err:
        geoprov = 'C:/Users/alema/OneDrive/Ale/COVID/dash_project_italy/limits_IT_provinces.json'
        f = open(geoprov, 'r')
        break
        
     
with f as response:
    geo = json.load(response)

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M")    
tc = 'COVID-19 Epidemy in Italy - last update ' + dt


def job():
    print("Start job")  
#filedata = 'C:/Users/ale/OneDrive/Ale/COVID/grafici/dpc-covid19-ita-province-latest.csv'
    filedata = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-latest.csv"
    df = pd.read_csv(filedata,dtype={"sigla_provincia": str},error_bad_lines=True)
    fig1 = px.choropleth_mapbox(df, geojson=geo, color="totale_casi",
                               locations="sigla_provincia", featureidkey="properties.prov_acr",
                               center={"lat": 42.35, "lon": 12.70},
                               mapbox_style="carto-positron", zoom=5.5,
                               labels={'totale_casi':'confirmed cases'}
                               )
    fig1.update_layout(title_text= tc,
                       margin={"r":0,"t":100,"l":0,"b":0},
                       autosize=True,
                       width=1000, height=1100)
    #plot(fig1)
    fig1.show()
    plot(fig1, filename = 'index.html')

job()


# from apscheduler.schedulers.blocking import BlockingScheduler

# scheduler = BlockingScheduler()
# sched.add_job(job_function, 'cron', hour=18, minute=26)
# scheduler.start()
# scheduler.shutdown()
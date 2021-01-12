# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:06:08 2020

@author: Ksenia Mukhina
"""
import streamlit as st
import pandas as pd
import pydeck as pdk
import datetime
from dateutil.relativedelta import relativedelta
import json

folder = 'data/'   
museums = {
    'Hermitage Museum, Saint Petersburg, Russia':0,
    'Museum of Modern Art (MoMA), New York, USA':0,
    'Louvre, Paris, France':0,
    'British Museum, London, UK':0,
    'Museo Nacional del Prado, Spain':0,
    'Louvre-Lens, Lille, France':0,
    'Louvre Abu Dhabi, United Arab Emirates':0,
    'Museum of Contemporary Art, Los Angeles, USA':0,
    'National Palace Museum, Taipei':0,
    'Dallas Museum of Art, Dallas, USA':0,
    'Vatican Museums, Vatican':0,
    'Garage Museum of Contemporary Art, Moscow, Russia':0,
 } 

def date_range():
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2020, 1, 1)
    
    rang = [start]
    while start < end:
        start += relativedelta(months=1)
        rang.append(start)
        
    return rang
          
@st.cache
def load_data(city):
    map_data = pd.read_csv(folder + city + '-filtered.csv')
    map_data.columns =[x.lower() for x in map_data.columns]
    
    return map_data

def main():
    main_area = st.empty()    
    main_window(main_area)
    
def main_window(area):
    with open(folder + 'museums-wiki.json', 'r') as f:
        museum_info = json.load(f) 
        
    st.title('Museums')
    
    option = st.selectbox(
            'Select museum',
             list(museums.keys()))
    

    col1, col2 = st.beta_columns(2)
    
    col1.write(museum_info[option]['summary'])
    col2.image(museum_info[option]['img_link'])

if __name__ == "__main__":
    main()
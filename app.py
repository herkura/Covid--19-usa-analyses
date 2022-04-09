import pandas as pd
import streamlit as st
import warnings
import folium as fo

warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Covid Analysis')
st.subheader('This is a type of geospatial analysis where I have used folium library to plot that data onto the usa map.')
path = "johns-hopkins-covid-19-daily-dashboard-cases.csv"
dataFrame = pd.read_csv(path)

st.markdown('This data-set is dated for 21/05/2020 and the analysis was also done on this date.')

#total null values in the dataset
dataFrame.isnull().sum()



dataFrame.dropna(subset=['province_state','lat','long','admin2','fips','incident_rate','iso3'],axis=0,inplace=True)
dataFrame.drop(columns=['people_tested','people_hospitalized'])
st.subheader('Brief description of the data')
st.text(dataFrame.describe(include=['object']))

lat_usa=39.381266
lng_usa= -97.922211

# creating a map and displaying it
usa_map = fo.Map(location=[lat_usa , lng_usa],zoom_start=4,zoom_control=False,scrollWheelZoom=False,
               dragging=False)

#superimposing the data with the map
st.subheader('Cases allover the United States🦠🦠')
cases = fo.map.FeatureGroup()
for lat,lng in zip(dataFrame.lat,dataFrame.long):
    cases.add_child( fo.features.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )
      
map1_covid = usa_map.add_child(cases)
map1_covid

st.subheader('Statewise Cases')

from folium import plugins
map1_covid = fo.Map(location=[lat_usa , lng_usa],zoom_start=4,zoom_control=False,scrollWheelZoom=False,
               dragging=False)
cases =  plugins.MarkerCluster().add_to(map1_covid)
for lat,lng in zip(dataFrame.lat,dataFrame.long):
    fo.Marker(
    location=[lat,lng],
    icon=None,
    
    ).add_to(cases)
map1_covid

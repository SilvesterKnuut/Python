# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:57:53 2019

@author: Silvester
"""

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
"""WORKING WITH LISTS IS FASTER THAN WORKING WITH DATAFRAME OBJECTS"""
lat = list(data["LAT"])
lon = list(data["LON"])
v_name = list(data["NAME"])
stat = list (data["STATUS"])
typ = list (data["TYPE"])
elev = list (data["ELEV"])

def marker_colour(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 2000:
        return 'orange'
    elif 2000 < elevation < 3000:
        return 'red'
    else:
        return 'darkpurple'

html_1 = """<h4>Volcano information:</h4>
Name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>Status: %s
<br>Type: %s
<br>Elevation: %s
"""

map = folium.Map(location=[39.26,-102.12], zoom_start=5, tiles="OpenStreetMap")

fg_volcanos = folium.FeatureGroup(name="Volcanos")

for latitude, longitude, elevation, volcanoe_name, status, volcanoe_type in zip(lat, lon, elev, v_name, stat, typ):
    
    iframe_1 = folium.IFrame(html = html_1 % (volcanoe_name+ " volcano USA", volcanoe_name, 
                                        str(status), str(volcanoe_type), str(elevation)), width=210, height=130)
    
    fg_volcanos.add_child(folium.Marker(location=[latitude, longitude], popup=folium.Popup(iframe_1), 
                               icon=folium.Icon(marker_colour(elevation))))
   
fg_population = folium.FeatureGroup(name="Population")    
    
fg_population.add_child(folium.GeoJson(data=open('world.json','r',encoding='UTF-8-SIG').read(), 
style_function = lambda x: { 'fillColor': 'black' if x['properties']['POP2005'] > 300000000 
                            else 'purple' if 300000000 > x['properties']['POP2005'] > 150000000 
                            else 'red' if 150000000 > x['properties']['POP2005'] > 50000000
                            else 'green'}))

map.add_child(fg_volcanos)
map.add_child(fg_population)

map.add_child(folium.LayerControl(position='bottomleft'))

map.save("Volcanoe_Map.html")



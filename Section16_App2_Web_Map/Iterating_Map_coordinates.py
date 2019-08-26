# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import folium
"""create a map"""

map = folium.Map(location=[59.4370,24.7536], zoom_start=13, tiles="OpenStreetMap")

"""Adding elements to the map"""

"""create a feature group, fyi: marker is a feature and this will allow to switch layers on and off"""

fg = folium.FeatureGroup(name="MyMap")

for coordinates in [[59.3935,24.6660],[59.450137, 24.688835]]:

    fg.add_child(folium.Marker(location=coordinates, popup="Im a Marker !! yaya !!", icon=folium.Icon('blue')))

map.add_child(fg)

map.save("Map_Tallinn.html")

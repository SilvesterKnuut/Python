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

fg_myMap = folium.FeatureGroup(name="MyPlaces")

fg_myMap.add_child(folium.Marker(location=[59.3935, 24.6660], popup="Shahl6kki!", icon=folium.Icon('blue')))
fg_myMap.add_child(folium.Marker(location=[59.450137, 24.688835], popup="MyHome", icon=folium.Icon('blue')))

map.add_child(fg_myMap)

map.add_child(folium.LayerControl(position='bottomleft'))

map.save("Map_Tallinn.html")


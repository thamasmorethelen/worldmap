import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

data = pandas.read_csv('world_map_data/Volcanoes.txt')

lat = list(data["LAT"])
lon = list(data['LON'])
name = list(data['NAME'])

for lt, ln, name in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color='green')))


map.add_child(fg)
map.save('Map1.html')

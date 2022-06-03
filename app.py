import folium
import pandas


def to_feet(listy):
    ls = []
    item = ''
    for i in listy:
        item = i * 3.28084
        item = round(item, 2)
        ls.append(item)
    return ls


def map():
    map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")
    return map


map = map()


def make_map():
    fg = folium.FeatureGroup(name="My Map")

    data = pandas.read_csv('world_map_data/Volcanoes.txt')
    name = list(data['NAME'])
    elev = to_feet(list(data['ELEV']))
    tipe = list(data['TYPE'])
    lat = list(data["LAT"])
    lon = list(data['LON'])
    
    for lt, ln, name, elev, tipe in zip(lat, lon, name, elev, tipe):
        fg.add_child(folium.Marker(location=[lt, ln], popup=f'Name: {name} \nType: {tipe} \nElevation: {elev} feet', icon=folium.Icon(color='green')))
    map.add_child(fg)
    map.save('Map1.html')
    return map


make_map()

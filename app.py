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
    map = folium.Map(location=[41.984812, -117.344886], zoom_start=6, titles="Stamen Terrain", min_zoom='3', max_zoom='10',)
    return map


map = map()


def make_map():
    fg = folium.FeatureGroup(name="My Map")
    data = pandas.read_csv("world_map_data/Volcanoes.txt")
    html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s feet<br>
    Type: %s
    """
    name = list(data['NAME'])
    elev = to_feet(list(data['ELEV']))
    tipe = list(data['TYPE'])
    lat = list(data["LAT"])
    lon = list(data['LON'])




    for lt, ln, name, elev, tipe in zip(lat, lon, name, elev, tipe):
        iframe = folium.IFrame(html=html % (name, name, elev, tipe), width=200, height=100)
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))
    map.add_child(fg)
    map.save("Map_html_popup_advanced.html")
    return map


if __name__ == '__main__':
    make_map()

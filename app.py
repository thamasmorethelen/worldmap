import folium
import pandas


def to_feet(listy):
    ls = []
    item = ''
    for i in listy:
        item = i * 3.28084
        item = round(item)
        ls.append(item)
    return ls


def icon_color(elev):
    if elev < 3280.84:
        return 'green'
    if elev > 3280.84 and elev < 9842.52:
        return 'orange'
    if elev > 9842.52:
        return 'red'



def map():
    map = folium.Map(location=[41.984812, -117.344886], zoom_start=6, titles="Stamen Terrain", min_zoom='3', max_zoom='10',)
    return map


map = map()


def make_map():
    fgv = folium.FeatureGroup(name="Volcanos")
    data = pandas.read_csv("world_map_data/Volcanoes.txt")
    html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
    Height: %s feet<br>
    Type: <a href="https://www.google.com/search?q=%s&oq=Lava+domes&aqs=chrome.0.0i512l10.542j0j7&sourceid=chrome&ie=UTF-8" target="_blank">%s<a>
    """
    name = list(data['NAME'])
    elev = to_feet(list(data['ELEV']))
    tipe = list(data['TYPE'])
    lat = list(data["LAT"])
    lon = list(data['LON'])

    for lt, ln, name, elev, tipe in zip(lat, lon, name, elev, tipe):
        iframe = folium.IFrame(html=html % (name, name, elev, tipe, tipe), width=200, height=100)
        fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=icon_color(elev))))
    fgpop = folium.FeatureGroup(name='Population')
    fgpop.add_child(folium.GeoJson(data=open('world_map_data/world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: 
    {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 200000000 >= x['properties']['POP2005'] < 1000000000 else 'red'}))
    map.add_child(fgv)
    map.add_child(fgpop)
    map.add_child(folium.LayerControl())
    map.save("Map_html_popup_advanced.html")
    return map


if __name__ == '__main__':
    make_map()

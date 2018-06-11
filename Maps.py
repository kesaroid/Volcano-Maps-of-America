import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
elev = list(data['ELEV'])

def icons(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 2000:
        return 'orange'
    elif 2000 <= el < 3000:
        return 'yellow'
    else:
        return 'blue'

map = folium.Map(location = [40.815697, -103.086074], zoom_start = 4)

for i, j, k, el in zip(lat,lon,name, elev):
    map.add_child(folium.Marker(location=[i, j], popup = folium.Popup(str(k), parse_html = True), icon = folium.Icon(color = icons(el))))

map.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()))

map.save("Map.html")

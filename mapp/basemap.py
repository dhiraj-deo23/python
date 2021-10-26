import folium
import pandas
# import csv

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
location = list(data['LOCATION'])
name = list(data['NAME'])
m = folium.Map(location=[lat[0], lon[0]],
               zoom_start=6)
folium.TileLayer("Stamen Terrain").add_to(m)
# with open("Volcanoes.txt", "r") as file:
#     csv_reader = csv.DictReader(file, delimiter=",")
#     lat = []
#     lon = []
#     for row in csv_reader:
#         lat.append(row['LAT'])
#         lon.append(row['LON'])
fgv = folium.FeatureGroup("Volcanoes")
fgp = folium.FeatureGroup("Population")

for lt, ln, lc, nm in zip(lat, lon, location, name):
    fgv.add_child(folium.Marker(
        location=[lt, ln], tooltip=nm + '-' + lc, icon=folium.Icon(color='green')))
m.add_child(fgv)

fgp.add_child(folium.GeoJson(
    data=(open("world.json", "r", encoding='utf-8-sig').read()), style_function=lambda x: {"fillColor": "	#008000" if x['properties']['POP2005'] < 10000000 else "#FFA500" if 10000000 > x['properties']['POP2005'] < 20000000 else "red"}))
m.add_child(fgp)
m.add_child(folium.LayerControl())


m.save("map.html")

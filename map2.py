import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
name = list(data.NAME)
elev = list(data.ELEV)

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup("My Map2")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup="{}, {} m".format(nm, el), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map2.html")
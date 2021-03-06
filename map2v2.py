import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data.LAT)
lon = list(data.LON)
name = list(data.NAME)
elev = list(data.ELEV)

html = """<h4>Volcano information:</h4>
Name: %s <br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup("My Map2")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (nm, str(el)), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map2V2.html")
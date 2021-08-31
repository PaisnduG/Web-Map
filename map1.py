import folium

map = folium.Map(location=[6.504066, 80.646809], zoom_start=15)

# Feature Group
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[6.500258, 80.665326], popup="This is my Home", icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("Map1.html")
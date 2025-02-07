import folium

# Create a map centered around Dubai
dubai_map = folium.Map(location=[25.2048, 55.2708], zoom_start=12)

# Add markers for each location
locations = [
    ("Burj Khalifa", 25.1972, 55.2744),
    ("Dubai Mall", 25.1986, 55.2794),
    ("Dubai Fountain", 25.1957, 55.2752),
    ("Jumeirah Beach", 25.2459, 55.2788),
    ("Souk Madinat Jumeirah", 25.1375, 55.1935),
    ("Dubai Creek", 25.2654, 55.3047),
    ("Al Fahidi Historical Neighborhood", 25.2639, 55.2974),
    ("Gold Souk", 25.2679, 55.3026),
    ("Spice Souk", 25.2687, 55.3014),
    ("Palm Jumeirah", 25.1207, 55.1353)
]

# Add markers to the map
for name, lat, lon in locations:
    folium.Marker([lat, lon], popup=name).add_to(dubai_map)

# Save the map to an HTML file
dubai_map.save('dubai_map.html')

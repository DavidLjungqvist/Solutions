import folium
from folium.plugins import TimestampedGeoJson

# m = folium.Map(location=[35.68159659061569, 139.76451516151428], zoom_start=16)
#
# points = [
#     {
#         "coordinates": [139.76451516151428, 35.68159659061569],
#         "time": "2004-01-01",
#         "color": "red",
#     },
#     {
#         "coordinates": [139.75964426994324, 35.682590062684206],
#         "time": "2015-01-01",
#         "color": "blue",
#     },
#     {
#         "coordinates": [139.7575843334198, 35.679505030038506],
#         "time": "2017-01-01",
#         "color": "green",
#         "weight": 15,
#     },
#     {
#         "coordinates": [139.76337790489197, 35.678040905014065],
#         "time": "2018-01-01",
#         "color": "#FFFFFF",
#     },
# ]
#
# features = [
#     {
#         "type": "Feature",
#         "geometry": {
#             "type": "Point",
#             # for Point, coordinates must be a single [lon, lat] pair, not a list of lists
#             "coordinates": p["coordinates"],
#         },
#         "properties": {
#             # for single points, use a single "time" value, not a "times" array
#             "time": p["time"],
#             "style": {
#                 "color": p["color"],
#             },
#         },
#     }
#     for p in points
# ]
#
# TimestampedGeoJson(
#     {
#         "type": "FeatureCollection",
#         "features": features,
#     },
#     period="P1Y",              # 1 year steps
#     date_options="YYYY-MM-DD", # display format
#     add_last_point=True,
#     auto_play=False,
#     loop=False,
# ).add_to(m)
#
# m.save("text.html")


m = folium.Map(location=[35.6816, 139.7645], zoom_start=16)

# Timeline expects a DataFrame-like structure
data = """
lon,lat,date,color
139.764515,35.681597,1800-01-01,red
139.759644,35.682590,1850-01-01,blue  
139.757584,35.679505,1900-01-01,green
139.763378,35.678041,1950-01-01,"#FFFFFF"
"""

df = pd.read_csv(pd.StringIO(data))  # or load your actual data

Timeline(
    data=df,
    time_col='date',           # your date column (ISO format)
    position_col='lat',        # latitude
    popup_col='color',         # optional popup info
    auto_play=True,
    loop=False,
    max_speed=10,
    add_last_point=True
).add_to(m)

m.save("timeline_1800s.html")

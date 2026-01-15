import folium
import pandas as pd
# from folium.plugins import TimestampedGeoJson
from folium.plugins.timeline import Timeline, TimelineSlider

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


m = folium.Map(location=[55, 10], zoom_start=5)


df = pd.read_csv("stations.csv")

features = [
    {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [row["lon"], row["lat"]]},
        "properties": {"Start Dato": f"{int(row['year'])}-01-01"},
    }
    for _, row in df.iterrows()
]

print(features)

timeline = Timeline(
    data=df,
    time_col='year',           # your date column (ISO format)
    position_col=['lat', 'lon'],    # optional popup info
    auto_play=True,
    loop=False,
    max_speed=10,
    add_last_point=True
).add_to(m)


m.save("timeline_test.html")

import folium
import pandas as pd
from folium.plugins import Timeline, TimelineSlider
from folium.utilities import JsCode
from folium.features import GeoJsonPopup

m = folium.Map(location=[55, 10], zoom_start=5)

# Load your stations.csv
df = pd.read_csv("stations.csv")

# Convert to Timeline GeoJSON format (each point gets start/end times)
features = []
for _, row in df.iterrows():
    # Create start/end as same year (or adjust end as needed)
    start_time = f"{int(row['year'])}-01-01"
    end_time = f"{int(row['year'])}-12-31"  # or same as start_time

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['lon'], row['lat']]  # [lon, lat] order!
        },
        "properties": {
            "start": start_time,
            "end": end_time,
            "name": f"Station {row.get('name', row.name)}"  # optional popup
        }
    }
    features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# Simple point style function (required)
point_style = JsCode("""
function (feature) {
    return {
        radius: 6,
        color: "#ff7800",
        weight: 2,
        fillColor: "#ff7800",
        fillOpacity: 0.7
    };
}
""")

# Create Timeline layer
timeline = Timeline(
    geojson_data,
    style=point_style
).add_to(m)

# Add popup info
GeoJsonPopup(fields=['name']).add_to(timeline)

# Add TimelineSlider control
TimelineSlider(
    auto_play=False,
    show_ticks=True,
    enable_keyboard_controls=True
).add_timelines(timeline).add_to(m)

m.save("stations_timeline.html")

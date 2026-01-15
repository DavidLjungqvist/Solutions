# import folium
# import pandas as pd
# from folium.plugins import Timeline, TimelineSlider
# from folium.utilities import JsCode
# from folium.features import GeoJsonPopup
#
# m = folium.Map(location=[55, 10], zoom_start=5)
#
# # Load your stations.csv
# df = pd.read_csv("stations.csv")
#
# # Convert to Timeline GeoJSON format (each point gets start/end times)
# features = []
# for _, row in df.iterrows():
#     # Create start/end as same year (or adjust end as needed)
#     start_time = f"{int(row['year'])}-01-01"
#     end_time = f"{int(row['year'])}-12-31"  # or same as start_time
#
#     feature = {
#         "type": "Feature",
#         "geometry": {
#             "type": "Point",
#             "coordinates": [row['lon'], row['lat']]  # [lon, lat] order!
#         },
#         "properties": {
#             "start": start_time,
#             "end": end_time,
#             "name": f"Station {row.get('name', row.name)}"  # optional popup
#         }
#     }
#     features.append(feature)
#
# geojson_data = {
#     "type": "FeatureCollection",
#     "features": features
# }
#
# # Simple point style function (required)
# point_style = JsCode("""
# function (feature) {
#     return {
#         radius: 6,
#         color: "#ff7800",
#         weight: 2,
#         fillColor: "#ff7800",
#         fillOpacity: 0.7
#     };
# }
# """)
#
# # Create Timeline layer
# timeline = Timeline(
#     geojson_data,
#     style=point_style
# ).add_to(m)
#
# # Add popup info
# GeoJsonPopup(fields=['name']).add_to(timeline)
#
# # Add TimelineSlider control
# TimelineSlider(
#     auto_play=False,
#     show_ticks=True,
#     enable_keyboard_controls=True
# ).add_timelines(timeline).add_to(m)
#
# m.save("stations_timeline.html")


import folium
import pandas as pd
from folium.plugins import Timeline, TimelineSlider
from folium.utilities import JsCode

m = folium.Map(location=[55, 10], zoom_start=5)
df = pd.read_csv("stations.csv")

features = []
for _, row in df.iterrows():
    start_time = f"{int(row['year'])}-01-01"
    # Make end date far in future - points stay visible after appearing
    end_time = "2027-12-31"  # or "9999-12-31"

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['lon'], row['lat']]
        },
        "properties": {
            "start": start_time,
            "end": end_time,  # Stays visible until 2100+
            "name": f"Station {row.get('name', '')} - {row['year']}"
        }
    }
    features.append(feature)

geojson_data = {"type": "FeatureCollection", "features": features}

# Style for points
point_style = JsCode("""
function (feature) {
    return {
        radius: 6,
        color: "#3186cc",
        weight: 2,
        fillColor: "#ff7800",
        fillOpacity: 0.7
    };
}
""")

timeline = Timeline(
    geojson_data,
    style=point_style
).add_to(m)

TimelineSlider(
    auto_play=True,
    loop=True,  # Loops back to start
    show_ticks=True,
    playback_duration=30000
).add_timelines(timeline).add_to(m)

m.save("stations_persistent.html")

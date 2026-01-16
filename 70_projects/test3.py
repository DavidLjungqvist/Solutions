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
#

import folium
import pandas as pd
from folium.plugins import Timeline, TimelineSlider
from folium.utilities import JsCode
import requests
from io import StringIO

query = """
    SELECT ?station ?stationLabel ?lat ?lon ?openDate ?estDate #?endDate ?endDate2 ?endDate3
    WHERE {
        ?station wdt:P31/wdt:P279* wd:Q55488 ;
                 wdt:P17 wd:Q35;
             #    wdt:P131* wd:Q504125 ;
                 wdt:P625 ?coord ;
             #    wdt:P5817 wd:Q55654238 .
                 OPTIONAL { ?station wdt:P1619 ?openDate . }
                 OPTIONAL { ?station wdt:P571 ?estDate . }
              #   OPTIONAL { ?station wdt:P582 ?endDate . }
              #   OPTIONAL { ?station wdt:P576 ?endDate2 . }
              #   OPTIONAL { ?station wdt:P3999 ?endDate3 . }
    
    
      BIND(geof:latitude(?coord) AS ?lat)
      BIND(geof:longitude(?coord) AS ?lon)
    
        SERVICE wikibase:label {
          bd:serviceParam wikibase:language "en".
          }
    }
"""


url = "https://query.wikidata.org/sparql"

headers = {
    "Accept": "text/csv"
}

response = requests.get(
    url,
    params={"query": query},
    headers=headers
)

df = pd.read_csv(StringIO(response.text))
df.to_csv("stations2.csv", index=False)

m = folium.Map(location=[55, 10], zoom_start=6, tiles=None
               )

default_tiles = folium.TileLayer(
    tiles="OpenStreetMap",
    name="Default map",
    control=True
)

raw_tiles = folium.TileLayer(
    tiles="CartoDB Positron",
    name="Raw map",
    control=True
)
default_tiles.add_to(m)
raw_tiles.add_to(m)


df = pd.read_csv("stations2.csv")

df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
df["earliestDate"] = df[["openDate", "estDate"]].min(axis=1)
df.to_csv("stations3.csv", index=False)

stations_layer = folium.FeatureGroup(name="Railway stations", overlay=True)

features = []
for _, row in df.iterrows():
    start_time = row["earliestDate"].isoformat()
    # Make end date far in future - points stay visible after appearing
    end_time = "2030-01-01"  # or "9999-12-31"

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['lon'], row['lat']]
        },
        "properties": {
            "start": start_time,
            "end": end_time,
            "name": f"Station {row.get('name', '')} - {row['earliestDate']}"
        }
    }
    features.append(feature)


geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

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

# timeline = Timeline(
#     geojson_data,
#     style=point_style
# ).add_to(m)

# timeline = Timeline(
#     geojson_data,
#     point_to_layer=JsCode("""
#         function(feature, latlng) {
#             return L.marker(latlng, {
#                 icon: L.divIcon({
#                     className: 'station-icon',
#                     html: '🚉',
#                     iconSize: [20, 20],
#                     iconAnchor: [10, 10]
#                 })
#             });
#         }
#     """)
# ).add_to(m)

timeline = Timeline(
    geojson_data,
    point_to_layer=JsCode("""
        function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: 'station-icon',
                    html: '🚉',
                    iconSize: [20, 20],
                    iconAnchor: [10, 10]
                })
            });
        }
    """)
)

stations_layer.add_child(timeline)
stations_layer.add_to(m)


TimelineSlider(
    auto_play=True,
    loop=True,  # Loops back to start
    show_ticks=True,
    playback_duration=30000
).add_timelines(timeline).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)


m.save("stations_persistent3.html")

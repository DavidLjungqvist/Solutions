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

def get_wikidata_stations():
    # # nyeste query:
    station_query = """SELECT ?station ?stationLabel ?lat ?lon ?statusLabel
     ?trainServiceLabel ?openDate ?estDate ?endDate ?endDate2 ?endDate3
    WHERE {
      ?station wdt:P31/wdt:P279* wd:Q55488 ;
               wdt:P17 wd:Q35 ;
               wdt:P625 ?coord ;
               wdt:P5817 ?status .
    
      FILTER NOT EXISTS { ?station wdt:P31/wdt:P279* wd:Q28109487. }
      FILTER NOT EXISTS { ?station wdt:P31/wdt:P279* wd:Q928830. }
      FILTER NOT EXISTS { ?station wdt:P5817 wd:Q811683. }
      FILTER NOT EXISTS { ?station wdt:P5817 wd:Q12377751. }
      FILTER NOT EXISTS { ?station wdt:P5817 wd:Q55570340. }
    
      OPTIONAL { ?station wdt:P1192 ?trainService . }
      OPTIONAL { ?station wdt:P1619 ?openDate . }
      OPTIONAL { ?station wdt:P571  ?estDate . }
      OPTIONAL { ?station wdt:P582  ?endDate . }
      OPTIONAL { ?station wdt:P576  ?endDate2 . }
      OPTIONAL { ?station wdt:P3999 ?endDate3 . }
    
      BIND(geof:latitude(?coord)  AS ?lat)
      BIND(geof:longitude(?coord) AS ?lon)
    
      SERVICE wikibase:label {
        bd:serviceParam wikibase:language "da" .
      }
    }
    """
    url = "https://query.wikidata.org/sparql"
    headers = {
        "Accept": "text/csv"
    }

    response = requests.get(
        url,
        params={"query": station_query},
        headers=headers
    )

    df = pd.read_csv(StringIO(response.text))
    df.to_csv("stations5.csv", index=False)
    # station_query = """
    #     SELECT ?station ?stationLabel ?lat ?lon ?openDate ?estDate #?endDate ?endDate2 ?endDate3
    #     WHERE {
    #         ?station wdt:P31/wdt:P279* wd:Q55488 ;
    #                  wdt:P17 wd:Q35;
    #              #    wdt:P131* wd:Q504125 ;
    #                  wdt:P625 ?coord ;
    #              #    wdt:P5817 wd:Q55654238 .
    #                  OPTIONAL { ?station wdt:P1619 ?openDate . }
    #                  OPTIONAL { ?station wdt:P571 ?estDate . }
    #               #   OPTIONAL { ?station wdt:P582 ?endDate . }
    #               #   OPTIONAL { ?station wdt:P576 ?endDate2 . }
    #               #   OPTIONAL { ?station wdt:P3999 ?endDate3 . }
    #
    #
    #       BIND(geof:latitude(?coord) AS ?lat)
    #       BIND(geof:longitude(?coord) AS ?lon)
    #
    #         SERVICE wikibase:label {
    #           bd:serviceParam wikibase:language "en".
    #           }
    #     }
    # """
def get_wikidata_metro_stations():
    metro_station_query = """
        SELECT ?station ?stationLabel ?lat ?lon ?openDate ?estDate
        WHERE {
          ?station wdt:P31 wd:Q928830 ;
                   wdt:P17 wd:Q35 ;
                   wdt:P625 ?coord .
        
          OPTIONAL { ?station wdt:P1619 ?openDate . }
          OPTIONAL { ?station wdt:P571  ?estDate . }
        
          BIND(geof:latitude(?coord)  AS ?lat)
          BIND(geof:longitude(?coord) AS ?lon)
        
          SERVICE wikibase:label {
            bd:serviceParam wikibase:language "da" .
          }
        }
    """




    url = "https://query.wikidata.org/sparql"
    headers = {
        "Accept": "text/csv"
    }

    response = requests.get(
        url,
        params={"query": metro_station_query},
        headers=headers
    )

    df = pd.read_csv(StringIO(response.text))
    df.to_csv("stations5metro.csv", index=False)

def sort_df():
    df = pd.read_csv("stations5.csv")

    df = df.rename(columns={"stationLabel": "station_label"})


    df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
    df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
    df["earliest_date"] = df[["openDate", "estDate"]].min(axis=1)
    df["endDate"] = pd.to_datetime(df["endDate"], errors="coerce", utc=True)
    df["endDate2"] = pd.to_datetime(df["endDate2"], errors="coerce", utc=True)
    df["endDate3"] = pd.to_datetime(df["endDate3"], errors="coerce", utc=True)
    df["latest_date"] = df[["endDate", "endDate2", "endDate3"]].max(axis=1)
    df = df.drop(columns=["openDate", "estDate", "endDate", "endDate2", "endDate3"])
    df[["metro", "s_train", "regional", "intercity", "historic"]] = False
    df.loc[df["trainServiceLabel"].str.contains("Linje", case=False, na=False), "s_train"] = True
    df.loc[df["trainServiceLabel"].str.contains("L1|L2", case=False, na=False), "s_train"] = False
    df.loc[df["trainServiceLabel"].str.contains("Regionaltog", case=False, na=False), "regional"] = True
    df.loc[df["trainServiceLabel"].str.contains("Intercity", case=False, na=False), "intercity"] = True
    df.loc[df["trainServiceLabel"].str.contains("M1|M2|M3|M4|Cityringer", case=False, na=False), "metro"] = True
    df.loc[df["statusLabel"].str.contains("Q109551035", case=False, na=False), "historic"] = True
    df = df.drop(
        df[
            df["statusLabel"].str.contains("nedlagt", case=False, na=False)
            & df["latest_date"].isna()
        ].index
    )
    df = df.drop(columns=["statusLabel", "trainServiceLabel"])
### Merge Rows ###

    bool_cols = [
        "metro",
        "s_train",
        "regional",
        "intercity",
        "historic",
    ]

    other_cols = [
        "station_label",
        "lat",
        "lon",
        "earliest_date",
        "latest_date",
    ]

    dict1 = {c: "first" for c in other_cols}
    dict2 = {c: "any" for c in bool_cols}

    df_merged = (
        df
        .groupby("station", as_index=False)
        .agg({
            **{c: "first" for c in other_cols},
            **{c: "any" for c in bool_cols},
        })
    )



    # df.to_csv("stations4after.csv", index=False)
    df_merged.to_csv("stations5after.csv", index=False)

def sort_metro_df():

    df = pd.read_csv("stations5metro.csv")

    df = df.rename(columns={"stationLabel": "station_label"})
    df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
    df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
    df["earliest_date"] = df[["openDate", "estDate"]].min(axis=1)
    df = df.drop(columns=["openDate", "estDate"])
    df["latest_date"] = ""
    df["metro"] = True
    df[["s_train", "regional", "intercity", "historic"]] = False

    df.to_csv("stations5metroafter.csv", index=False)

def merge_df():
    df1 = pd.read_csv("stations5after.csv")
    df2 = pd.read_csv("stations5metroafter.csv")

    combined_df = pd.concat([df1, df2], ignore_index=True)
    combined_df = combined_df.dropna(subset=["earliest_date"])
    combined_df["latest_date"] = combined_df["latest_date"].fillna(pd.Timestamp("2030-01-01", tz="UTC"))

    combined_df.to_csv("combined_stations.csv", index=False)

def generate_map():
    m = folium.Map(location=[55, 10], zoom_start=6, tiles=None
                   )
    raw_tiles = folium.TileLayer(
        tiles="CartoDB Positron",
        name="Raw map",
        control=True
    )

    default_tiles = folium.TileLayer(
        tiles="OpenStreetMap",
        name="Default map",
        control=True
    )

    raw_tiles.add_to(m)
    default_tiles.add_to(m)

    #
    # df = pd.read_csv("stations2.csv")

    # df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
    # df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
    # df["earliestDate"] = df[["openDate", "estDate"]].min(axis=1)
    # df.to_csv("stations3.csv", index=False)

    df = pd.read_csv("combined_stations.csv")
    df["earliest_date"] = pd.to_datetime(df["earliest_date"], errors="coerce", utc=True)
    df["latest_date"] = pd.to_datetime(df["latest_date"], errors="coerce", utc=True)

    stations_layer = folium.FeatureGroup(name="Railway stations", overlay=True)

    features = []
    for _, row in df.iterrows():
        start_time = row["earliest_date"].isoformat()
        end_time = row["latest_date"].isoformat()
        # Make end date far in future - points stay visible after appearing

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row['lon'], row['lat']]
            },
            "properties": {
                "start": start_time,
                "end": end_time,
                "name": f"Station {row.get('name', '')} - {row['earliest_date']}"
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
        playback_duration=60000
    ).add_timelines(timeline).add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)


    m.save("stations_persistent4.html")

# get_wikidata_stations()
# get_wikidata_metro_stations()
sort_df()
# sort_metro_df()
# merge_df()
# generate_map()
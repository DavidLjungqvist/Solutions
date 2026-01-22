import folium
import pandas as pd
from folium.plugins import Timeline, TimelineSlider
from folium.utilities import JsCode
import requests
from io import StringIO


def get_wikidata_stations(): # Gets regular station data from wikidata and stores them as csv
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


def get_wikidata_metro_stations(): # Gets metro station data from wikidate and stores them as csv
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

def sort_df(): #
    df = pd.read_csv("stations5.csv")

    df = df.rename(columns={"stationLabel": "station_label"})

# def to_datetime():
    df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
    df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
    df["endDate"] = pd.to_datetime(df["endDate"], errors="coerce", utc=True)
    df["endDate2"] = pd.to_datetime(df["endDate2"], errors="coerce", utc=True)
    df["endDate3"] = pd.to_datetime(df["endDate3"], errors="coerce", utc=True)
    df["earliest_date"] = df[["openDate", "estDate"]].min(axis=1)
    df["latest_date"] = df[["endDate", "endDate2", "endDate3"]].max(axis=1)
    df = df.drop(columns=["openDate", "estDate", "endDate", "endDate2", "endDate3"])
    df[["metro", "s_train", "regional", "intercity", "historic"]] = False
    df.loc[df["trainServiceLabel"].str.contains("Linje", case=False, na=False), "s_train"] = True
    df.loc[df["trainServiceLabel"].str.contains("L1|L2", case=False, na=False), "s_train"] = False
    df.loc[df["trainServiceLabel"].str.contains("Regionaltog", case=False, na=False), "regional"] = True
    df.loc[df["trainServiceLabel"].str.contains("Intercity", case=False, na=False), "intercity"] = True
    df.loc[df["trainServiceLabel"].str.contains("M1|M2|M3|M4|Cityringer", case=False, na=False), "metro"] = True
    df.loc[df["statusLabel"].str.contains("Q109551035", case=False, na=False), "historic"] = True # Q109551035 = "partial use" but all stations are used for historical purposes as of 22-01-2026
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
    m = folium.Map(location=[55.575, 11], zoom_start=7, tiles=None
                   )
    # m.get_root().html.add_child(folium.Element("""
    # <script>
    # map.createPane('metro');
    # map.getPane('metro').style.zIndex = 400;
    #
    # map.createPane('generic');
    # map.getPane('generic').style.zIndex = 410;
    #
    # map.createPane('s_train');
    # map.getPane('s_train').style.zIndex = 500;
    #
    # map.createPane('regional');
    # map.getPane('regional').style.zIndex = 600;
    #
    # map.createPane('intercity');
    # map.getPane('intercity').style.zIndex = 700;
    # </script>
    # """))

    m.get_root().html.add_child(folium.Element("""
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        const map = window._leaflet_map || Object.values(window).find(
            v => v && v instanceof L.Map
        );

        if (!map) return;

        map.createPane('generic');
        map.getPane('generic').style.zIndex = 300;

        map.createPane('metro');
        map.getPane('metro').style.zIndex = 400;

        map.createPane('s_train');
        map.getPane('s_train').style.zIndex = 500;
        
        map.createPane('dummy');
        map.getPane('dummy').style.zIndex = 550;

        map.createPane('regional');
        map.getPane('regional').style.zIndex = 600;

        map.createPane('intercity');
        map.getPane('intercity').style.zIndex = 700;
        
        map.createPane('historic');
        map.getPane('intercity').style.zIndex = 800;
    });
    </script>
    """))

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

    df = pd.read_csv("combined_stations.csv")
    df["earliest_date"] = pd.to_datetime(df["earliest_date"], errors="coerce", utc=True)
    df["latest_date"] = pd.to_datetime(df["latest_date"], errors="coerce", utc=True)

    stations_layer = folium.FeatureGroup(name="Railway stations", overlay=True)

    # df_regional = df.loc[df["regional"] == True]
    #
    # print(df_regional["regional"][101:120])

    features = []
    for _, row in df.iterrows():
        start_time = row["earliest_date"].isoformat()
        end_time = row["latest_date"].isoformat()
        lon, lat = row["lon"], row["lat"]

        if row["metro"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "metro"
                }
            })
        if not row["metro"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "generic"
                }
            })
        if row["s_train"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "s_train"
                }
            })
        if True:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "dummy"
                }
            })
        if row["regional"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "regional"
                }
            })
        if row["intercity"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "intercity"
                }
            })
        if row["historic"]:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "start": start_time,
                    "end": end_time,
                    "layer": "historic"
                }
            })
        # else:
        #     features.append({
        #         "type": "Feature",
        #         "geometry": {
        #             "type": "Point",
        #             "coordinates": [lon, lat]
        #         },
        #         "properties": {
        #             "start": start_time,
        #             "end": end_time,
        #             "layer": "generic"
        #         }
        #     })


        # feature = {
        #     "type": "Feature",
        #     "geometry": {
        #         "type": "Point",
        #         "coordinates": [lon, lat]
        #     },
        #     "properties": {
        #         "start": start_time,
        #         "end": end_time,
        #         "name": f"Station {row.get('name', '')} - {row['earliest_date']}"
        #     }
        # }
        # features.append(feature)

    style_fn = JsCode("""
    function(feature, latlng)  {
    
    
        if (feature.properties.layer === "metro")  {
            return L.circleMarker(latlng,  {
                pane: "metro",
                radius: 9,
                color: "#606060",
                weight: 2,
                fillColor: "#ffffff",
                fillOpacity: 1
            });
        }
        
        if (feature.properties.layer === "generic")  {
            return L.circleMarker(latlng,  {
                pane: "generic",
                radius: 9,
                color: "#000000",
                weight: 1,
                fillColor: "#393939",
                fillOpacity: 1
            });
        }
        
        if (feature.properties.layer === "s_train")  {
            return L.circleMarker(latlng,  {
                pane: "s_train",
                radius: 6.5,
                color: "#ff2020",
                weight: 1,
                fillColor: "#ff0000",
                fillOpacity: 1
            });
        }
        if (feature.properties.layer === "regional")  {
            return L.circleMarker(latlng,  {
                pane: "regional",
                radius: 4.5,
                color: "#4caf50",
                weight: 1,
                fillColor: "#4caf50",
                fillOpacity: 1
            });
        }
        if (feature.properties.layer === "dummy")  {
            return L.circleMarker(latlng,  {
                pane: "dummy",
                radius: 7,
                color: "#4caf50",
                opacity: 0,
                weight: 1,
                fillColor: "#4caf50",
                fillOpacity: 0
            });
        }
        
        if (feature.properties.layer === "intercity")  {
            return L.circleMarker(latlng,  {
                pane: "intercity",
                radius: 3,
                color: "#ffa500",
                weight: 1,
                fillColor: "#ffa500",
                fillOpacity: 1
            });
        }
        if (feature.properties.layer === "historic")  {
            return L.circleMarker(latlng,  {
                pane: "historic",
                radius: 10,
                color: "#606060",
                weight: 1,
                fillColor: "#909090",
                fillOpacity: 1
            });
        }
    }
        """)

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }


# old timeline
    timeline = Timeline(
        geojson_data,
        pointToLayer=style_fn
    )

    # timeline = Timeline(
    #     geojson_data,
    #     style=style_fn
    # )

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
# sort_df()
# sort_metro_df()
# merge_df()
generate_map()
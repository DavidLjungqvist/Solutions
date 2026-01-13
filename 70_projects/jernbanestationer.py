import requests
import pandas as pd
from io import StringIO
import folium
from folium.plugins import TimestampedGeoJson


# query =
"""
SELECT ?station ?stationLabel ?lat ?lon ?openDate
WHERE {
    ?station wdt:P31 wd:Q55488 ;
             wdt:P131* wd:Q504125 ;
             wdt:P625 ?coord ;
             wdt:P1619 ?openDate .

  BIND(geof:latitude(?coord) AS ?lat)
  BIND(geof:longitude(?coord) AS ?lon)

    SERVICE wikibase:label {
      bd:serviceParam wikibase:language "en".
      }
}
"""

"""
SELECT ?station ?stationLabel ?lat ?lon ?openDate ?openDate2 ?endDate ?endDate2 ?endDate3 ?inUse
WHERE {
    ?station wdt:P31 wd:Q55488 ;
             wdt:P17 wd:Q35;
         #    wdt:P131* wd:Q504125 ;
             wdt:P625 ?coord .
             OPTIONAL { ?station wdt:P1619 ?openDate . }
             OPTIONAL { ?station wdt:P571 ?openDate2 . }
             OPTIONAL { ?station wdt:P582 ?endDate . }
             OPTIONAL { ?station wdt:P576 ?endDate2 . }
             OPTIONAL { ?station wdt:P3999 ?endDate3 . }
             OPTIONAL { ?station wdt:P5817 ?inUse . }

  BIND(geof:latitude(?coord) AS ?lat)
  BIND(geof:longitude(?coord) AS ?lon)

    SERVICE wikibase:label {
      bd:serviceParam wikibase:language "en".
      }
}
"""

query = """
SELECT ?station ?stationLabel ?lat ?lon ?openDate ?estDate #?endDate ?endDate2 ?endDate3
WHERE {
    ?station wdt:P31 wd:Q55488 ;
             wdt:P17 wd:Q35;
         #    wdt:P131* wd:Q504125 ;
             wdt:P625 ?coord ;
             wdt:P5817 wd:Q55654238 .
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



# print(response.text[:200])

df = pd.read_csv(StringIO(response.text))
print(df.head())

print(df.loc[3].to_string())

df["openDate"] = pd.to_datetime(df["openDate"], errors="coerce", utc=True)
df["estDate"] = pd.to_datetime(df["estDate"], errors="coerce", utc=True)
df["earliestDate"] = df[["openDate", "estDate"]].min(axis=1)

print(df.loc[3].to_string())

df = df.dropna(subset=["earliestDate"])

df["year"] = df["earliestDate"].dt.year

# "time": f"{int(row['year'])}-01-01"

features = []

for _, row in df.iterrows():
    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row["lon"], row["lat"]],
        },
        "properties": {
            "time": f"{int(row['year'])}-01-01",
            "popup": row["stationLabel"],
        },
    })

# print(features)

m = folium.Map(location=[55, 10], zoom_start=5)

TimestampedGeoJson(
    {
        "type": "FeatureCollection",
        "features": features,
    },
    period="P1Y",        # 1 year per step
    add_last_point=True,
    auto_play=False,
    loop=False,
).add_to(m)


m.save("railway_stations_map.html")

print(df[["earliestDate", "year", "lat", "lon"]].head(20))




df.to_csv("stations.csv", index=False)
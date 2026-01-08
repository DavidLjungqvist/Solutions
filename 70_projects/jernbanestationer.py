import requests
import pandas as pd
from io import StringIO

query = """
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

df.to_csv("stations.csv", index=False)
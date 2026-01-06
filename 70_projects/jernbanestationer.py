import requests
import pandas as pd
from io import StringIO

query = """
SELECT ?station ?stationLabel
WHERE {
    ?station wdt:P31 wd:Q55488 ;
             wdt:P131* wd:Q504125 .
             
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


response.raise_for_status()

print(response.text[:200])

df = pd.read_csv(StringIO(response.text))
print(df.head())

df.to_csv("stations.csv", index=False)
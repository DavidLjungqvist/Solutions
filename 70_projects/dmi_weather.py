from datetime import datetime
import httpx

lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"
now = datetime.now()
print(now)

def lightning(key):
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?datetime=2025-01-01T00:00:00Z/2025-12-02T12:00:00Z&limit=100&sortorder=observed,DESC&api-key=" + key
    response = httpx.get(url)
    strikes_info = response.json()
    strikes = strikes_info["features"]
    time = []
    # print(strikes)
    # for strike in strikes:
    #     print(f"Intensity: {abs(strike["properties"]["amp"])}")
    for i, strike in enumerate(strikes):
        time.append(datetime.fromisoformat(strike["properties"]["observed"].replace("Z", "+00:00")))
        print(f"Coordinates: {strike["geometry"]["coordinates"]}, Intensity: {abs(strike["properties"]["amp"])}, Time: {time[i]:%d.%m.%y  %H:%M:%S}")

lightning(lightning_api_key)
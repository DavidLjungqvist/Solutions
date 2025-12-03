from datetime import datetime, timezone
import os
import httpx
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import fastparquet
import pyarrow

# import datashader
# import holoviews

lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"
now_dt = datetime.now(timezone.utc)
now_iso = now_dt.isoformat().replace("+00:00", "Z")
# print(now_iso)
start_time = "2025-01-01T00:00:00Z"
end_time = now_iso

# bbox=7,54,16,58&

def lightning(key):
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?bbox=7,54,16,58&datetime=" + start_time + "/" + end_time + "&limit=10000&sortorder=observed,DESC&api-key=" + key
    response = httpx.get(url, timeout=30.0)
    print("Got Response")
    strikes_info = response.json()
    raw_strikes = strikes_info["features"]
    # time = []
    # print(strikes)
    # for strike in strikes:
    #     print(f"Intensity: {abs(strike["properties"]["amp"])}")
    # for i, strike in enumerate(strikes):
    #     time.append(datetime.fromisoformat(strike["properties"]["observed"].replace("Z", "+00:00")))
    #     print(f"Coordinates: {strike["geometry"]["coordinates"]}, Intensity: {abs(strike["properties"]["amp"])}, Time: {time[i]:%d.%m.%y  %H:%M:%S}")
    strikes = []
    for raw_strike in raw_strikes:
        strike = {"timestamp": raw_strike["properties"]["observed"], "lat": raw_strike["geometry"]["coordinates"][1], "lon": raw_strike["geometry"]["coordinates"][0], "intensity": raw_strike["properties"]["amp"]}
        strikes.append(strike)

    df = pd.DataFrame(strikes)

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")

    print(gdf.head())

    gdf.to_parquet("lightning_2025.parquet", index=False)


# print(list(ctx.providers.Stamen))
# print(ctx.__version__)
# print(list(ctx.providers))

def read_parquet_to_plot():
    gdf = gpd.read_parquet("lightning_2025.parquet")
    print(gdf.head())

    print(os.getcwd())
    print(os.path.exists("lightning_2025.parquet"))

    gdf = gpd.read_parquet("lightning_2025.parquet")
    print(gdf.head())
    print(gdf.crs)  # should be 'EPSG:4326'
    print(len(gdf))  # how many strikes
    print(gdf.describe())  # stats on intensity, lat, lon

    gdf_web = gdf.to_crs("EPSG:3857")

    fig, ax = plt.subplots(figsize=(10, 10))

    gdf_web.plot(ax=ax, markersize=20, alpha=0.6, color="yellow")

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    plt.show()

    # gdf.plot(markersize=1, figsize=(10, 10))
    # gdf.plot(marker='o', color='red', markersize=5, figsize=(8, 8))
    # filter options:
    # Example: only strikes with positive intensity
    # gdf_filtered = gdf[gdf['intensity'] > 0]
    # Example: only strikes in December
    # gdf_filtered = gdf[pd.to_datetime(gdf['timestamp']).dt.month == 12]


    # for strike in enumerate(strikes):
    #     time.append(datetime.fromisoformat(strike["properties"]["observed"].replace("Z", "+00:00")))
    #     print(f"Coordinates: {strike["geometry"]["coordinates"]}, Intensity: {abs(strike["properties"]["amp"])}, Time: {time[i]:%d.%m.%y  %H:%M:%S}")


lightning(lightning_api_key)
read_parquet_to_plot()
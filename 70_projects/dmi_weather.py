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
# print(now_iso)

# end_of_year = input_year + "-12-31T23:59:59"
# if end_of_year
# end_time = now_iso

# bbox=7,54,16,58&




def lightning(key, year, box_size):
    input_year = year
    start_date = input_year + "-01-01T00:00:00Z"
    now_dt = datetime.now(timezone.utc)
    print(now_dt.year, input_year)
    if str(now_dt.year) == str(input_year):
        end_date = now_dt.isoformat().replace("+00:00", "Z")
    else:
        end_date = input_year + "-12-31T23:59:59Z"

    print(start_date, end_date)

    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?bbox=" + box_size + "&datetime=" + start_date + "/" + end_date + "&limit=250000&sortorder=observed,DESC&api-key=" + key
    response = httpx.get(url, timeout=30.0)
    print(url)
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

    print(df.head())

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326")

    print(gdf.head())

    gdf.to_parquet("lightning_2025.parquet", index=False)


# print(list(ctx.providers.Stamen))
# print(ctx.__version__)
# print(list(ctx.providers))

def read_parquet_to_plot():
    # gdf = gpd.read_parquet("lightning_2025.parquet")
    # print(gdf.head())

    print(os.getcwd())
    print(os.path.exists("lightning_2025.parquet"))

    gdf = gpd.read_parquet("lightning_2025.parquet")
    print(gdf.head())
    print(gdf.crs)  # should be 'EPSG:4326'
    print(len(gdf))  # how many strikes
    print(gdf.describe())  # stats on intensity, lat, lon

    gdf_web = gdf.to_crs("EPSG:3857")

    fig, ax = plt.subplots(figsize=(16, 16))

    gdf_web.plot(ax=ax, markersize=20, alpha=1, color="yellow", edgecolor="black")

    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    plt.show()

    # gdf.plot(markersize=1, figsize=(10, 10))
    # gdf.plot(marker='o', color='red', markersize=5, figsize=(8, 8))
    # filter options:
    # Example: only strikes with positive intensity
    # gdf_filtered = gdf[gdf['intensity'] > 0]
    # Example: only strikes in December
    # gdf_filtered = gdf[pd.to_datetime(gdf['timestamp']).dt.month == 12]

def main(year):
    area_dk = "7,54,16,58"
    area_copenhagen = "12.35,55.6,12.65,55.8"
    area_n_jutland = "8.1,56.75,11.3,58" #Need ajusting
    area_c_jutland = "8.1,56.75,11,55.65"
    lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"
    lightning(lightning_api_key, year, area_n_jutland)
    read_parquet_to_plot()


main("2022")

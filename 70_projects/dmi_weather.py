from datetime import datetime, timezone
import sys
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

# lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"

# end_of_year = input_year + "-12-31T23:59:59"
# if end_of_year
# end_time = now_iso




# class Lightning:
#     def __init__(self, time, lat, lon, intensity):
#         self.timestamp = time
#         self.latitude = lat
#         self.longitude = lon
#         self.intensity = abs(intensity)
#         self.intesity_group = 1 if self.intensity < 10 else 2 if self.intensity < 30 else 3  # Used for determining the color of points


class Lightning:
    def __init__(self, data):
        # self.id = index
        # self.timestamp = data.properties.observed
        self.timestamp = data["properties"]["observed"]
        # self.latitude = data.geometry.coordinates
        self.latitude = data["geometry"]["coordinates"][1]
        # self.longitude = data.geometry.coordinates
        self.longitude = data["geometry"]["coordinates"][0]
        self.intensity = abs(data["properties"]["amp"])
        self.intensity_group = 0 if self.intensity < 10 else 1 if self.intensity < 30 else 2  # Used for determining the color of points


def get_json(key, year, box_size):
    input_year = year
    start_date = input_year + "-01-01T00:00:00Z"
    now_dt = datetime.now(timezone.utc)
    if str(now_dt.year) == str(input_year):
        end_date = now_dt.isoformat().replace("+00:00", "Z")
    else:
        end_date = input_year + "-12-31T23:59:59Z"

    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?bbox=" + box_size + "&datetime=" + start_date + "/" + end_date + "&limit=250000&sortorder=observed,DESC&api-key=" + key
    response = httpx.get(url, timeout=30.0)

    return response.json()

def lightning(key, year, box_size):
    # input_year = year
    # start_date = input_year + "-01-01T00:00:00Z"
    # now_dt = datetime.now(timezone.utc)
    # print(now_dt.year, input_year)
    # if str(now_dt.year) == str(input_year):
    #     end_date = now_dt.isoformat().replace("+00:00", "Z")
    # else:
    #     end_date = input_year + "-12-31T23:59:59Z"
    #
    # print(start_date, end_date)
    #
    # url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?bbox=" + box_size + "&datetime=" + start_date + "/" + end_date + "&limit=250000&sortorder=observed,DESC&api-key=" + key
    # response = httpx.get(url, timeout=30.0)
    # print(url)
    # print("Got Response")
    # strikes_info = response.json()
    data = get_json(key, year, box_size)
    raw_strikes = data["features"]
    # time = []
    # print(strikes)
    # for strike in strikes:
    #     print(f"Intensity: {abs(strike["properties"]["amp"])}")
    # for i, strike in enumerate(strikes):
    #     time.append(datetime.fromisoformat(strike["properties"]["observed"].replace("Z", "+00:00")))
    #     print(f"Coordinates: {strike["geometry"]["coordinates"]}, Intensity: {abs(strike["properties"]["amp"])}, Time: {time[i]:%d.%m.%y  %H:%M:%S}")
    obj_list = []
    for strike in (raw_strikes):
        obj = Lightning(strike)
        obj_list.append(obj)



    # strikes = []


    # for raw_strike in raw_strikes:
    #     strike = {"timestamp": raw_strike["properties"]["observed"], "lat": raw_strike["geometry"]["coordinates"][1], "lon": raw_strike["geometry"]["coordinates"][0], "intensity": raw_strike["properties"]["amp"]}
    #     strikes.append(strike)

    rows = [obj.__dict__ for obj in obj_list]

    # df = pd.DataFrame(strikes)
    df = pd.DataFrame(rows)

    print(df.head())

    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")

    print(gdf.head())

    gdf.to_parquet("lightning_2025.parquet", index=False)


# print(list(ctx.providers.Stamen))
# print(ctx.__version__)
# print(list(ctx.providers))

def read_parquet_to_plot(markersize):
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

    linewidth_dict = {3: 0.3, 10: 0.5, 30: 1.2}
    linewidth = linewidth_dict[markersize]
    color_map = {0: "Yellow", 1: "Orange", 2: "Red"}
    gdf_web["color"] = gdf_web["intensity_group"].map(color_map)
    gdf_web.plot(ax=ax, color=gdf_web["color"], markersize=markersize, alpha=1, edgecolor="black", linewidth=linewidth) # linewidth = small: 0.25, medium: 0.5, large: 1.2

    # gdf_web.plot(ax=ax, markersize=20, alpha=1, color="yellow", edgecolor="black")
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    plt.show()

    # gdf.plot(markersize=1, figsize=(10, 10))
    # gdf.plot(marker='o', color='red', markersize=5, figsize=(8, 8))
    # filter options:
    # Example: only strikes with positive intensity
    # gdf_filtered = gdf[gdf['intensity'] > 0]
    # Example: only strikes in December
    # gdf_filtered = gdf[pd.to_datetime(gdf['timestamp']).dt.month == 12]

def main():
    args = sys.argv[1:]
    print(args)
    # area_fo = "-7.85,61.3,-6.1,62.45"
    # area_gl
    area_dk = "7,54,16,58"
    area_copenhagen = "12.35,55.6,12.65,55.8"
    area_sea_lolland = "10.85,54.55,12.8,56.15"
    area_n_jutland = "8.05,56.65,11.3,57.8"
    area_c_jutland = "8.05,55.65,11,56.70"
    area_south_dk = "8.05,54.65,11,55.70"
    area_bornholm = "14.6,54.96,15.2,55.32"
    lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"
    small_marker = 3
    medium_marker = 10
    large_marker = 30
    area_option_dict = {1: area_dk, 2: area_copenhagen, 3: area_sea_lolland, 4: area_n_jutland, 5: area_c_jutland, 6: area_south_dk, 7: area_bornholm}
    marker_size_dict = {1: small_marker, 2: large_marker, 3: medium_marker, 4: medium_marker, 5: medium_marker, 6: medium_marker, 7: large_marker}
    year_input = "x"
    while year_input == "x":
        if len(args) >= 1:
            map_code_input = int(args[0])
        else:
            print("Indtast et nummer for at se de følgende kort:\n1 : Danmark / 2 : København / 3 : Sjælland og Lolland / 4 : Nord Jylland / 5 : Midt Jylland / 6 : Syd Danmark / 7 : Bornholm")
            map_code_input = input("Vælg et kort: ")
        if len(args) >= 2:
            year_input = args[1]
        else:
            print("For at vælge et andet område indtast 'x'")
            year_input = input("Vælg et år: ")
        while True:
            selected_area = area_option_dict[int(map_code_input)]
            lightning(lightning_api_key, year_input, selected_area)
            markersize = marker_size_dict[int(map_code_input)]
            read_parquet_to_plot(markersize)
            year_input = input("Vælg et nyt år eller indtast 'x' for at vælge kort: ")
            if year_input == "x":
                break

main()

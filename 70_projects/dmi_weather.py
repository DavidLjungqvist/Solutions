from datetime import datetime, timezone
import sys
import os
import httpx
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import configparser
import fastparquet
import pyarrow

# import datashader
# import holoviews

map_config_file = "map_config.ini"
config = configparser.ConfigParser(inline_comment_prefixes='#')
config.optionxform = str
config.read(map_config_file, encoding='utf-8')


class Area:
    def __init__(self, name, w, s, e, n, marker_size, line_width):
        self.name = name
        self.west = w
        self.south = s
        self.east = e
        self.north = n
        self.marker_size = marker_size
        self.line_width = line_width


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


def get_json(key, year, area):
    input_year = year
    start_date = input_year + "-01-01T00:00:00Z"
    now_dt = datetime.now(timezone.utc)
    if str(now_dt.year) == str(input_year):
        end_date = now_dt.isoformat().replace("+00:00", "Z")
    else:
        end_date = input_year + "-12-31T23:59:59Z"

    map_coordinates = f"{area.west},{area.south},{area.east},{area.north}"

    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?bbox=" + map_coordinates + "&datetime=" + start_date + "/" + end_date + "&limit=250000&sortorder=observed,DESC&api-key=" + key
    response = httpx.get(url, timeout=30.0)

    return response.json()


def lightning(data):
    raw_strikes = data["features"]
    obj_list = []
    for strike in (raw_strikes):
        obj = Lightning(strike)
        obj_list.append(obj)
    rows = [obj.__dict__ for obj in obj_list]
    df = pd.DataFrame(rows)
    print(df.head())
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")
    print(gdf.head())
    gdf.to_parquet("lightning_2025.parquet", index=False)


def read_parquet_to_plot(markersize, line_width):
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

    # linewidth_dict = {3: 0.3, 10: 0.5, 30: 1.2}
    # linewidth = linewidth_dict[markersize]

    color_map = {0: "Yellow", 1: "Orange", 2: "Red"}

    gdf_web["color"] = gdf_web["intensity_group"].map(color_map)
    gdf_web.plot(ax=ax, color=gdf_web["color"], markersize=markersize, alpha=1, edgecolor="black", linewidth=line_width)  # linewidth = small: 0.25, medium: 0.5, large: 1.2

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

    # small_marker = 3
    # medium_marker = 10
    # large_marker = 30

    # area_fo = "-7.85,61.3,-6.1,62.45"
    # area_gl

    areas = []
    area_strings = ["Denmark", "Copenhagen", "Sea Lolland", "North Jutland", "Central Jutland", "South Denmark", "Bornholm"]
    for area_string in area_strings:
        area = read_area(area_string, config)
        areas.append(area)

    lightning_api_key = "501d635d-81f9-42f9-a36a-00fc85bb2bce"

    area_option_dict = {1: areas[0], 2: areas[1], 3: areas[2], 4: areas[3], 5: areas[4], 6: areas[5], 7: areas[6]}
    # marker_size_dict = {1: small_marker, 2: large_marker, 3: medium_marker, 4: medium_marker, 5: medium_marker, 6: medium_marker, 7: large_marker}

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
            if year_input == "x":
                break
            selected_area = area_option_dict[int(map_code_input)]

            data = get_json(lightning_api_key, year_input, selected_area)
            lightning(data)
            # markersize = marker_size_dict[int(map_code_input)]
            read_parquet_to_plot(int(selected_area.marker_size), float(selected_area.line_width))
            year_input = input("Vælg et nyt år eller indtast 'x' for at vælge kort: ")

def read_area(name, config):
    west = config.get(name, "west") # fallback="results_only")
    south = config.get(name, "south") # fallback="results_only")
    east = config.get(name, "east") # fallback="results_only")
    north = config.get(name, "north") # fallback="results_only")
    marker_size = config.get(name, "marker size") # fallback="results_only")
    line_width = config.get(name, "line width") # fallback="results_only")
    area = Area(name, west, south, east, north, marker_size, line_width)
    return area

main()

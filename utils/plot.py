import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
import geodatasets

df = pd.read_csv("landsat_data.csv", delimiter=',', encoding='unicode-escape')

geometry = [Point(xy) for xy in zip(df['Corner Upper Left Latitude'], df['Corner Upper Left Longitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
gdf.plot(ax=world.plot(figsize=(10,6)), marker='o', color='red', markersize=15);

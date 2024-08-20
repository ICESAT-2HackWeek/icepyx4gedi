import earthaccess
import geopandas as gpd
import xarray as xr

"""
This script uses earthaccess to access GEDI L2B data on the cloud and converts it to Xarray format. It can only do part of a single data file at a time, so some extra effort will be needed to add other parts of the file (or files).

Also, extracting the data into Xarray is rather slow, so an alternative solution might be needed.
"""

# Initialize Earthaccess login
earthaccess.login(strategy='interactive', persist=True)

# Login authorization
auth = earthaccess.login()

# Search parameters
short_name = "GEDI02_B"
spatial_file = "/home/jovyan/gedi_wildfire.geojson"
date_range = ('2019-04-04', '2020-12-31')

# Extract bounding box from geoJSON
geojson = gpd.read_file(spatial_file)
bbox = tuple(list(geojson.total_bounds))

# Access L2B data through the cloud
results = earthaccess.search_data(
    short_name = short_name,
    cloud_hosted=True,
    bounding_box = bbox,
    temporal = date_range
)

# Extract information from first file, first beam into Xarray. Note that this step takes a while...
files = earthaccess.open(results)
ds = xr.open_dataset(files[1], group='/BEAM0001/', phony_dims='sort')
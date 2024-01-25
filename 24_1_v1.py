import cdsapi
import geopandas as gpd
import os

# Setting up the output path
fp_outpath_ecmwf = os.path.expanduser('~/Downloads/ECMWF_Test_dir')
if not os.path.exists(fp_outpath_ecmwf):
    os.makedirs(fp_outpath_ecmwf)

# Authentication for ECMWF API
client = cdsapi.Client(url=os.getenv('ECMWF_API_URL'), 
                       key=os.getenv('ECMWF_API_KEY'))

# Define Area of Interest (AOI)
countries = ['Nicaragua', 'Honduras', 'Guatemala', 'El Salvador']
aoi_countries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
aoi_countries = aoi_countries[aoi_countries['name'].isin(countries)]
aoi_bbox = aoi_countries.total_bounds  # [minx, miny, maxx, maxy]

# Function to create API requests
def create_requests(years, months, leadtime_months, aoi_bbox):
    requests = []
    for year in years:
        for leadtime_month in leadtime_months:
            requests.append({
                'product_type': 'monthly_mean',
                'format': 'netcdf',
                'originating_centre': 'ecmwf',
                'system': '51',
                'variable': ['total_precipitation'],
                'year': [str(year)],
                'month': [f"{month:02d}" for month in months],
                'area': [
                    aoi_bbox[3],  # North
                    aoi_bbox[0],  # West
                    aoi_bbox[1],  # South
                    aoi_bbox[2]   # East
                ],
                'leadtime_month': [str(leadtime_month)],
            })
    return requests

# Creating requests for 2019-2022 and 2023 for testing purposes
requests_2019_2022 = create_requests(range(2019, 2023), range(1, 13), range(1, 5), aoi_bbox)
requests_2023 = create_requests([2023], range(1, 10), range(1, 5), aoi_bbox)

# Downloading data
def download_data(requests, path):
    for request in requests:
        target_filename = f"ecmwf_forecast_{request['year'][0]}_lt{request['leadtime_month'][0]}.nc"
        request['target'] = target_filename
        client.retrieve('seasonal-monthly-single-levels', request, os.path.join(path, target_filename))
        print(f"Downloaded {target_filename}")

# Downloading 2019-2022 data
print("Downloading data for 2019-2022")
download_data(requests_2019_2022, fp_outpath_ecmwf)

# Downloading 2023 data
print("Downloading 2023 data")
download_data(requests_2023, fp_outpath_ecmwf)

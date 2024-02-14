import cdsapi
import os

# Setting up the output path
fp_outpath_ecmwf = os.path.expanduser('~/Downloads/ECMWF_Global_Forecast')
if not os.path.exists(fp_outpath_ecmwf):
    os.makedirs(fp_outpath_ecmwf)

# Authentication for ECMWF API
client = cdsapi.Client(url=os.getenv('ECMWF_API_URL'), key=os.getenv('ECMWF_API_KEY'))

# Function to create a single API request for the specified years, all months, and all leadtime months
def create_single_request(years, months, leadtime_months):
    return {
        'product_type': 'monthly_mean',
        'format': 'grib',  # Format set to grib
        'originating_centre': 'ecmwf',
        'system': '51',
        'variable': ['total_precipitation'],
        'year': [str(year) for year in years],
        'month': [f"{month:02d}" for month in months],
        'leadtime_month': [str(leadtime_month) for leadtime_month in leadtime_months],
        # 'area' parameter removed to target the whole globe
    }

# Adjusting for all available lead times
all_leadtimes = range(1, 7)  # Assuming these are all the lead times available

# Utilizing the specific range of available years you've provided
available_years = range(1981, 2024)  # Updated to include 1981 through 2023

# Creating a single request for all years, months, and leadtime months
single_request = create_single_request(available_years, range(1, 13), all_leadtimes)

# Downloading data with a single request
def download_single_request(request, path):
    target_filename = "ecmwf_forecast_global_all_years.grib"
    request['target'] = os.path.join(path, target_filename)
    client.retrieve('seasonal-monthly-single-levels', request, request['target'])
    print(f"Downloaded {target_filename}")

# Now calling download_single_request with the single request
download_single_request(single_request, fp_outpath_ecmwf)
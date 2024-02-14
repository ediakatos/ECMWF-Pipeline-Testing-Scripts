import cdsapi
import os

# Define the output path for the downloaded files
output_path = os.path.expanduser('~/Downloads/ERA5_Global_Data')
if not os.path.exists(output_path):
    os.makedirs(output_path)

# CDS API client
c = cdsapi.Client()

def download_era5_data_single_request(years, months, format='grib'):
    filename = f"ERA5_total_precipitation_global_1981_2023_all_months.{format}"
    filepath = os.path.join(output_path, filename)
    c.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type': 'monthly_averaged_reanalysis',
            'variable': 'total_precipitation',
            'year': [str(year) for year in years],
            'month': months,
            'time': '00:00',
            'format': format,
        },
        filepath)
    print(f"Downloaded: {filepath}")

# Define the years and months for the single request
years = range(1981, 2024)  # From 1981 to 2023 try extra 2024 next time
months = [f"{month:02d}" for month in range(1, 13)]  # All months

# Download the data for the entire globe with a single request
download_era5_data_single_request(years, months)
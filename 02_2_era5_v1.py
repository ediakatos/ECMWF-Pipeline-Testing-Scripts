import cdsapi
import os

# Define the output path for the downloaded files
output_path = os.path.expanduser('~/Downloads/ERA5_Data')
if not os.path.exists(output_path):
    os.makedirs(output_path)

# CDS API client
c = cdsapi.Client()

# Function to download ERA5 data
def download_era5_data(years, months, area, variable='total_precipitation', product_type='monthly_averaged_reanalysis', format='netcdf'):
    for year in years:
        for month in months:
            filename = f"ERA5_{variable}_{year}_{month}.nc"
            filepath = os.path.join(output_path, filename)
            c.retrieve(
                'reanalysis-era5-single-levels-monthly-means',
                {
                    'product_type': product_type,
                    'variable': variable,
                    'year': year,
                    'month': month,
                    'time': '00:00',
                    'area': area,
                    'format': format,
                },
                filepath)
            print(f"Downloaded: {filepath}")

# Define the years, months, and area of interest
years = ['2019', '2020', '2021', '2022', '2023']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
area = [17, -92, 11, -83]  # [North, West, South, East] covering Nicaragua, Honduras, Guatemala, El Salvador

# Download the data
download_era5_data(years, months, area)

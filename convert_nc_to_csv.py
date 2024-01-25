import xarray as xr
import pandas as pd
import os

# Define the directory where your .nc files are located
data_directory = os.path.expanduser('~/Downloads/ECMWF_Test_dir')

# Loop through the .nc files in the directory
for filename in os.listdir(data_directory):
    if filename.endswith('.nc'):
        filepath = os.path.join(data_directory, filename)
        dataset = xr.open_dataset(filepath)

        # Convert the dataset to a Pandas DataFrame for tabular format
        df = dataset.to_dataframe()

        # Determine the output CSV filename based on the input filename
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_filepath = os.path.join(data_directory, csv_filename)

        # Export the DataFrame to the CSV file
        df.to_csv(csv_filepath, index=False)

        print(f'Data exported to {csv_filepath}')

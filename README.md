# ECMWF-Pipeline-Testing-Scripts
This repo contains Python scripts for ECMWF data testing, adapted from a CHD R script. It automates data retrieval and preprocessing for specific AOIs, focusing on monthly precipitation forecasts.

This repository hosts a collection of Python scripts developed for the purpose of testing and validating ECMWF (European Centre for Medium-Range Weather Forecasts) data pipelines. Originating from an R script shared by CHD, these scripts have been adapted and extended to fit the specific needs of our data science team at MapAction.

The primary script (24_1_v1.py) automates the process of downloading, converting, and preprocessing ECMWF forecast data for a targeted area of interest (AOI) encompassing Nicaragua, Honduras, Guatemala, and El Salvador. Utilizing libraries such as cdsapi for data retrieval, geopandas for spatial operations, and standard Python modules like os, the script sets up a structured approach to fetch monthly mean precipitation forecasts, catering to the specific geographical and temporal needs of our projects.

Key functionalities include:

Authentication and interaction with the ECMWF API to programmatically retrieve forecast data.
Definition and application of AOIs through geospatial filtering to narrow down data downloads to relevant regions.
Dynamic generation of API requests based on specified parameters such as time range and leadtime months, enhancing the script's flexibility to accommodate different forecasting needs.
A systematic approach to downloading and organizing forecast data into a designated directory, streamlining the workflow for subsequent analysis and testing phases.

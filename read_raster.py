# -*- coding: utf-8 -*-
"""
read_raster.py

Reading raster files with rasterio.

Created on Wed Nov 14 09:14:03 2018

@author: Hadi
"""

import rasterio
import os 
import numpy as np
import pycrs


# Data directory
data_dir = r"C:\IntroGIS"

# Parse the file path
fp = os.path.join(data_dir, 'L5_data', 'Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif')


# Open the file
raster = rasterio.open(fp)

# Projection
print(raster.crs)
#pycrs.parser.from_epsg_code(3067).to_proj4()

# Affine transform
raster.transform

# Dimension
raster.width
raster.height

# Number of channels
raster.count

# Bounds of the file
raster.bounds

# Driver
raster.driver

# No data value
raster.nodatavals

# All metadata at once
raster.meta


# Read the data values to Python
# ------------------------------

# Read the raster into Numpy array
# See geopython materials on numpy
band1 = raster.read(1)

# Access the data type
band1.dtype
data_type = str(band1.dtype)

# Calculate basic stats
# ----------------------

# Stats of one band
band1.max() 
band1.min()

# Read all the bands
array = raster.read() 

# Calculate channel stats
stats = []  # a list

# iterrows used in pandas, geopandas
for idx, band in enumerate(array):
    band_stat = {
            'min': band.min(),
            'max': band.max(),
            'median': np.median(band),
            'mean': band.mean(),
            'std': band.std()
            }   # A dictionary
    # Insert stats inside another dict
    channel_stat = {'channel %s' % (idx+1): band_stat} 
    # "Hello {name} {name}!".format(name='Hadi')
    stats.append(channel_stat)
    








































# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:44:15 2022

@author: azade
"""

import geopandas as gpd
import os
import rasterio
import scipy.sparse as sparse 
import pandas as pd
import numpy as np


master_df=pd.DataFrame()
for csvfiles in os.listdir(os.getcwd()):
    if csvfiles.endswith('.csv'):
        master_df=master_df.append(pd.read_csv(csvfiles))
        
master_df.to_csv("D:/GitHub Uploads/Merging-CSV-files/masterfile2.csv", index=False)
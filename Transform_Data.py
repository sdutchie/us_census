# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:31:33 2021

@author: smdut
"""

import pandas as pd

df = pd.read_csv('Get_Data.csv', index_col=0)
    #Note: index_col=0 makes the first column in the csv file the index
        #Variables: B01003_001E (TOTAL POPULATION)
        #Variables: B02001_003E (Estimate!!Total:!!Black or African American alone)
        #Variables: B02001_002E (Estimate!!Total:!!White alone)
        #Variables: B11001_001E (Estimate!!Total:, HOUSEHOLD TYPE (INCLUDING LIVING ALONE))
        #Variables: B28008_002E (Estimate!!Total:!!Has a computer:)
#print(df.columns)
df.columns = ['Name', 'Total Pop', 'White Pop', 'Black Pop', 'Household Type', 'Computer', 'State', 'County', 'Tract', 'Block Group']
#print(df.columns)
#print(df.head)
df.drop(index=0, inplace = True)
#print(df.head)
#How to Export Pandas DataFrame to a CSV File: https://datatofish.com/export-dataframe-to-csv/
df.to_csv(r'C:\MLPP\Transformed_Data.csv')

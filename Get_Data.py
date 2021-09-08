# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:28:16 2021

@author: smdut
"""

import requests
import pandas as pd
import json

#Request Data from API
url = "https://api.census.gov/data/2019/acs/acs5?get=NAME,B01003_001E,B02001_003E,B02001_002E,B11001_001E,B28008_002E&for=block%20group:*&in=state:51&in=county:*&in=tract:*&key=f6c7074b1ca2c944b1cb15acbe4b2a2e6ab63c4e"
    #Variables: B01003_001E,B02001_003E,B02001_002E,B11001_001E,B28008_002E (0/5 nulls :) 
        #Variables: B01003_001E (TOTAL POPULATION)
        #Variables: B02001_003E (Estimate!!Total:!!Black or African American alone)
        #Variables: B02001_002E (Estimate!!Total:!!White alone)
        #Variables: B11001_001E (Estimate!!Total:, HOUSEHOLD TYPE (INCLUDING LIVING ALONE))
        #Variables: B28008_002E (Estimate!!Total:!!Has a computer:)
r = requests.get(url)
#print(r.text)


#Convert Requests Response to Json: https://www.codegrepper.com/code-examples/javascript/requests+json+response+list+data+python
json_data = json.loads(r.text) #outputs list of lists
df = pd.DataFrame(json_data)
print(df.head)


#How to Export Pandas DataFrame to a CSV File: https://datatofish.com/export-dataframe-to-csv/
df.to_csv(r'C:\MLPP\Get_Data.csv')

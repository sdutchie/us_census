# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:16:05 2021

@author: smdut
"""

"Sources"
# Connect To PostgreSQL Database Server Using Psychopg2: https://www.postgresqltutorial.com/postgresql-python/connect/
#CSVs to the Database: https://dssg.github.io/hitchhikers-guide/curriculum/1_getting_and_keeping_data/csv-to-db/
#(BEST) Loading Data into Postgres using Python and CSVs:https://www.dataquest.io/blog/loading-data-into-postgres/
#Connect to PostgreSQL Database Server Using Python Module of psycopg2: https://towardsdatascience.com/connect-to-postgresql-database-server-using-psycopg2-with-an-elegant-configuration-file-dba6fc885989#2ac2
#Import CSV File Into PostgreSQL Table: https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/

import psycopg2

#Connect to Database
conn = psycopg2.connect(
    host="acs-db.mlpolicylab.dssg.io",
    database="acs_data_loading",
    user="mlpp_student",
    password="CARE-horse-most")
cur = conn.cursor()

#Create Table
#Note: Create it in the acs schema with table name: acs.{your_andrew_id}_acs_data
cur.execute("""
CREATE TABLE acs.sdutchie_acs_data(
    ID Int PRIMARY KEY NOT NULL,  
    Name text,
    Total_Pop INT,
    White_Pop INT,
    Black_Pop INT,
    Household_Type INT,
    Computer INT,
    State INT,
    County INT,
    Tract INT,
    Block_Group INT);
""")
conn.commit()

# #Check to make sure table was created
# cur.execute("""
# SELECT Name FROM acs.sdutchie_acs_data LIMIT 5;
# """)
# one = cur.fetchone()
# print(one)


#Load Data
import csv
with open('Transformed_Data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        """INSERT INTO acs.sdutchie_acs_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        row
    )
conn.commit()

#Check to make sure it worked
cur.execute("""
SELECT Name FROM acs.sdutchie_acs_data LIMIT 5;
""")
one = cur.fetchone()
print(one)

#Close
conn.close()
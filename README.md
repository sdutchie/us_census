# us_census

Instructions: discussion of what you did and why (what data you chose, how you transformed/structured it, how you loaded it, etc)

## Features
I chose the state of Virginia becuase I'm from Virginia. My variables were: (1) Total_Pop (2) White Population (3) Black Population (4) Household Type (5) Computer. A lot of my decision was because I assumed these variables were less likely to be null, but I will admit to being curious about the distribution of certain socioeconomic factors between races and ethnicities. I attempted to add Korean as one of the variables since Virginia has a really large Korean population, but many of the values were null.

### Useful Sources: 
- API Link: https://www.census.gov/data/developers/data-sets.html
- Census Data User Guide: https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-guide.pdf
- BEAUTIFUL VIDEO: https://www.youtube.com/watch?v=l47HptzM7ao&ab_channel=DataCamp    
- Variable List: https://api.census.gov/data/2019/acs/acs5/variables.html

## Transformation and Structure
I did few transformations on the data since I decided to keep the index as a column and use it as a the primary key for my table. I didn't realize the data's first row coming from the API was a header until much later, so I ended up just dropping that row.

## Loading
After connecting to the database and creating my table, I loaded the data using a with open statement and after skipping the first line, read in the row using a for-loop.

### Useful Sources: 
- Connect To PostgreSQL Database Server Using Psychopg2: https://www.postgresqltutorial.com/postgresql-python/connect/
- CSVs to the Database: https://dssg.github.io/hitchhikers-guide/curriculum/1_getting_and_keeping_data/csv-to-db/
- (BEST) Loading Data into Postgres using Python and CSVs:https://www.dataquest.io/blog/loading-data-into-postgres/
- Connect to PostgreSQL Database Server Using Python Module of psycopg2: https://towardsdatascience.com/connect-to-postgresql-database-server-using-psycopg2-with-an-elegant-configuration-file-dba6fc885989#2ac2

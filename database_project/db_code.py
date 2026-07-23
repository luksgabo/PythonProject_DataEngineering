'''
Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

In this lab, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.
Objectives

In this lab you'll learn how to:

    Create a database using Python

    Load the data from a CSV file as a table to the database

    Run basic "queries" on the database to access the information

Scenario

Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :
Header 	Description
ID 	Employee ID
FNAME 	First Name
LNAME 	Last Name
CITY 	City of residence
CCODE 	Country code (2 letters)
'''
#%% Import libraries
import pandas as pd
import sqlite3

#%% Connection to database
conn = sqlite3.connect('STAFF.db')

# %% Table attributes
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# %% Reading csv file and loading to database
file_path = './INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, 
          if_exists='replace', index=False)

# %% Running basic queries on the data
def query(query_statement):
    # query_statement = f"SELECT * FROM {table_name}"
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)

#%%
# query(f"SELECT COUNT(*) FROM {table_name}")
# query(f"SELECT * FROM {table_name} LIMIT 5")
# query(f"SELECT FNAME FROM {table_name}")
query(f"SELECT DISTINCT(CITY) FROM {table_name}")

# %% Load data into database table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, 
                   if_exists='append', index=False)
print('Data appended')

# %% Close the connection
conn.close()

# %%

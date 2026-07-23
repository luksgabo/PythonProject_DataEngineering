'''
Lab Task:
Create an automated ETL script that extracts the latest list of countries
ranked by GDP in billion USD, rounded to 2 decimal places, from the IMF
reference data source.

Objective:
- Build a Python pipeline that retrieves the required GDP data
- Save the output as a CSV file named Countries_by_GDP.csv
- Store the data in a SQLite database table named Countries_by_GDP
  with columns Country and GDP_USD_billion
- Run a database query to display countries with GDP greater than 100
  billion USD
- Log the full execution process in a file named etl_project_log.txt
'''

#%% Import Libraries
import pandas as pd, numpy as np
import requests, sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

#%% initializing known entities
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
db_name = 'World_Economics.db'
table_name = 'Countries_by_GDP'
table_attribs = ['Country', 'GDP_USD_millions']
csv_path = './Countries_by_GDP.csv'

#%% get request response from url
response = requests.get(url, )
# parse text to html
html_file = BeautifulSoup(response.text, 'html.parser', )

#%% Write a data extraction function to retrieve the relevant information from the required URL.
def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''


    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''


#%% Transform the available GDP information into 'Billion USD' from 'Million USD'.

#%% Load the transformed information to the required CSV file and as a database file.

#%% Run the required query on the database.

#%% Log the progress of the code with appropriate timestamps.

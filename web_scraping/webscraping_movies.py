#%%
''' Lab Objectives:
Use the requests and BeautifulSoup libraries to extract the contents of a web page

Analyze the HTML code of a webpage to find the relevant information

Extract the relevant information and save it in the required form

Scenario

Consider that you have been hired by a Multiplex management organization to extract the information 
of the top 50 movies with the best average rating from the web link shared below.
https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

The information required is Average Rank, Film, and Year.
You are required to write a Python script webscraping_movies.py that extracts the information and saves it to a CSV file top_50_films.csv. 
You are also required to save the same information to a database Movies.db under the table name Top_50.
'''
#%% Libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests, sqlite3

# %% Initializing known entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = './top_50_films.csv'
df = pd.DataFrame(columns=['Average Rank', 'Film', 'Year'])
count = 0 # for loops

# %% Loading the webpage for scraping
# load entire web page as an HTML document
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser') 

# %% Scraping html file
tables = data.find_all('table')
# print([t.caption for t in tables])
rows = tables[0].tbody.find_all('tr')

# %% iterate over the rows to find the required data.
headers = [h.text for h in rows[0].find_all('th')[:3]]
for row in rows[1:]:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {headers[0]:col[0].contents[0],
                         headers[1]:col[1].contents[0],
                         headers[2]:col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count+=1
    else:
        break

print(df.head())

# %% Save dataframe to csv
df.to_csv(csv_path)

# %% Database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

# %%

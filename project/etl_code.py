import xml.etree.ElementTree as ET 
import pandas as pd
import glob
from datetime import datetime as dt

#%%
log_file = 'log_file.txt'
target_file = 'transformed_data.csv'

#%% Extraction functions
def extract_csv(file_to_process):
    return pd.read_csv(file_to_process)
    
def extract_json(file_to_process):
    return pd.read_json(file_to_process, lines=True)

def extract_xml(file_to_process):
    # create dataframe with headers based on the xml file
    dataframe = pd.DataFrame( columns=["name", "height", "weight"]) 
    # parse the xml file to an ElementTree object
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        # add values to the dataframe 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 

# Function that identifies the type of file and uses the appropriate
# function to extract the data into a dataframe
def extract(): 
    # create an empty data frame to hold extracted data 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) 
   
    # process all csv files, except the target file
    for csvfile in glob.glob("*.csv"):
        # check if the file is not the target file
        if csvfile == target_file: continue
        extracted_data = pd.concat([extracted_data, 
            pd.DataFrame(extract_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, 
            pd.DataFrame(extract_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, 
            pd.DataFrame(extract_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

#%% Units conversion
def transform(data):
    ''' Convert inches to meters and round off to two decimals
    1 in = 0.0254 m'''
    data['height'] = round(data['height']*.0254,2)

    ''' Convert pounds to kilograms and round off to two decimals
    1 lb = 0.45359237 kg'''
    data['weight'] = round(data['weight']*0.45359237,2)

    return data

#%% Loading and Logging
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    # Year-Monthname-Day-Hour-Minute-Second 

    # get current timestamp 
    now = dt.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + '\n' + message + '\n') 

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)
    
# def decorator(func, message):
#     def wrapper():
#         log_progress('Start: ' + message)
#         func()
#         log_progress('Finished: ' + message)
#     return wrapper

#%% ETL process

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 
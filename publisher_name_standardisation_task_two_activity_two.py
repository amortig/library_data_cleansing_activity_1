#import pandas package, fuzzywuzzy for string matching, and pip to install packages
import pip
import ensurepip
ensurepip
import re
from gettext import install
import rapidfuzz
from rapidfuzz import fuzz, process
import pandas as pd

 


#-------------------import file and assign it to a variable as a data frame ---------------------------------

df = metadata_extract = pd.read_excel(r'C:\Users\46071956\Downloads\library_excel_data_cleaning_scripts\Outputs\metadata_extract_20260127_filtered_task_two_activity_one.xlsx')



#----------------store the values within the "publisher" column as a variable--------------------------------
publisher_col="publisher"


#----------------define a cleaning function that checks for the following:-----------------------------------
# Identify None/NaN values 
# Covert values to text and lowercase
# Remove punctuation
# Make '&' and 'And' equivalent
# Remove extra spaces 
# Remove corporate markers such as 'ltd', 'plc, 'gmbh'
#----------------finally, return back the cleaned publisher names-------------------------------------------


def clean_publisher (text):
    if pd.isna(text):
        return None
    text =str(text).lower().strip()
    text =re.sub(r"[^\w\s&]"," ",text)
    text =text.replace("&","and")
    text =re.sub(r"\s+","",text).strip()
    text =re.sub(r"\b(ltd/plc/comany/limited/gmbh,corp/inc)\b","",text)
    text =re.sub(r"\s+","",text).strip()
    return text


df["publisher cleaned"]=df[publisher_col].apply(clean_publisher)


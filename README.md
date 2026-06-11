																													**Project Title - Open Research Excel Data Cleansing script**
								The scripts in this repository are to be used to perform basic Excel data cleansing tasks, particularly, filtering by variable and standardising values. **


								
<img width="381" height="223" alt="image" src="https://github.com/user-attachments/assets/e09e12d8-ade8-4dd8-9406-7b377e7ca225" />

<img width="368" height="192" alt="image" src="https://github.com/user-attachments/assets/bd62e064-c785-43a1-892d-7734bbc44303" />




**clean_eprints.py:**
-filters metadata to keep "conference_item", "exhibition", and "performance" records.
main steps involved:
-Read Excel -> filter "e_prints_type" with isin() -> export to Outputs -> New Excel file created. 



**standardisation_of_dates.py**
-standardises "event_dates_start" and "event_dates_end" to DD-MM-YYYY. 
main steps involved: 
-Read filtered Excel -> apply standardise_date using pd.to_datetime() -> export to Outputs -> New Excel File created. 



**activity_2_metadata_extract.py:** 
-filters metadata to keep only "article" and "conference_item" records. 
main steps involved:
-Read Excel -> filter "eprints_type" with isin() -> export to Outputs -> New Excel file created. 








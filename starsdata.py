from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge("C:/Users/DELL/Downloads/edgedriver_win64/msedgedriver")
browser.get(START_URL)

time.sleep(6)

stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
   
    
    
    soup = BeautifulSoup(browser.page_source , "html.parser")
    star_table = soup.find("table" , attrs = {"class" , "wikitable"})
    table_body = star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    
    for row in table_rows:
        table_coloumns = row.find_all('td')
        tempList = []
        for col in table_coloumns:
            data = col.text.strip()
            tempList.append(data)
        stars_data.append(tempList)

scrape()
           
stars_data_final = []
for i in range(0,len(stars_data)):
    star_name = stars_data[i][1]
    distance = stars_data[i][3]
    mass = stars_data[i][5]
    radius = stars_data[i][6]
    luminosity = stars_data[i][7]

    data = [star_name , distance , mass , radius , luminosity]
    stars_data_final.append(data)

headers = ["star_name" , "distance" , "mass" , "radius" , "luminosity"]

star_df = pd.DataFrame(stars_data_final , columns = headers )
star_df.to_csv("Starsdata.csv" , index = True , index_label = "id")


        
# Calling Method    


# Define Header


# Define pandas DataFrame   


# Convert to CSV

    



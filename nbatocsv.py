#Importing Json, requests and a variable for an NBA api key in another file, as well as pandas to manipulate data.
import json
import requests
from NbaAPIKey import NBA_key
import pandas as pd

url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key": NBA_key,
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}


response = requests.get(url, headers=headers, params=querystring).json()
#printing out the json data
#print(response.json())

#imported pandas module to manipulate data into a table
df = pd.DataFrame(response['data'])
print(df)

#used the df pandas variable to convert it to csv file and named it response_python.csv
df.to_csv('response_python.csv')

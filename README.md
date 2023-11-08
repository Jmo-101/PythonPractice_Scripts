# PythonPractice_Scripts

# Date_script.py

This script simulates a dating scenario where the user inputs their date's name and has a conversation about where they want to eat. The user also inputs and specifies their budget for the date. The script involves creating a list of menu items and their prices, while allowing the user to input their choice of food from the menu. The script utilizes the `time` and `pandas` imports, as well as if statements and while loops.

## Imports

```python
import time
import pandas as pd
```

# DictionaryJson.py

This script was used as practice to parse through json data. We initially started off with a string and used json to convert it into a python dictionary to make it easier to parse through. Afterwards I made a function that will output the number of healthy and unhealthy checks, and another function that will output the names of unhealthy checks. Lastly used a pandas dataframe import to format the data nicely.

## Imports
```python
import json
import pandas as pd
import numpy as np
```
# NBAtoCSV.py
This script demonstrated the usage of import modules such as json, requests and pandas. To start off I used an API to request data from NBArapidAPI, this data provided a list of all nba players in the NBA currently. To output this API data onto our console, I needed a key from rapidAPI. Once I got the key I made a variable on a seperate file and used an import module to grab the key variable from that file to use in our script. Afterwards, I used a json module to convert it to a python dictionary and it made it easier to parse through. I converted the outputted data into a table using a pandas dataframe, afterwards outputted the data table into a csv file.

## Imports
```python
import json
import pandas as pd
import requests
```

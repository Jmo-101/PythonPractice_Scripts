import os
import psutil
import csv
import json
#initializing an empty list to iterate through every object in the list
process_info =[]
for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'cpu_percent', 'memory_info']):
    process = [proc.info]
    process_info.append(process)
#checking to see if process_info is accurate
# print(process_info)

## creating a new csv to import info
with open('process.csv','w',newline='') as f:
    # what we are writing to
    w = csv.writer(f)
    # writing first column for csv file
    w.writerow(['pid','Name','Executable path','CPU percent usage','Memory Info (Resident Set Size, Virtual Memory Size, Shared, Text, Library, Data, Dirty)'])
    # adding info based on columnsand keep adding all processes to the empty list (process_info)
    for process in process_info:
        w.writerow([process[0]['pid'], process[0]['name'], process[0]['exe'], process[0]['cpu_percent'], process[0]['memory_info']])

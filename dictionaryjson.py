import json
import pandas as pd
import numpy as np

#code challenge parse status JSON
#make a function that will output the number of healthy and unhealthy checks
#make a function that will output the names of unhealthy checks

new = """
{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "uHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}

"""

# newV2 = json.loads(new)
# print(newV2)

def status_checks(new):
    #Used loads to parse through the Json data since it was in string format
    newv2 = json.loads(new)

#Created a counter to keep track of the healthy and unhealthy checks
    hcount= 0
    uncount = 0

    for machine in newv2["Checks"]:
        status = machine["Status"].lower()
        if status == "healthy":
            hcount =hcount+1
        elif status == "unhealthy":
            uncount =uncount+1    

    return hcount , uncount
hcount, uncount = status_checks(new)
print(f"healthy checks:{hcount}")
print(f"unhealthy checks:{uncount}")


def names_health(new):
    newv2 = json.loads(new)

#Created an empty list to add the names to later on
    unhealthy_names = [] 
    healthy_names = []   

#Created a for loop to reiterate through the Json dictionary for the names
    for machine in newv2["Checks"]:
        if machine["Status"].lower() == "unhealthy":
            unhealthy_names.append(machine["Name"])
        elif machine["Status"].lower() == "healthy":
            healthy_names.append(machine["Name"])


    return unhealthy_names , healthy_names

#Called back to the function with the variable 
unhealthy_names , healthy_names = names_health(new)
#print(unhealthy_names) 
#print(healthy_names)              

joint = pd.DataFrame({"Healthy":healthy_names,})
joint2 = pd.DataFrame({"Unhealthy":unhealthy_names})
#print(joint)
#print(joint2)

result = pd.concat([joint,joint2])
#result2 = result.dropna()
result2 = result.replace([np.nan, -np.inf], 0)
print(result2)

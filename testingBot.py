import requests
import json
allUSStatesArray = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']
def check():
   url = "https://covidtracking.com/api/states"

   payload = {}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   print(response.text.encode('utf8'))

   to_python_JSONFILE = json.loads(response.text.encode('utf8'))
   userChoice = input("Please type state abbreviation")
   indexOfState = 1
   for x in range (0,len(allUSStatesArray)):
       if userChoice == allUSStatesArray[x]:
           indexOfState = x

   print(to_python_JSONFILE[indexOfState])
   allStateInfo = to_python_JSONFILE[indexOfState]
   print(allStateInfo['negative'])


check()

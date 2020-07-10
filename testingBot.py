import requests
import json

allUSStatesSpelledOutArray = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", " ", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
allUSStatesArray = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO','MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']

def check():
   print(len(allUSStatesSpelledOutArray))
   print(len(allUSStatesArray))
   for x in range (0, len(allUSStatesArray)):
      print(allUSStatesArray[x])
      # print(allUSStatesSpelledOutArray[x])
   # print(allUSStatesArray[1])
   # print(allUSStatesSpelledOutArray[1])
   url = "https://covidtracking.com/api/states"

   payload = {}
   headers = {}

   response = requests.request("GET", url, headers=headers, data=payload)

   print(response.text.encode('utf8'))


   print("next one here")
   to_python_JSONFILE = json.loads(response.text.encode('utf8'))
   print(len(to_python_JSONFILE))
   for x in range (0,len(to_python_JSONFILE)):
      print(to_python_JSONFILE[x]['state'])

   userChoice = input("Please type state abbreviation")
   indexOfState = 1
   for x in range (0,len(allUSStatesArray)):
       if userChoice == allUSStatesArray[x]:
           indexOfState = x

   print(to_python_JSONFILE[indexOfState])
   allStateInfo = to_python_JSONFILE[indexOfState]
   print(allStateInfo['negative'])


check()

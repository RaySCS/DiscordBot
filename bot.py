import discord
import logging
import aiohttp
import json
import requests
from datetime import date

today = date.today()

logging.basicConfig(level=logging.INFO)

client = discord.Client()
allUSStatesSpelledOutArray = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", " ", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
allUSStatesArray = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO','MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']

@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
   if message.author == client.user:
       return

   if message.content.startswith('$hello'):
       await message.channel.send('Hello {0.author}!'.format(message))

   if "wave to me" in message.content:
       await message.add_reaction('👋')

   if "how are you doing" in message.content:
       await message.channel.send("Nothing much")

   # if "cat" in message.content:
   #     async with aiohttp.ClientSession() as session:
   #         async with session.get('http://aws.random.cat/meow') as r:
   #             if r.status == 200:
   #                 json = await r.json()
   #                 await message.channel.send(json['file'])

   #actual below
   #covid: il
   if "!help" in message.content:
       await message.channel.send("`COVID-19 BOT`")
       await message.channel.send("-----------------------------------")
       await message.channel.send("Please Follow the Syntax: covid [state abbreviation or name]")
       await message.channel.send("Once you enter which state, you will be returned with information regarding the COVID-19 Situation in your state")

   if "covid" in message.content or "Covid" in message.content or "COVID" in message.content:
       print(message.content)
       stateDescribed = message.content[7:len(message.content)]
       # await message.channel.send("you described " + stateDescribed)

       url = "https://covidtracking.com/api/states"

       payload = {}
       headers = {}

       response = requests.request("GET", url, headers=headers, data=payload)

       print(response.text.encode('utf8'))
       foundState = False

       to_python_JSONFILE = json.loads(response.text.encode('utf8'))
       indexOfState = -1
       for x in range(0, len(allUSStatesArray)):
           if stateDescribed == allUSStatesArray[x]:
               foundState = True
               indexOfState = x
               print("Index found: " + str(indexOfState))

       if not foundState:
           for x in range(0, len(allUSStatesSpelledOutArray)):
               if stateDescribed == allUSStatesSpelledOutArray[x]:
                   foundState = True
                   indexOfState = x
                   print("Index found: " + str(indexOfState))

       if foundState:
           print(to_python_JSONFILE[indexOfState])
           allStateInfo = to_python_JSONFILE[indexOfState]
           print(allStateInfo['positive'])
           dateFormated = today.strftime("%b-%d-%Y")#date format
           await message.channel.send("`" + str(stateDescribed + " ALL INFORMATION AS OF " + dateFormated) + "`")
           await message.channel.send("-----------------------------------")
           await message.channel.send(str(stateDescribed) + " Total Positive Cases:  " + str(allStateInfo['positive']))
           await message.channel.send(str(stateDescribed) + " Total Negative Cases:  " + str(allStateInfo['negative']))
           await message.channel.send(str(stateDescribed) + " Citizens Hospitalized Currently:  " + str(allStateInfo['hospitalizedCurrently']))
           await message.channel.send(str(stateDescribed) + " Citizens Recovered Today:  " + str(allStateInfo['recovered']))
       else:
           await message.channel.send("Please re-type your command.")
           await message.channel.send("Plesae Follow the Syntax: Covid [state abbreviation or name]")
token_file = open("token", "r")#Load in the token file
contents = token_file.read()

#user types 'covid: state'
#bot returns the number of cases

client.run(contents)

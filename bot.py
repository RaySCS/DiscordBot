import discord
import logging
import aiohttp
import json
import requests
from datetime import date

today = date.today()

logging.basicConfig(level=logging.INFO)

client = discord.Client()
allUSStatesArray = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']


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
   if "covid" in message.content:
       print(message.content)
       stateDescribed = message.content[7:len(message.content)]
       # await message.channel.send("you described " + stateDescribed)

       url = "https://covidtracking.com/api/states"

       payload = {}
       headers = {}

       response = requests.request("GET", url, headers=headers, data=payload)

       print(response.text.encode('utf8'))

       to_python_JSONFILE = json.loads(response.text.encode('utf8'))
       indexOfState = -1
       for x in range(0, len(allUSStatesArray)):
           if stateDescribed == allUSStatesArray[x]:
               indexOfState = x
               print("Index found: " + str(indexOfState))

       print(to_python_JSONFILE[indexOfState])
       allStateInfo = to_python_JSONFILE[indexOfState]
       print(allStateInfo['positive'])
       dateFormated = today.strftime("%b-%d-%Y")#date format
       await message.channel.send(str(stateDescribed + " ALL INFORMATION AS OF " + dateFormated))
       await message.channel.send("-----------------------------------")
       await message.channel.send(str(stateDescribed) + " Total Positive Cases:  " + str(allStateInfo['positive']))
       await message.channel.send(str(stateDescribed) + " Total Negative Cases:  " + str(allStateInfo['negative']))
       await message.channel.send(str(stateDescribed) + " Citizens Hospitalized Currently:  " + str(allStateInfo['hospitalizedCurrently']))
       await message.channel.send(str(stateDescribed) + " Citizens Recovered Today:  " + str(allStateInfo['recovered']))

token_file = open("token", "r")#Load in the token file
contents = token_file.read()

#user types 'covid: state'
#bot returns the number of cases

client.run(contents)

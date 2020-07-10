import discord
import logging
import aiohttp

logging.basicConfig(level=logging.INFO)

client = discord.Client()

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

    if "cat" in message.content:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    json = await r.json()
                    await message.channel.send(json['file'])

    #actual below
    #covid: il
    if "covid" in message.content:
        print(message.content)
        stateDescribed = message.content[7:len(message.content)]
        await message.channel.send("you described " + stateDescribed)


token_file = open("token", "r")#Load in the token file
contents = token_file.read()

#user types 'covid: state'
#bot returns the number of cases

client.run(contents)

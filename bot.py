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

    messageKey = "kakashi"
    if messageKey in message.content:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/',messageKey) as r:
                if r.status == 200:
                    json = await r.json()
                    await message.channel.send(json['file'])

token_file = open("token", "r")
contents = token_file.read()

client.run(contents)

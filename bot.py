import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("message received", message)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello {0.author}!'.format(message))

client.run('NzMwOTIyNjMwMTIyNzAwODcw.XwejLA.7OwZgpiUzMhD8np0TIjQqkripJc')

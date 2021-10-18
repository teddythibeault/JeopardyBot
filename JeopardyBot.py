import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('j!animeq'):
        await message.channel.send('Here is your anime trvia question:')
        
    if message.content.startswith('j!q'):
        await message.channel.send('Here is your Jeopardy question:')

client.run(os.environ['BOT_TOKEN'])

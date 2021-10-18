import discord
import os
from dotenv import load_dotenv
<<<<<<< HEAD
from discord.ext import commands
from requests import get




load_dotenv()

#client = discord.Client()
bot = commands.bot(command_prefix ='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot.user))

@bot.command(name="animeq", help="Provides an anime trivia question, courtesy of opentdb.com")
async def animeq(ctx):
    '''if message.author == client.user:
=======

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
>>>>>>> 003a4f2b2f93a49963d33c6330734f61ba0fdf8b
        return

    if message.content.startswith('j!animeq'):
        await message.channel.send('Here is your anime trvia question:')
        
    if message.content.startswith('j!q'):
<<<<<<< HEAD
        await message.channel.send('Here is your Jeopardy question:')'''

    await ctx.send("Here's your anime trivia question:\n")

    request = get('https://opentdb.com/api.php?amount=1&category=31'.json())
    difficulty = request.get("results")[0].get("difficulty")
    question = request.get("results")[0].get("question")
    correct_answer = request.get("results")[0].get("correct_answer")
    incorrect_answers = request.get("results")[0].get("incorrect_answers")

    await ctx.send("The difficulty is " + difficulty)
    await ctx.send("The question is " + question)
    await ctx.send("The correct answer is " + correct_answer)

bot.run(os.environ['BOT_TOKEN'])
=======
        await message.channel.send('Here is your Jeopardy question:')

client.run(os.environ['BOT_TOKEN'])
>>>>>>> 003a4f2b2f93a49963d33c6330734f61ba0fdf8b

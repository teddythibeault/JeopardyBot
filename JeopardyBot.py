import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import requests




load_dotenv()

#client = discord.Client()
bot = commands.bot(command_prefix ='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot.user))

@bot.command(name="animeq", help="Provides an anime trivia question, courtesy of opentdb.com")
async def animeq(ctx):
    
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

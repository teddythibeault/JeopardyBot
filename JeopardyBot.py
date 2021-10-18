import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import requests
import json
import html




load_dotenv()

#client = discord.Client()
bot = commands.Bot(command_prefix ='!')


emojis = ['🇦', '🇧', '🇨', '🇩']

request = requests.get('https://opentdb.com/api.php?amount=1&category=31').json()
    
questionlist = [None, None, None, None, None]
questionlist[0] = request.get("results")[0].get("difficulty")
questionlist[1] = request.get("results")[0].get("question")
questionlist[2] = request.get("results")[0].get("correct_answer")
questionlist[3] = request.get("results")[0].get("incorrect_answers")
questionlist[4] = request.get("results")[0].get("type")

for i, string in enumerate(questionlist[0:2]):
    questionlist[i] = html.unescape(string)
for i, string in enumerate(questionlist[3]):
    questionlist[3][i] = html.unescape(string)


answerset = {questionlist[2], questionlist[3][0], questionlist[3][1], questionlist[3][2]}

answerdict = {}
for emoji in emojis:
    answerdict[emoji] = answerset.pop()



@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

@bot.command(name="animeq", help="Provides an anime trivia question, courtesy of opentdb.com")
async def animeq(ctx):
    
    
    embed=discord.Embed(title='Q: ' + questionlist[1], url="https://cdn.discordapp.com/emojis/806616122228080650.png?size=128", description="", color=0xFF5733)
    for emoji in emojis:
        embed.add_field(name = emoji, value = answerdict.get(emoji), inline = False)
    
    embed.set_footer(text="Question courtesy of OpenTDB. Requested by: {}".format(ctx.author.display_name))
    question = await ctx.send(embed=embed)
    
    for emoji in emojis:
        await question.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    if answerdict[reaction.emoji] == questionlist[2]:
        
        await reaction.message.channel.send("Congratulations {}, that is correct!".format(user.display_name))
    else: 
        await reaction.message.channel.send("Sorry {}, that is not correct.".format(user.display_name))


bot.run(os.environ['BOT_TOKEN'])
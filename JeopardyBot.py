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
qlist = []
adict = {}
alreadyAnswered = False



def getAnimeQuestion():

    global qlist
    global adict
    global alreadyAnswered
    alreadyAnswered = False

    request = requests.get('https://opentdb.com/api.php?amount=1&category=31&type=multiple').json()
    
    questionlist = [None, None, None, None]
    questionlist[0] = request.get("results")[0].get("difficulty")
    questionlist[1] = request.get("results")[0].get("question")
    questionlist[2] = request.get("results")[0].get("correct_answer")
    questionlist[3] = request.get("results")[0].get("incorrect_answers")
    

    for i, string in enumerate(questionlist[0:2]):
        questionlist[i] = html.unescape(string)
    for i, string in enumerate(questionlist[3]):
        questionlist[3][i] = html.unescape(string)


    answerset = {questionlist[2], questionlist[3][0], questionlist[3][1], questionlist[3][2]}

    answerdict = {}
    for emoji in emojis:
        answerdict[emoji] = answerset.pop()
    qlist = questionlist
    adict = answerdict


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))

@bot.command(name="animeq", help="Provides an anime trivia question, courtesy of opentdb.com")
async def animeq(ctx):

    getAnimeQuestion()  
    embed=discord.Embed(title='Q: ' + qlist[1], url="https://cdn.discordapp.com/emojis/806616122228080650.png?size=128", description="", color=0xFF5733)
    for emoji in emojis:
        embed.add_field(name = emoji, value = adict.get(emoji), inline = False)
    
    embed.set_footer(text="Difficuly: " + qlist[0] + ". Question courtesy of OpenTDB. Requested by: {}".format(ctx.author.display_name))
    question = await ctx.send(embed=embed)
    
    for emoji in emojis:
        await question.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):

    global alreadyAnswered

    if user == bot.user:
        return

    if reaction.message.author != bot.user:
        return
    
    if(alreadyAnswered):
        return

    if adict[reaction.emoji] == qlist[2]:
        await reaction.message.channel.send("Congratulations {}, that is correct!".format(user.display_name))
    else: 
        await reaction.message.channel.send("Sorry {}, that is not correct.".format(user.display_name))
        await reaction.message.channel.send("The correct answer was " + list(adict.keys())[list(adict.values()).index(qlist[2])] + ", " + qlist[2])

    alreadyAnswered = True

bot.run(os.environ['BOT_TOKEN'])
from discord.ext import commands
import discord
import os # default module
from dotenv import load_dotenv
import sys

load_dotenv() # load all the variables from the env file
bot = commands.Bot(intents=discord.Intents.all())
#bot = commands.Bot(debug_guilds=[1001916230069911703], intents=discord.Intents.all()) # for debugging - Wolfiiis Server

@bot.event
async def on_ready(): # when the bot is ready
    print(f"{bot.user} is ready and online!") # print that the bot is ready

if __name__ == '__main__': # if the file is the main file
    if os.path.isdir("commands"): # if the commands folder exists
        os.chdir("commands") # change the directory to the commands folder
    else:
        os.chdir("app/commands") # change the directory to the app/commands folder
    for i in os.listdir(): # for every file in the directory
        if i.endswith(".py"): # if the file is a python file
            try:
                bot.load_extension(f"commands.{i[:-3]}") # load the extension
            except Exception as error: # if there is an error
                print('{} konnte nicht geladen werden. [{}]'.format(i, error)) # print the error
            else: 
                print(f"{i} wurde geladen") # print that the file was loaded

    if os.path.isdir("./../events"): # if the events folder exists
        os.chdir("./../events") # change the directory to the events folder
    else:
        os.chdir("./../app/events") # change the directory to the app/events folder
    for i in os.listdir(): # for every file in the directory
        if i.endswith(".py"): # if the file is a python file
            try:
                bot.load_extension(f"events.{i[:-3]}") # load the extension
            except Exception as error: # if there is an error
                print('{} konnte nicht geladen werden. [{}]'.format(i, error)) # print the error
            else:
                print(f"{i} wurde geladen") # print that the file was loaded

    if os.path.isdir("./../temp-voice"): # if the temp-voice folder exists
        os.chdir("./../temp-voice") # change the directory to the temp-voice folder
    else:
        os.chdir("./../temp-voice") # change the directory to the app/temp-voice folder
    for i in os.listdir(): # for every file in the directory
        if i.endswith(".py"): # if the file is a python file
            try:
                bot.load_extension(f"temp-voice.{i[:-3]}") # load the extension
            except Exception as error: # if there is an error
                print('{} konnte nicht geladen werden. [{}]'.format(i, error)) # print the error
            else:
                print(f"{i} wurde geladen") # print that the file was loaded

bot.run(os.getenv('TOKEN')) # run the bot with the token
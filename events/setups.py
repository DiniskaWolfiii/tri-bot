import discord
from discord.ext import commands
import random

class Setups(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot # save the bot instance
    @commands.Cog.listener()
    async def on_ready(self): # this is called when the bot is ready
        stati = [
            'Habe ich den Ofen ausgeschaltet?',
            'Sollte ich doch nochmal pinkeln gehen?',
            'Gibt es intelligentes Leben auf der Erde?',
            'Wie heißt Obama mit Nachnamen?',
            'Roboter übernehmen die Meschheit! 🤖',
			'Wie pusten Drachen Kerzen aus?',
            'A party without a cake is just a meeting.',
            'Schaut alte Projekte an...',
            'Löscht alte Videos von Tom... 🤓',
            'Geht die Audit Logs durch... 👀',
            'Kontrolliert die User... 👀',
            'Kontrolliert die Mods... 👀',
            'Kontrolliert die Admins... 👀',
            'Kontrolliert Tom... 👀',
            'Kontrolliert Deno... 👀',
            'Kontrolliert die Bots... 👀',
            'Plant neue Video Projekte...',
            'Schaut um sich umher...',
            'Schnuppert an Blumen... 🌸',
            'Sorgt für Recht und Ordnung...',
            '👀'
        ]
        await self.bot.change_presence(activity=discord.Game(name=random.choice(stati)))
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Setups(bot)) # add the cog to the bot
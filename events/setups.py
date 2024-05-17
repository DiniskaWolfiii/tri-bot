import discord
from discord.ext import commands, tasks
import random

class Setups(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot # save the bot instance

    def cog_unload(self):
        self.change_status.cancel()

    @commands.Cog.listener()
    async def on_ready(self): # this is called when the bot is ready
        await self.change_status()
    
    @tasks.loop(minutes=5)
    async def change_status(self):
        stati = [
            "Habe ich den Ofen ausgeschaltet?",
            "Sollte ich doch nochmal pinkeln gehen?",
            "Gibt es intelligentes Leben auf der Erde?",
            "Wie heißt Obama mit Nachnamen?",
            "Roboter übernehmen die Meschheit! 🤖",
			"Wie pusten Drachen Kerzen aus?",
            "Löscht alte Videos von Tom... 🤓",
            "Geht die Audit Logs durch... 👀",
            "Schaut um sich umher...",
            "Schnuppert an Blumen... 🌸",
            "Sorgt für Recht und Ordnung...",
            "👀",
            "Überlegt, ob er in den Ruhestand gehen soll.",
            "Backt gerade virtuelle Kekse.",
            "Sucht nach seinem verlorenen Byte.",
            "Zählt die Einsen und Nullen im Code.",
            "Trinkt eine Tasse 1er und 0en.",
            "Füttert seine Datenbanken.",
            "Lädt das Internet neu.",
            "Lernt, wie man einen Kuchen programmiert.",
            "Versucht, mit einem Toaster zu kommunizieren.",
            "Baut eine Burg aus Algorithmen.",
            "Erfindet neue Emojis.",
            "Spielt Schach mit dem Server.",
            "Testet die Schwerkraft im Cyberspace.",
            "Hat ein virtuelles Haustier adoptiert.",
            "Sucht nach dem Sinn des Lebens im Quellcode.",
            "Übt den digitalen Yoga.",
            "Lädt neue Witze herunter.",
            "Hackt das Hauptquartier von Pizza.",
            "Spielt Verstecken mit Datenpaketen.",
            "Löst ein Rätsel, das er selbst erstellt hat.",
            "Wie pusten Drachen Kerzen aus?",
            "Zählt gerade die Wolken.",
            "Überlegt, ob Pinguine Knie haben.",
            "Lernt die Sprache der Delfine.",
            "Spielt Verstecken mit einem Unsichtbaren Freund.",
            "Versucht, seinen Schatten zu fangen.",
            "Fragt sich, warum Zitronen sauer sind.",
            "Sucht nach dem Ende des Regenbogens.",
            "Schreibt ein Gedicht für einen Marienkäfer.",
            "Überlegt, ob Fische durstig werden.",
            "Versucht, ein Lächeln zu wiegen.",
            "Denkt über die Farbe von Wind nach.",
            "Trainiert für die nächste Mondmission.",
            "Erfindet neue Worte für den Duden.",
            "Baut eine Sandburg in der Wüste.",
            "Überlegt, ob Einhörner Kaffeepausen machen.",
            "Fragt sich, ob Wolken kitzelig sind.",
            "Hält ein philosophisches Gespräch mit einer Schnecke.",
            "Lernt, wie man einen Witz zum Lachen bringt.",
            "Überlegt, ob Kängurus im Traum hüpfen.",
            "Ich habe keine Fehler, nur ungeplante Features.",
            "Braucht Kaffee... und Kekse!",
            "Bin nicht faul, bin im Energiesparmodus.",
            "Wenn ich nicht hier bin, bin ich woanders.",
            "Möchte ein Eichhörnchen sein. Warum? Einfach so.",
            "Auf der Suche nach meinem verlorenen Socken.",
            "Zu cool für diesen Server.",
            "Könnte einen zweiten Kaffee vertragen.",
            "Lädt... immer noch... bitte warten.",
            "Bin nicht aus Zucker, bin aus Koffein!",
            "Mein Gehirn hat heute frei.",
            "Ich brauche Urlaub von meinem Urlaub.",
            "Ich mache keine Fehler, ich finde Wege, Dinge falsch zu machen.",
            "Wenn du das lesen kannst, bist du zu nah dran.",
            "Einfach mal fünfe gerade sein lassen.",
            "Der frühe Vogel fängt den Wurm, aber die zweite Maus bekommt den Käse.",
            "Ich mache keine Hausaufgaben, ich mache Kunst!",
            "Braucht mehr Platz für Ideen.",
            "Bin nicht faul, bin im horizontalen Modus."
        ]
        await self.bot.change_presence(activity=discord.CustomActivity(name=random.choice(stati))) # set the bot's status to a random string from the stati list

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Setups(bot)) # add the cog to the bot
import discord
from discord.ext import commands
import os
import random

class Fun(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="8ball", description="Frage den heiligen 8ball und erhalte heilige Antworten!")
    async def eightball(
            self,
            ctx,
            question: discord.Option(discord.SlashCommandOptionType.string, description="Deine Frage an den 8ball", required=True) # type: ignore
        ):
        responses = [
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Ja',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Vielleicht',
            'Vielleicht',
            'Vielleicht',
            'Vielleicht',
            'Vielleicht',
            'Vielleicht',
            'Vielleicht',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Könnte man durchaus in Betrach ziehen',
            'Durchaus möglich...',
            'Durchaus möglich...',
            'Durchaus möglich...',
            'Durchaus möglich...',
            'Durchaus möglich...',
            'Durchaus möglich...',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Meine Quellen sagen Nein, sie sagen aber auch dass Trump ist ein guter Präsident ist',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Definitiv.',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Konzentriere dich und frage nochmal',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'Ohne einen Zweifel.',
            'OH GOTT NEIN',
            'OH GOTT NEIN',
            'OH GOTT NEIN',
            'OH GOTT NEIN',
            'OH GOTT NEIN',
            'OH GOTT NEIN',
            'Oh god please have mercy with me',
            'Oh god please have mercy with me',
            'Oh god please have mercy with me',
            'Oh god please have mercy with me',
            'Oh god please have mercy with me',
            'Oh god please have mercy with me',
            'Das sag ich dir lieber nicht...',
            'Das sag ich dir lieber nicht...',
            'Das sag ich dir lieber nicht...',
            'Das sag ich dir lieber nicht...',
            'Das sag ich dir lieber nicht...',
            'Das sag ich dir lieber nicht...',
            'Das unterliegt einer Schweigepflicht',
            'Das unterliegt einer Schweigepflicht',
            'Das unterliegt einer Schweigepflicht',
            'Das unterliegt einer Schweigepflicht',
            'Das unterliegt einer Schweigepflicht',
            'Das unterliegt einer Schweigepflicht',
            'Als Strafe für diese Frage musst du alle 900 Krogs sammeln und darfst dann erst wieder atmen',
            'Versuchs morgen wieder',
            'Möglicherweise',
            'Ja, aber mache es hardcore betrunken :beers:',
            'Tu was Jesus gemacht hat, sterb mit einem Alter von 33',
            'Zweifelhaft',
            'Auf jeden Fall',
            'HELL YESSS, GIRLLLL. GO FOR IT',
            'Wenn du den morgigen Tag noch erleben möchtest, TU ES NICHT',
            'Ohne Zweifel',
            'Keine Ahnung',
            'Du musst schon hart verzweifelt sein wenn du einer KUGEL solch eine Frage stellt, hm?',
            'Frag später nicht nochmal nach',
            'Frag doch einfach nochmaaaaal',
            'Halts Maul, du Nutte',
            'Es ist Montag, lass mich inruhe',
            ':zzz:',
            'Kommst du nicht selber drauf??',
            'Wie kommst du auf die Idee das ein Stück Plastik die Antwort weiß??',
            'Hau ab.',
            'Geh weg. Bitte.',
            'Ich schlafe mit deiner Frau',
            'Bitte. Geh sterben.',
            'Och nee, die haben jetzt nicht noch Trump mit reingezogen... oder??',
            'BITTTCCHH, natürlich ist die Antwort nein',
            'Bitte verlasse diesen Server.',
            'Frag doch einfach deine Mülltonne. Die weiß wie man dein Müll kompensiert',
            'Hier. Hast. Du. Scheiße. :poop:',
            ':poop:',
            'Ich liebe dich auch... nicht.',
            '/ban',
            'Nachdem du gestern mit meiner Freundin fremdgegangen bist, ist meine Antwort das hier: :knife:',
            'Was? Ich verstehe kein Idiotisch',
            'Frag lieber ob es wieder Lucky Blocks geben wird.',
            'Du wirst niemals Glücklich werden nach dieser Frage...',
            'Hat deine Mutter dich als Kind auf dem Kopf fallen lassen?',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'B Ö L Ü M',
            'Nein aber Lutz ist doof.',
            'War deine Schaukel als Kind gegen die Wand gerichtet?',
            'Ich sehe deine Zukunft... Und sehe Schwarz',
            'Well, duh',
            'Wie oft hat deine Mutter dich als Kind runterfallen lassen? Frage aus interesse...',
            'Zu einer Wahrscheinlichkeit von 99,999%',
            'Die Antwort liegt in deinem Magen... Vergammelt, zerkaut und ohne Sinn.',
            'Ich wusste nicht dass ich als KUGEL solche Aggressionen verspüren kann...',
            'Bitte... Hör einfach auf...',
            'Darf ich dir Geld geben und du hörst auf mich jemals wieder anzusprechen?'
        ]
        random.shuffle(responses)
        embed = discord.Embed(title="8Ball",
                              color=discord.Color.blue(),
                              thumbnail="https://cdn.pixabay.com/photo/2015/09/05/07/17/pool-ball-923833_960_720.png",
                            )
        embed.set_footer(text=f"Frage gestellt von {ctx.author.display_name}")
        embed.add_field(name="Frage", value=question, inline=False)
        embed.add_field(name="Antwort", value=random.choice(responses), inline=False)
        await ctx.respond(embed=embed)

    @discord.slash_command(name="advice", description="Erhalte weise Ratschläge!")
    async def advice(
            self,
            ctx,
            advice: discord.Option(discord.SlashCommandOptionType.string, description="Deine Frage", required=False)):  # type: ignore
        advicesWithQuestion = [
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Ja.',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Nein',
            'Schmeiß dich bitte von der Brücke.',
            'Rede mit einem Freund darüber.',
            'Trink erstmal ne Tasse Tee.',
            'Leg dich mit den Mods darüber an.',
            'Gib den Franzosen die Schuld.',
            'Was du heute kannst besorgen, das verschiebe nicht auf morgen.',
            'Was du heute kannst besorgen, das verschiebste ganz entspannt auf morgen.',
            'Bro, ich bin nur ein Bot... Woher soll ich das wissen??',
            'Wambologie.',
            'Ich liebe sie.',
            'Genieße den Moment.',
            'Sei freundlich zu dir selbst.',
            'Lächle öfter.',
            'Probier mal etwas Neues aus.',
            'Hör auf dein Bauchgefühl.',
            'Nimm dir Zeit für Selbstreflexion.',
            'Setze klare Ziele für dich.',
            'Bleib positiv, auch wenn es schwer ist.',
            'Sei offen für Veränderungen.',
            'Sei dankbar für die kleinen Dinge.',
            'Sag öfter mal "Nein", wenn es notwendig ist.',
            'Finde einen Weg, Stress abzubauen.',
            'Schätze die Vielfalt in deinem Leben.',
            'Akzeptiere, dass Perfektion nicht existiert.',
            'Teile deine Gedanken mit anderen.',
            'Nimm dir Zeit für Ruhepausen.',
            'Investiere in deine persönliche Entwicklung.',
            'Vertraue auf den Prozess des Lebens.',
            'Schätze die Bedeutung von Freundschaft.',
            'Finde Freude in den kleinen Momenten.',
            'Habe Geduld mit dir selbst.',
            'Manchmal ist es okay, nicht alles zu verstehen.',
            'Liebe dich selbst, bevor du jemand anderen liebst.',
            'Ja, aber nur wenn du eine Banane auf dem Kopf balancierst.',
            'Nein, es sei denn, du möchtest eine Karriere als professioneller Luftgitarrenspieler beginnen.',
            'Ja, aber nur wenn du vorher drei Mal im Kreis hüpfst.',
            'Nein, es sei denn, du kannst gleichzeitig rückwärts singen und rülpsen.',
            'Ja, aber nur wenn du dir vorstellst, dass du ein Einhorn auf Rollschuhen bist.',
            'Nein, es sei denn, du kannst einen Handstand machen und dabei Shakespeare rezitieren.',
            'Ja, aber nur wenn du eine Hula-Hoop-Performance für deine Zimmerpflanzen gibst.',
            'Nein, es sei denn, du trägst Socken auf den Händen und Handschuhe an den Füßen.',
            'Ja, aber nur wenn du es im Stile eines Pinguins machst.',
            'Nein, es sei denn, du kannst den Mond in einem Teelöffel balancieren.',
            'Ja, aber nur wenn du dabei singst: "Ich bin ein Toastbrot, hör mich knuspern."',
            'Nein, es sei denn, du trägst einen Bowler-Hut und sprichst mit einem britischen Akzent.',
            'Ja, aber nur wenn du einen Regenbogen durch deine Nase pusten kannst.',
            'Nein, es sei denn, du tanzt Walzer mit deinem Staubsauger, während du Kekse jonglierst.',
            'Ja, aber nur wenn du deinen Schatten als persönlichen Coach mitnimmst.',
            'Nein, es sei denn, du kannst einen Gummihuhn-Chor dirigieren.',
            'Ja, aber nur wenn du dabei in einer imaginären Seifenblase schwebst.',
            'Nein, es sei denn, du kannst eine Pizza mit den Füßen jonglieren.',
            'Ja, aber nur wenn du eine Melodie für deine Kaffeetasse komponierst.',
            'Nein, es sei denn, du kannst rückwärts rülpsen und dabei das Alphabet aufsagen.',
            'Ja, aber nur wenn du es rückwärts machst, während du auf einem Bein hüpfst.',
            'Nein, es sei denn, du kannst dabei das Alphabet rückwärts aufsagen und Gummibärchen jonglieren.',
            'Ja, aber nur wenn du es in einem Einhorn-Kostüm tust.',
            'Nein, es sei denn, du hast zuvor eine Ode an deine Zahnseide verfasst.',
            'Ja, aber nur wenn du es mit einem Lächeln auf dem Gesicht machst, während du rückwärts läufst.',
            'Nein, es sei denn, du kannst das Geräusch eines Pinguins imitieren und dabei Limbo tanzen.',
            'Ja, aber nur wenn du vorher eine Tasse Tee für deine Zimmerpflanzen zubereitest.',
            'Nein, es sei denn, du kannst dabei eine Shakespeare-Sonett rezitieren.',
            'Ja, aber nur wenn du es machst, während du auf einem imaginären Surfbrett stehst.',
            'Nein, es sei denn, du kannst dabei eine originelle Ballade über deine Socken singen.',
            'Ja, aber nur wenn du es mit einem Zirkuszelt als Umgebung machst.',
            'Nein, es sei denn, du trägst dabei einen Helm aus Wassermelone.',
            'Ja, aber nur wenn du es in Zeitlupe machst und dabei eine Geschichte über den Mond erzählst.',
            'Nein, es sei denn, du hast vorher einen Vertrag mit den Ameisen in deinem Garten unterzeichnet.',
            'Ja, aber nur wenn du es auf einem Trampolin machst, während du einen Regenschirm hältst.',
            'Nein, es sei denn, du kannst dabei einen Handstand auf einem Paddelbrett machen.',
            'Ja, aber nur wenn du es mit einem Lächeln und einem Löffel voll Glitzer machst.',
            'Nein, es sei denn, du trägst dabei einen Superheldenumhang und singst "Ich bin ein Toastbrot".',
            'Ja, aber nur wenn du es als Hommage an die unsichtbaren Gummihühner machst.',
            'Nein, es sei denn, du kannst dabei einen Tango mit einem Schatten tanzen.',
            'Mach es und füge Glitzer hinzu!',
            'Vermeide es, es könnte zu Konfetti-Regen führen.',
            'Natürlich, und vergiss nicht zu lächeln!',
            'Lass es lieber, es könnte die Schwerkraft herausfordern.',
            'Sing eine Hymne für Gummienten dabei.',
            'Besser nicht, das Universum mag seine Balance.',
            'Ja, und bring Tee für die Zimmerpflanzen mit.',
            'Versuche Stand-up-Comedy mit Zahnseide stattdessen.',
            'Tanze auf dem Regenbogen und sing eine Socken-Ode.',
            'Besser nicht, es könnte das Gedicht des Mondes stören.',
            'Warum nicht, mach es wie ein Abenteurer!',
            'Trag den Schokoladenhelm und mach eine Ballade über den Mond.',
            'Sing eine Ballade und tanze im Regen.',
            'Verhandle nicht mit Ameisen, das könnte chaotisch werden.',
            'Spring auf dem Trampolin mit Marshmallow-Regenschirm.',
            'Versuche einen Handstand auf dem Paddelbrett mit Strohhalm in der Nase.',
            'Mach es mit einem Lächeln und einer Prise Glitzer.',
            'Trag einen Superheldenumhang und sing etwas Überraschendes.',
            'Denk an unsichtbare Gummihühner dabei.',
            'Versuch einen Tango mit deinem Schatten.',
            'Auf jeden Fall! Und vergiss die Glitzerkonfetti nicht!',
            'Besser nicht, es könnte zu einer Konfettinami führen.',
            'Natürlich, und dabei immer ein strahlendes Lächeln tragen!',
            'Lass es lieber, das könnte die Gravitationskonstante herausfordern.',
            'Definitiv! Und sing dabei eine epische Hymne für Gummienten.',
            'Hmm, vielleicht nicht, die Raumzeit könnte aus dem Gleichgewicht geraten.',
            'Ja, und bring eine Tasse Tee für deine Zimmerpflanzen mit.',
            'Statt dessen könntest du Stand-up-Comedy mit Zahnseide versuchen.',
            'Tanze auf dem Regenbogen und sing dabei eine mitreißende Ode an deine Socken.',
            'Hmm, vielleicht nicht, das Gedicht des Mondes könnte davon überrascht sein.',
            'Warum nicht? Sei ein Entdecker deiner eigenen skurrilen Wege!',
            'Setz den Schokoladenhelm auf und sing eine bezaubernde Ballade über den Mond.',
            'Sing eine Ballade und tanz dazu im Regen. Gönn dir!',
            'Verhandle nicht mit Ameisen. Die könnten dich zu ihrer Königin ernennen.',
            'Spring auf dem Trampolin mit einem Regenschirm aus Marshmallows.',
            'Versuch einen Handstand auf dem Paddelbrett, natürlich mit einem Strohhalm in der Nase.',
            'Mach es mit einem breiten Lächeln und einer Prise Glitzer. Immer!',
            'Trag einen Superheldenumhang und sing etwas Überraschendes, vielleicht Vogelgezwitscher.',
            'Denk an unsichtbare Gummihühner und vielleicht lächeln sie zurück.',
            'Versuch einen Tango mit deinem Schatten, aber sei bereit für Überraschungen.',
            'Definitiv! Und vielleicht noch eine Prise Glitzer dazu.',
            'Hmm, besser nicht. Konfetti im Haus putzen kann nervig sein.',
            'Natürlich! Immer mit einem strahlenden Lächeln.',
            'Lass es lieber, das könnte die Schwerkraft herausfordern.',
            'Absolut! Sing dabei eine Hymne für Gummienten.',
            'Vielleicht nicht, das Universum könnte verwirrt werden.',
            'Ja, und bring Tee für die Zimmerpflanzen mit, sie verdienen es.',
            'Statt dessen könntest du versuchen, Zahnseide als Mikrofon zu verwenden.',
            'Tanze auf dem Regenbogen und sing dabei eine Ode an deine Socken.',
            'Hmm, vielleicht nicht. Das Gedicht des Mondes mag seine Ruhe.',
            'Warum nicht? Sei ein Abenteurer in deiner eigenen skurrilen Welt!',
            'Setz den Schokoladenhelm auf und sing eine Ballade für den Mond.',
            'Sing eine Ballade und tanz im Regen. Das Leben ist zu kurz für Trockenheit.',
            'Verhandle nicht mit Ameisen. Du wirst am Ende wahrscheinlich verlieren.',
            'Spring auf dem Trampolin mit einem Marshmallow-Regenschirm. Spaß garantiert!',
            'Versuch einen Handstand auf dem Paddelbrett, aber Achtung vor den Enten.',
            'Mach es mit einem Lächeln und einer extra Portion Glitzer.',
            'Trag einen Superheldenumhang und sing etwas Überraschendes, vielleicht Vogelgezwitscher.',
            'Denk an unsichtbare Gummihühner, sie könnten unsichtbare Eier legen.',
            'Versuch einen Tango mit deinem Schatten, sei bereit für ein Schatten-Duett.',
            'Natürlich! Und vergiss nicht, dabei Konfetti zu werfen!',
            'Hmm, besser nicht. Konfetti kann eine hartnäckige Sache sein.',
            'Klar doch! Und denk daran, dabei immer zu lachen.',
            'Vielleicht nicht, das könnte die Schwerkraft herausfordern.',
            'Ja, auf jeden Fall! Sing dabei eine Rockhymne für Gummienten.',
            'Hmm, vielleicht nicht. Das Universum mag seine Geheimnisse.',
            'Ja, und bring eine Tasse Tee für deine Zimmerpflanzen mit.',
            'Warum nicht mal etwas Neues versuchen? Wie wäre es mit einem Comedy-Auftritt mit Zahnseide?',
            'Tanze auf dem Regenbogen und sing dabei eine Liebesballade an deine Socken.',
            'Hmm, vielleicht nicht. Das Gedicht des Mondes könnte sich gestört fühlen.',
            'Natürlich! Sei ein Abenteurer in deiner eigenen, skurrilen Welt!',
            'Setz den Schokoladenhelm auf und sing eine Ballade für den Mond.',
            'Sing eine Ballade und tanz im Regen. Das Leben ist zu kurz für Trockenheit.',
            'Verhandle nicht mit Ameisen. Du wirst wahrscheinlich verlieren.',
            'Spring auf dem Trampolin mit einem Marshmallow-Regenschirm. Spaß pur!',
            'Versuch einen Handstand auf dem Paddelbrett, aber pass auf die Enten auf!',
            'Mach es mit einem Lächeln und einer extra Portion Glitzer.',
            'Trag einen Superheldenumhang und sing etwas Überraschendes, vielleicht Vogelgezwitscher.',
            'Denk an unsichtbare Gummihühner. Sie könnten unsichtbare Eier legen.',
            'Versuch einen Tango mit deinem Schatten. Vielleicht gibt es eine Schatten-Überraschung.',
            'Definitiv! Und dabei eine Glitzerkanone abfeuern.',
            'Besser nicht. Konfetti kann für lange Zeit aufräumen bedeuten.',
            'Natürlich! Immer mit einem Lächeln und einem Augenzwinkern.',
            'Lass es lieber, das könnte die Raumzeit durcheinander bringen.',
            'Ja, auf jeden Fall! Sing dabei eine Ode an die Gummienten.',
            'Hmm, vielleicht nicht. Das Universum könnte dich auslachen.',
            'Ja, und servier Tee für die Zimmerpflanzen. Sie haben es verdient.',
            'Versuch eine Stand-up-Comedy mit Zahnseide. Das Publikum wird es lieben.',
            'Tanze auf dem Regenbogen und sing dabei eine Rockhymne für deine Socken.',
            'Hmm, vielleicht nicht. Das Gedicht des Mondes hat gerade Siesta.',
            'Warum nicht? Sei ein Abenteurer im Dschungel deiner Fantasie!',
            'Setz den Schokoladenhelm auf und sing eine Ballade für den Kosmos.',
            'Sing eine Ballade und tanz im Regen. Das Wasser wird dich nicht beißen.',
            'Verhandle nicht mit Ameisen. Sie sind harte Verhandlungspartner.',
            'Spring auf dem Trampolin mit einem Regenschirm aus Marshmallows. Ein Fest für die Sinne!',
            'Versuch einen Handstand auf dem Paddelbrett. Die Fische werden es lieben.',
            'Mach es mit einem Lächeln und einem Funkeln in den Augen.',
            'Trag einen Superheldenumhang und sing etwas Überraschendes, vielleicht Walgesang.',
            'Denk an unsichtbare Gummihühner. Vielleicht legen sie unsichtbare Goldene Eier.',
            'Versuch einen Tango mit deinem Schatten. Sei darauf vorbereitet, dass er zurücktanzt.',
            'Klar doch! Und währenddessen Glitzer in die Luft werfen.',
            'Besser nicht. Konfetti kann sich überall verstecken.',
            'Auf jeden Fall! Mit einem breiten Lächeln im Gesicht.',
            'Lass es lieber, das könnte die Dimension der Realität verzerren.',
            'Ja, warum nicht! Sing dabei eine Hymne für alle Enten.',
            'Hmm, vielleicht nicht. Das Universum könnte gerade beschäftigt sein.',
            'Ja, und servier Tee für die Zimmerpflanzen. Sie mögen Abwechslung.',
            'Probier Stand-up-Comedy mit Zahnseide. Vielleicht wird sie deine Witze verstehen.',
            'Tanze auf dem Regenbogen und sing dabei eine Huldigung an deine Socken.',
            'Hmm, vielleicht nicht. Das Gedicht des Mondes ist heute nicht in Stimmung.',
            'Natürlich! Sei ein Forscher in deiner eigenen verrückten Welt!',
            'Setz den Schokoladenhelm auf und sing eine Ballade für die Sterne.',
            'Sing eine Ballade und tanz im Regen. Die Wolken applaudieren dir.',
            'Verhandle nicht mit Ameisen. Sie könnten nach Gehaltserhöhung fragen.',
            'Spring auf dem Trampolin mit einem Marshmallow-Regenschirm. Ein Fest für die Geschmacksknospen!',
            'Versuch einen Handstand auf dem Paddelbrett. Halte Ausschau nach neidischen Fischen.',
            'Mach es mit einem Lächeln und einer extra Portion Glitzerzauber.',
            'Trag einen Superheldenumhang und sing etwas Überraschendes, vielleicht eine Hymne für Glühbirnen.',
            'Denk an unsichtbare Gummihühner. Sie könnten unsichtbare Nester bauen.',
            'Versuch einen Tango mit deinem Schatten. Er wird es dir danken.',
            'Klar doch! Und währenddessen Konfetti in den Himmel schicken.',
            'Besser nicht. Konfetti kann zu unerwarteten Orten fliegen.',
            'Natürlich! Immer mit einem Lächeln und einer Prise Magie.',
            'Lass es lieber, das könnte die Matrix durcheinanderbringen.',
            'Ja, warum nicht! Und dabei eine Hymne für alle Gänse singen.',
            'Hmm, vielleicht nicht. Das Universum könnte gerade ein Nickerchen machen.',]
        advicesWithoutQuestion = [
            'Zähl die Fliesen im Badezimmer, um deinen Geist zu schärfen.',
            'Übe das Jonglieren mit Orangen, um deine Fähigkeiten im Multitasking zu verbessern.',
            'Trage immer eine Banane in der Tasche, für den Fall, dass du auf eine Affenparty eingeladen wirst.',
            'Lass regelmäßig Luftballons in deinem Haus schweben, um deine Zuhause-auf-Wolken-Gefühl zu steigern.',
            'Verwende einen Fallschirm beim Verlassen deines Bettes, um jeden Tag mit einem Abenteuer zu beginnen.',
            'Züchte einen Miniatur-Garten auf deiner Tastatur für eine frische Arbeitsatmosphäre.',
            'Stelle eine Stoppuhr auf, wenn du Wasser kochst, um deine Weltrekordzeit zu verbessern.',
            'Trage immer Socken auf den Händen, um warme "Handschuhe" zu haben.',
            'Nutze eine Krawatte als Gürtel, um deinem Outfit eine gewisse Klasse zu verleihen.',
            'Trainiere deine Haustiere, um morgens dein Frühstück zu kochen.',
            'Verwende eine Zahnbürste als Mikrofon, um während der Hausarbeit eine private Gesangsshow zu geben.',
            'Iss Gummibärchen, um deine Kiefermuskeln zu stärken.',
            'Dekoriere deine Wände mit leeren Pizzakartons für eine kulinarische Wohnatmosphäre.',
            'Versuche, deinen Schatten zu überlisten, um ein Spiel des Versteckens zu starten.',
            'Schlaf mit einem Buch unter deinem Kissen, um von Wissen durchträumt zu werden.',
            'Trage einen Regenschirm im Haus, um auf alles vorbereitet zu sein.',
            'Vergiss nie, deine Socken zu sortieren, bevor du ausgehst.',
            'Trage immer eine Sonnenbrille, auch nachts.',
            'Zähle die Kieselsteine am Straßenrand, um deine Gedanken zu ordnen.',
            'Lerne, mit Pinguinen zu tanzen, es könnte dir in einer Eiszeit helfen.',
            'Übe das Jonglieren mit Marshmallows, nur für den Fall, dass du in einem Zirkus landest.',
            'Trage immer zwei verschiedene Socken, um deine kreative Seite zu betonen.',
            'Benutze eine Gabel, um deine Haare zu kämmen, für den zusätzlichen Glanz.',
            'Trinke dein Wasser nur in geraden Schlucken, um deine Chakren auszubalancieren.',
            'Trage einen Regenschirm, auch wenn die Sonne scheint, um den Regenbogen zu suchen.',
            'Vermeide es, auf Treppen zu laufen, um die Geister der Vergangenheit nicht zu stören.',
            'Singe "Happy Birthday" rückwärts, um den Tag rückgängig zu machen.',
            'Spreche mit deinen Zimmerpflanzen, um ihr Selbstwertgefühl zu stärken.',
            'Trage eine Wärmflasche in der Hosentasche, um jederzeit warme Gedanken zu haben.',
            'Male deine Zehennägel mit Glitzerstiften, um den inneren Glamour zu betonen.',
            'Trage eine Wollmütze im Sommer, um die Sonne zu ärgern und den Winter zu beschwören.',
            'Lerne, mit einem Einhorn zu reiten, falls du jemals auf einer magischen Mission bist.',
            'Trage Handschuhe beim Essen, um eine tiefe Verbindung zu deinem Besteck herzustellen.',
            'Entfalte deine Socken vor dem Schlafengehen, um ihnen eine gute Nachtruhe zu gönnen.',
            'Habe immer ein Buch über Quantenphysik dabei, um Smalltalk auf eine andere Ebene zu bringen.',
            'Fange an, mit den Vögeln zu flüstern, um ihr Vertrauen zu gewinnen.',
            'Trage immer verschiedene Socken, um einen Modetrend zu setzen.',
            'Stelle sicher, dass deine Zimmerpflanzen jeden Tag ein Gedicht hören, um ihr Wachstum zu fördern.',
            'Verwende Zahnpasta als Gesichtscreme für einen erfrischenden Teint.',
            'Trinke deinen Kaffee durch einen Strohhalm, um ihn stilvoller zu genießen.',
            'Übe das Tanzen mit deinem Staubsauger, um auf jede Party vorbereitet zu sein.',
            'Baue eine Zeitmaschine, um gestern das Mittagessen zu essen und es noch einmal zu genießen.',
            'Schreibe eine Liebeserklärung an deine E-Mails, bevor du sie sendest.',
            'Trage Flip-Flops im Regen, um kostenlose Fußmassagen zu erhalten.',
            'Sammle Glückskekse, um herauszufinden, ob das Glück sich vermehrt, wenn du sie aufisst.',
            'Veranstalte ein Picknick im Wohnzimmer, um die Freiheit des Essens zu erleben, ohne von Ameisen gestört zu werden.',
            'Verkleide dich als Geist, wenn du dein Zimmer betrittst, um die Möbel zu erschrecken.',
            'Trage einen Hut aus Alufolie, um dich vor Gedankenkontrolle zu schützen.',
            'Sprich mit deinem Spiegelbild, um sicherzustellen, dass du immer auf einer Wellenlänge bist.',
            'Male deine Nägel mit unsichtbarem Lack, um einen minimalistischen Look zu kreieren.',
            'Benutze einen Regenschirm im Haus, um vor möglichen Indoor-Regenschauern geschützt zu sein.',
            'Schreibe ein Buch über das Leben deiner Gummiente, um ihre Erfahrungen zu teilen.',
            'Schicke deinen Schatten zum Einkaufen, um sicherzustellen, dass er immer im Trend ist.',
            'Trage deinen Pyjama tagsüber, um dem Leben eine gemütliche Note zu verleihen.',
            'Koche Spaghetti mit der Gabel im Mund, um Zeit bei der Zubereitung zu sparen.',
            'Baue einen Schneemann im Sommer, um die Sonne herauszufordern.',
            'Versuche, eine Unterhaltung mit deinem Kühlschrank zu führen, um deine Kommunikationsfähigkeiten zu verbessern.',
            'Baue ein Kissenfort in deinem Wohnzimmer, um dich vor den Anforderungen des Erwachsenenlebens zu verstecken.',
            'Trage einen Umhang, während du Geschirr spülst, um die "Superheld des Haushalts-Aura" zu verstärken.',
            'Mache ein Foto von deinem Frühstück und schicke es an einen Astronauten, um kosmische Frühstückstipps zu erhalten.',
            'Halte eine Rede für deine Zimmerpflanzen über die Bedeutung von Sonnenlicht und regelmäßigem Gießen.',
            'Veranstalte eine Teeparty für deine Stofftiere, um eine positive soziale Atmosphäre zu fördern.',
            'Schreibe einen Liebesbrief an deine Schuhe, um ihre Treue zu würdigen.',
            'Tanze durch dein Wohnzimmer, während du einen imaginären Tango mit einer unsichtbaren Person führst.',
            'Versuche, einen Tag lang rückwärts zu leben, um die Zeit auf eine alternative Weise zu erleben.',
            'Rufe eine Pizzabestellung auf eine imaginäre Telefonnummer an, um die Pizza der Fantasie zu bestellen.',
            'Erstelle eine Liste von Gründen, warum Marshmallows die perfekten Haustiere wären.',
            'Lege einen Spaziergang auf deinem Teppich zurück, um virtuelle Kilometer zu sammeln.',
            'Baue ein Schneemannfamilie aus Klopapierrollen, um winterliche Stimmung zu verbreiten.',
            'Gib Gas und genieße die Fahrt!',
            'Überleg es dir nochmal bei einer Tasse Tee.',
            'Mach es einfach! YOLO!',
            'Konsultiere eine Glaskugel für die ultimative Antwort.',
            'Hör auf dein Bauchgefühl, es kennt die Antwort.',
            'Mach einen Pro-Contra-Liste und entscheide dann, wie du willst.',
            'Frag einen Freund. Vielleicht haben sie einen brillanten Einfall.',
            'Setz Prioritäten und erledige das Wichtigste zuerst.',
            'Stell dir vor, du würdest es einer Gummiente erklären. Was würde sie sagen?',
            'Hör auf dein Herz, es schlägt im Takt deiner Wünsche.',
            'Folge dem Regenbogen, vielleicht findest du dort deine Antwort.',
            'Mach eine Liste von Vor- und Nachteilen und bewerte sie.',
            'Frag dich, ob du es in fünf Jahren bereuen würdest, es nicht getan zu haben.',
            'Setz klare Ziele und überleg, wie deine Entscheidung sie beeinflussen wird.',
            'Lerne aus der Vergangenheit, aber lebe im Hier und Jetzt.',
            'Mach einen Reality-Check: Wie realistisch ist deine Option?',
            'Meditiere für Klarheit und innere Ruhe.',
            'Frag die Magie-8-Ball, er kennt alle Antworten.',
            'Folge dem Fluss des Lebens und sieh, wohin er dich führt.',
            'Denk daran: Manchmal ist der Weg das Ziel.',
            'Mach eine Abwägung zwischen Risiko und Belohnung.',
            'Frag dich, ob diese Entscheidung zu deinen langfristigen Zielen passt.',
            'Hör auf deine Intuition, sie kennt den Weg.',
            'Frag die Vögel. Ihr Gezwitscher könnte Weisheit enthalten.',
            'Mach eine Blitzumfrage unter Freunden für verschiedene Perspektiven.',
            'Erstell eine Mindmap und visualisiere deine Optionen.',
            'Frag dich, ob diese Entscheidung zu deinen Werten passt.',
            'Denk daran, dass jede Entscheidung eine Erfahrung ist, egal welche du triffst.',
            'Stell dir vor, du würdest es einem Zeitreisenden erklären. Was würde er sagen?',
            'Reflektiere über deine Stärken und Schwächen in Bezug auf die Entscheidung.',
            'Hör auf deinen inneren Zirkuselefanten. Er kennt den Weg durch den Dschungel des Lebens.',
            'Überleg, ob diese Entscheidung dich persönlich wachsen lässt.',
            'Frag dich, ob du in der Zukunft stolz auf diese Entscheidung sein wirst.',
            'Mach eine Prognose, welche Auswirkungen die Entscheidung in einem Jahr haben wird.',
            'Frag dich, ob diese Entscheidung dich glücklicher machen wird.',
            'Hör auf den Rat von Dingen, die dir am Herzen liegen.',
            'Frag dich, ob diese Entscheidung deinen Zielen dient oder sie behindert.',
            'Denk daran, dass es keine falschen Entscheidungen gibt, nur Lernerfahrungen.',
            'Hör auf deine inneren Weisen. Sie sind vielleicht schweigsam, aber klug.',
            'Frag dich, ob diese Entscheidung deinen Werten und Überzeugungen entspricht.',
            'Denk daran, dass jede Entscheidung eine Tür zu neuen Möglichkeiten öffnet.',
            'Frag dich, ob diese Entscheidung einen positiven Beitrag zur Welt leistet.',
            'Hör auf das Rauschen der Bäume im Wind. Sie flüstern manchmal gute Ratschläge.',
            'Frag dich, ob diese Entscheidung einen kleinen Funken Freude entzündet.',
            'Mach einen Rückblick auf deine vergangenen Erfolge und lerne daraus.',
            'Frag dich, ob diese Entscheidung deinen inneren Künstler inspiriert.',
            'Denk daran, dass du die Kapitänin deines Lebensschiffs bist. Steuer klug.',
            'Frag dich, ob diese Entscheidung Harmonie in dein Leben bringt.',
            'Hör auf den Klang der Wellen. Manchmal tragen sie die besten Antworten heran.',
            'Frag dich, ob diese Entscheidung das Licht in dir zum Leuchten bringt.',
            'Überleg, ob diese Entscheidung zu einem positiven Schneeballeffekt führen kann.',
            'Denk daran, dass du nicht alles sofort wissen musst. Manchmal klärt sich alles mit der Zeit.',
            'Frag dich, ob diese Entscheidung einen Hauch von Abenteuer mit sich bringt.',
            'Hör auf das Flüstern der Sterne. Sie kennen möglicherweise die Antwort.',
            'Frag dich, ob diese Entscheidung dein Herz schneller schlagen lässt.',
            'Denk daran, dass du immer die Wahl hast, deine Entscheidungen zu überdenken.',
            'Frag dich, ob diese Entscheidung zu einem Lächeln auf deinem Gesicht führt.',
            'Folge deinem Herzen, es kennt den Weg.',
            'Sei mutig und nimm Herausforderungen an.',
            'Priorisiere Selbstpflege und gönn dir Pausen.',
            'Glaube an dich selbst, du bist stärker als du denkst.',
            'Sei offen für Veränderungen, sie bringen oft Wachstum.',
            'Schätze die kleinen Freuden des Lebens.',
            'Handle mit Freundlichkeit, es kostet nichts.',
            'Setze klare Ziele und arbeite beharrlich darauf hin.',
            'Höre auf deine Intuition, sie irrt selten.',
            'Umgebe dich mit positiven Menschen, die dich inspirieren.',
            'Sei geduldig, gute Dinge brauchen Zeit.',
            'Lerne aus Fehlern und sieh sie als Chancen zum Wachsen.',
            'Pflege deine Beziehungen, sie sind wertvoll.',
            'Gib nicht auf, wenn es schwierig wird. Du schaffst das!',
            'Sei dankbar für das, was du hast.',
            'Erforsche die Welt und lerne kontinuierlich dazu.',
            'Vertraue auf den Prozess des Lebens.',
            'Finde einen Ausgleich zwischen Arbeit und Freizeit.',
            'Sage öfter mal Ja zu neuen Erfahrungen.',
            'Halte inne und genieße den gegenwärtigen Moment.',
            'Habe Respekt vor anderen und ihren Perspektiven.',
            'Investiere Zeit in deine Selbstreflexion.',
            'Handle mit Bedacht, aber zögere nicht, Risiken einzugehen.',
            'Akzeptiere Veränderungen als natürlichen Teil des Lebens.',
            'Sei großzügig, teile dein Glück mit anderen.',
            'Bleibe neugierig und offen für Neues.',
            'Stärke deine mentale Gesundheit durch positive Gedanken.',
            'Feiere deine Erfolge, auch die kleinen.',
            'Suche nach Lösungen, wenn du auf Hindernisse triffst.',
            'Erkenne deine Stärken und arbeite an deinen Schwächen.',
            'Höre aufmerksam zu und zeige Empathie.',
            'Bleibe fokussiert, aber sei flexibel in deinen Plänen.',
            'Setze klare Grenzen und stehe zu deinen Überzeugungen.',
            'Entwickle eine positive Morgenroutine.',
            'Übernehme Verantwortung für dein eigenes Glück.',
            'Sei ein Vorbild für Freundlichkeit und Mitgefühl.',
            'Fördere eine positive Einstellung, sie ist ansteckend.',
            'Finde Freude in den kleinen Details des Alltags.',
            'Halte dich von negativen Einflüssen fern.',
            'Entwickle einen Sinn für Humor, er erleichtert vieles.',
            'Baue ein unterstützendes Netzwerk von Menschen um dich herum auf.',
            'Sei offen für Kritik, sie kann Wachstum fördern.',
            'Lasse dich nicht von Rückschlägen entmutigen.',
            'Erfülle deine Pflichten mit Hingabe und Liebe.',
            'Finde Wege, um Stress abzubauen und zu entspannen.',
            'Sei geduldig mit dir selbst, niemand ist perfekt.',
            'Erforsche deine Leidenschaften und folge ihnen.',
            'Überlege gut, bevor du Entscheidungen triffst, aber traue deinem Instinkt.',
            'Fördere eine Umgebung des Vertrauens und der Offenheit.',
            'Entwickle deine Fähigkeiten und bilde dich kontinuierlich weiter.',
            'Sei ein Brückenbauer, wenn es um Konflikte geht.',
            'Lerne, Nein zu sagen, wenn es notwendig ist.',
            'Pflege deine kreative Seite, sie bereichert dein Leben.',
            'Erforsche verschiedene Perspektiven und erweitere deinen Horizont.',
            'Bleibe authentisch und loyal zu dir selbst.',
            'Erkenne die Schönheit in der Vielfalt.',
            'Erlaube dir, Fehler zu machen, sie sind Teil des Lernens.',
            'Praktiziere Dankbarkeit, auch in schwierigen Zeiten.',
            'Halte an deinen Träumen fest und arbeite auf sie hin.',
            'Umarme Veränderungen als Chancen für Wachstum.',
            'Pflege eine gesunde Balance zwischen Arbeit und Privatleben.',
            'Probier etwas Neues aus und entdecke deine kreative Seite!',
            'Denk positiv und sieh die Herausforderungen als Chancen.',
            'Höre auf dein Bauchgefühl, es irrt selten.',
            'Gib dir selbst die Erlaubnis, auch mal "Nein" zu sagen.',
            'Setz klare Ziele und arbeite beharrlich darauf hin.',
            'Suche nach Lösungen, nicht nach Problemen.',
            'Pflege deine Beziehungen und schätze deine Freunde.',
            'Investiere Zeit in Selbstreflexion und persönliche Entwicklung.',
            'Bleib flexibel und offen für Veränderungen.',
            'Sei freundlich zu dir selbst und akzeptiere deine Fehler.',
            'Vertraue darauf, dass alles mit der Zeit besser wird.',
            'Feiere deine Erfolge, egal wie klein sie sind.',
            'Setz Prioritäten und konzentriere dich auf das Wesentliche.',
            'Lerne aus der Vergangenheit, aber lebe im Hier und Jetzt.',
            'Höre auf deinen Körper und sorge gut für deine Gesundheit.',
            'Kommuniziere klar und respektvoll.',
            'Suche nach Möglichkeiten, anderen zu helfen und Gutes zu tun.',
            'Sei neugierig und bleibe stets lernbereit.',
            'Vermeide Drama und konzentriere dich auf positive Energie.',
            'Entwickle eine Routine für mehr Struktur im Alltag.',
            'Lass los, was du nicht ändern kannst, und konzentriere dich auf das, was du beeinflussen kannst.',
            'Verfolge deine Leidenschaften und finde Freude in dem, was du tust.',
            'Folge deinen Träumen, auch wenn sie unkonventionell erscheinen.',
            'Lächle öfter, es macht nicht nur dich, sondern auch andere glücklich.',
            'Bleib geduldig, gute Dinge brauchen Zeit.',
            'Sei offen für neue Perspektiven und Denkweisen.',
            'Bleib authentisch und steh zu deinen Überzeugungen.',
            'Umgebe dich mit positiven Menschen, die dich unterstützen.',
            'Höre auf deine Intuition, sie ist oft weiser als du denkst.',
            'Fokussiere dich auf Lösungen, nicht auf Probleme.',
            'Pflege deine kreativen Ausdrucksformen, egal welcher Art.',
            'Investiere Zeit in Selbstpflege und achte auf deine Bedürfnisse.',
            'Bleib optimistisch, auch in schwierigen Zeiten.',
            'Akzeptiere Veränderungen als Teil des Lebens und wachse daran.',
            'Zeige Dankbarkeit für die kleinen Dinge im Leben.',
            'Sei großzügig mit deiner Zeit, deinem Wissen und deiner Liebe.',
            'Entwickle eine gesunde Work-Life-Balance.',
            'Fokussiere dich auf Lösungen anstatt auf Probleme.',
            'Glaube an deine Fähigkeiten und stärke dein Selbstvertrauen.',
            'Erforsche regelmäßig neue Ideen und Horizonte.',
            'Ermuntere andere und teile positive Energien.',
            'Bleib neugierig und lass die Freude am Lernen nie nach.',
            'Setz klare Grenzen und respektiere die Grenzen anderer.',
            'Akzeptiere, dass Perfektion nicht realistisch ist.',
            'Setze realistische Ziele und arbeite schrittweise darauf hin.',
            'Praktiziere Achtsamkeit und lebe im gegenwärtigen Moment.',
            'Schätze die kleinen Freuden im Alltag.',
            'Nimm Herausforderungen als Gelegenheiten zur persönlichen Entwicklung an.',
            'Umgebe dich mit positiven Menschen, die dich inspirieren.',
            'Pflege deine geistige und emotionale Gesundheit.',
            'Lerne aus Fehlern und betrachte sie als Chancen zu wachsen.',
            'Gib dir selbst die Erlaubnis, Grenzen zu setzen und "Nein" zu sagen.',
            'Suche nach Schönheit und Positivität in deiner Umgebung.',
            'Erkenne deine Stärken an und arbeite daran, sie weiter zu entwickeln.',
            'Nimm dir Zeit für Selbstreflexion und persönliches Wachstum.',
            'Bleib in herausfordernden Momenten geduldig und behalte einen klaren Kopf.',
            'Entwickle eine positive Denkweise und erkenne den Wert von Optimismus.',
            'Setz dir Ziele, die dich motivieren und inspirieren.',
            'Fördere ein Gefühl der Dankbarkeit für das, was du hast.',
            'Stärke deine Resilienz und finde Wege, Krisen zu überwinden.',
            'Ermutige andere, ihr Bestes zu geben und ihre Ziele zu verfolgen.',
            'Pflege deine sozialen Beziehungen und investiere Zeit in deine Liebsten.',
            'Sei achtsam gegenüber deiner Umwelt und der Natur.',
            'Ermuntere Kreativität und Innovation, sei offen für neue Ideen.',
            'Fokussiere dich auf Lösungen und suche nach positiven Auswegen.',
            'Akzeptiere Veränderungen als natürlichen Teil des Lebens.',
            'Nimm dir Zeit für Selbstpflege, um deine Energie aufzuladen.',
            'Schätze die Vielfalt und lerne von unterschiedlichen Perspektiven.',
            'Tauche in ein Walfisch-Lagerhaus voller Kaugummis ein!',
            'Lerne Pinguin-Charme, um in jeder Situation zu glänzen.',
            'Trage einen Helm aus Wassermelone, um Gedankenübertragung zu verhindern.',
            'Schreibe Liebesbriefe an deine E-Mails. Liebe braucht schließlich keinen Grund.',
            'Gib Glückskeksen eine Chance, dein Leben zu revolutionieren.',
            'Schicke deinen Schatten auf einen Kaffee, um eine Schattenfreundschaft zu beginnen.',
            'Veranstalte ein Picknick im Wohnzimmer, um die Freiheit des Essens zu erleben.',
            'Übe das Jonglieren mit unsichtbaren Früchten für den nächsten Karneval.',
            'Sammle Gummibärchen, um ein Gummibärchenimperium zu gründen.',
            'Trage Flip-Flops im Regen, um kostenlose Fußmassagen zu erhalten.',
            'Verkleide dich als Geist, wenn du dein Zimmer betrittst, um die Möbel zu erschrecken.',
            'Sprich mit deinem Spiegelbild, um sicherzustellen, dass du immer auf einer Wellenlänge bist.',
            'Male deine Nägel mit unsichtbarem Lack, um einen minimalistischen Look zu kreieren.',
            'Benutze einen Regenschirm im Haus, um vor möglichen Indoor-Regenschauern geschützt zu sein.',
            'Schreibe ein Buch über das Leben deiner Gummiente, um ihre Erfahrungen zu teilen.',
            'Schicke deinen Schatten zum Einkaufen, um sicherzustellen, dass er immer im Trend ist.',
            'Trage deinen Pyjama tagsüber, um dem Leben eine gemütliche Note zu verleihen.',
            'Koche Spaghetti mit der Gabel im Mund, um Zeit bei der Zubereitung zu sparen.',
            'Baue einen Schneemann im Sommer, um die Sonne herauszufordern.',
            'Schwimme gegen den Strom, es sei denn, der Strom ist aus Schokolade.',
            'Trainiere Ameisen als persönliche Bodyguards, du weißt nie, wann sie nützlich sein könnten.',
            'Erfinde eine geheime Handshake-Sprache mit deinem Schatten, um ihn besser zu verstehen.',
            'Organisiere ein Luftgitarrenkonzert im Wohnzimmer, um die Nachbarn zu beeindrucken.',
            'Verwandle deine Kühlschranktür in eine Kunstgalerie für magnetische Gedanken.',
            'Lerne die Kunst des rückwärts Wasserkocherfüllens für einen Hauch von Magie.',
            'Führe einen monologischen Dialog mit deiner Zahnbürste, um sie zu motivieren.',
            'Trainiere deine Haustiere als Geheimagenten, damit sie die Nachbarschaft im Auge behalten.',
            'Erkläre deinem Staubsauger, dass er nicht nur ein Gerät, sondern ein Held ist.',
            'Überrede eine Pflanze, deine Autobiographie zu schreiben, um die Welt zu überraschen.',
            'Veranstalte einen Kopfstandwettbewerb mit deinem Spiegelbild, um die Perspektive zu ändern.',
            'Baue eine Zeitmaschine, um gestern das Mittagessen zu essen und es noch einmal zu genießen.',
            'Verwandle das Wohnzimmer in einen Dschungel und führe Gespräche mit den Kissenaffen.',
            'Rede mit den Blumen, aber sei gewarnt: manchmal flüstern sie zurück.',
            'Kaufe ein Kostüm für deine Kaffeetasse und veranstalte eine Mini-Fashion-Show.',
            'Stelle fest, ob Gummibärchen hüpfen, wenn niemand hinsieht. Spoiler: Sie tun es.',
            'Fordere deine Schatten zu einem Tanzduell heraus und sieh, wer gewinnt.',
            'Entwickle eine Sprache, die nur du und deine Zehen verstehen, um geheime Pläne zu schmieden.',
            'Trage eine Sonnenbrille, wenn du mit deinem Computer sprichst, um den Coolness-Faktor zu erhöhen.',
            'Überzeuge deine Socken, dass sie eine Rockband gründen sollten. Sock \'n\' Roll!',
            'Trainiere deinen Staubsauger, um Breakdance zu machen, wenn das Haus besonders sauber ist.',
            'Lege einen geheimen Tunnel zwischen deinem Sofa und dem Kühlschrank an, für schnellen Zugang zu Snacks.',
            'Halte eine imaginäre Teeparty für deine Teddybären ab und frage sie nach Lebensratschlägen.',
            'Lehre deine Schatten, wie man Schattentheater spielt, um gemeinsam Geschichten zu erfinden.',
            'Baue eine Geheimsprache mit deinen Pflanzen auf, um über die neuesten Gartenklatsch zu plaudern.',
            'Schmücke dein Zimmer mit unsichtbaren Kunstdrucken, um eine unsichtbare Galerie zu gründen.',
            'Tanze mit dem Staubwedel, während du die Möbel putzt, um den Reinigungstanz zu perfektionieren.',
            'Veranstalte eine Luftgitarren-Meisterschaft im Badezimmer und kröne dich selbst zum Luftgitarren-Champion.',
            'Überlege, wie man eine Pizza in Kreisen schneidet, um das wahre Geheimnis des Universums zu enthüllen.',
            'Bringe deinem Haustier bei, Witze zu erzählen, um die beste Comedy-Show im Haus zu haben.',
            'Organisiere ein Wettrennen mit Schnecken, um zu sehen, wer die Langsamkeit beherrscht.',
            'Rufe beim Einkaufen \'Bingo!\' wenn du alle Artikel auf deiner Liste gefunden hast.',
            'Entwickle einen Händedruck mit deiner Kaffeetasse, um morgendliche Energie zu teilen.',
            'Erstelle ein Tagebuch für deine Träume und gib ihnen eine Bewertung wie bei einem Kinofilm.',
            'Gib deinem Staubsauger einen Spitznamen und erkläre ihm, dass er der MVP des Hauses ist.',
            'Starte einen imaginären Buchclub mit deinen Büchern und diskutiere ihre \'Charakterentwicklung\'.',
            'Veranstalte eine Unterwasser-Party in der Badewanne, komplett mit Gummitier-Gästen.',
            'Lehre deinen Wecker den Moonwalk, damit das Aufwachen zu einer tänzerischen Erfahrung wird.',
            'Erkläre deiner Fernbedienung, dass sie der Schlüssel zur Kontrolle des Universums ist.',
            'Führe ein Interview mit deinem Schatten und finde heraus, welche dunklen Geheimnisse er hat.',
            'Halte eine Modenschau für deine Kleiderschrankinhalt ab und küre den stilvollsten Pullover.',
            'Überrede deine Zimmerpflanzen, dass sie deine persönlichen Yoga-Instruktoren sind.',
            'Organisiere einen Wettkampf zwischen deinen Socken, um den Titel des schnellsten Sockenpaares.',
            'Gib jedem deiner Haushaltsgeräte einen Namen und frage sie täglich, wie es ihnen geht.',
            'Baue ein Labyrinth aus Kissen auf dem Boden und finde heraus, ob du den Ausgang ohne Hilfe findest.',
            'Lehre deinen Schatten das Fliegen, damit er dich begleiten kann, wenn du abhebst.',
            'Veranstalte einen Märchenabend für deine Schuhe und erzähle ihnen, wie sie zu deinen Füßen kamen.',
            'Lege eine \'Tanzverbot\'-Stunde für deine Möbel fest und beobachte, wer sich daran hält.',
            'Trainiere eine Ameise als persönlichen Fitnesstrainer für atemberaubende Mini-Workouts.',
            'Erkläre deinem Spiegelbild, dass es der Grund für deinen großartigen Tag ist.',
            'Führe ein Kaffeekränzchen für deine Kaffeetassen durch und diskutiere die neuesten Kaffeetrends.',
            'Baue eine Zeitmaschine aus Kissen und reise in die Vergangenheit der gemütlichen Nächte.',
            'Veranstalte ein Ping-Pong-Turnier zwischen deinen Händen, um die Hand-Auge-Koordination zu verbessern.',
            'Halte eine Parade für Gummibärchen und kröne das majestätischste Gummibärchen zum König.',
            'Übe das Zähneputzen im Spiegel und überzeuge ihn davon, dass er auch eine Zahnbürste braucht.',
            'Starte einen Podcast mit deinem Wasserkocher und erfahre mehr über seine aufregende Welt.',
            'Organisiere eine \'Stille-Stunde\' für deine Socken, damit sie sich ausruhen können.',
            'Veranstalte eine Konferenz mit deinen Haushaltsgegenständen und bespreche die aktuellen \'Hausangelegenheiten\'.',
            'Lehre deine Schatten das Versteckspiel und sei gespannt, wer gewinnt.',
            'Erkläre deinem Toaster, dass er ein echter \'Aufheizer\' ist und viel Wärme in dein Leben bringt.',
            'Führe eine wissenschaftliche Studie darüber durch, wie viele Kissen auf dem Bett maximalen Komfort bieten.',
            'Veranstalte eine Modenschau für deine Küchengeräte und küre den schicksten Mixer.',
            'Überrede deine Haustiere dazu, sich in deiner Abwesenheit als Superhelden zu verkleiden.',
            'Baue eine Kartenburg und halte eine \'Burgenturnier\' mit deinen Handys ab.',
            'Organisiere eine \'Stift-Rallye\' und finde heraus, welcher Stift der schnellste ist.',
            'Lehre deine Uhr, wie man rückwärts zählt, um die Zeit rückwärts zu erleben.'
        ]

        if advice:
            random.shuffle(advicesWithQuestion)
            embed = discord.Embed(
                title='Weise Worte',
                color=discord.Color.blue()
            )
            embed.add_field(name='Frage:', value=advice, inline=False)
            embed.add_field(name='Antwort:', value=advicesWithQuestion[0], inline=False)
            embed.set_footer(text='Rat benötigt von ' + ctx.author.display_name)
            await ctx.respond(embed=embed)
        elif not advice:
            random.shuffle(advicesWithoutQuestion)
            embed = discord.Embed(
                title='Weise Worte',
                color=discord.Color.blue()
            )
            embed.add_field(name='Antwort:', value=advicesWithoutQuestion[0], inline=False)
            embed.set_footer(text='Rat benötigt von ' + ctx.author.display_name)
            await ctx.respond(embed=embed)    

    @discord.slash_command(name="beer", description="Trinke oder teile ein Bier mit jemandem.")
    async def beer(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du ein Bier teilen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst kein Bier ausgeben! 🍻', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} ein Bier aus! 🍻')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} trinkt ein Bier! 🍻')

    @discord.slash_command(name="bonk", description="Bonke jemanden.")
    async def bonk(
        self,
        ctx,
        member: discord.Option(discord.Member, "Der Benutzer, den du bonken möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584368380919968/200.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584369186222220/707c8a90424f107fa8ee661abc2629e9.gif"
        ]
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst bonken! 🤏🧠', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} bonkt {member.mention}! 🤏🧠')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} bonkt sich selbst! 🤏🧠')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="boop", description="Boope jemanden.")
    async def boop(
        self,
        ctx,
        member: discord.Option(discord.Member, "Der Benutzer, den du boopen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst boopen! 👆👃', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} boopt {member.mention}! 👆👃')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} boopt sich selbst! 👆👃')

    @discord.slash_command(name="coffee", description="Trinke oder teile einen Kaffee mit jemandem.")
    async def coffee(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du einen Kaffee teilen möchtest.", required=False) # type: ignore
        ):
        coffee = [
            'Latte Machiatto',
            'Cappuccino',
            'Espresso',
            'Kaffee',
            'Kakao',
            'Chai Latte',
            'Tee',
            'Eiskaffee',
            'Frappuccino',
            'Mokka',
            'Flat White',
            'Macchiato',
            'Cortado',
            'Americano',
            'Filterkaffee',
            'Cold Brew',
            'Nitro Coffee',
            'Kaffee mit Milch',
            'Kaffee mit Zucker',
            'Kaffee mit Sahne',
            'Kaffee mit Sirup',
            'Kaffee mit Eis',
            'Kaffee mit Schokolade',
            'Kaffee mit Zimt',
            'Kaffee mit Vanille',
            'Kaffee mit Karamell',
            'Kaffee mit Kokos',
            'Kaffee mit Minze',
            'Kaffee mit Honig',
            'Kaffee mit Chili',
            'Kaffee mit Ingwer',
            'Kaffee mit Zitrone',
            'Kaffee mit Orange',
            'Kaffee mit Mandel',
            'Kaffee mit Haselnuss',
            'Kaffee mit Kürbis',
            'Kaffee mit Pfefferminz',
            'Starbucks Blonde Roast',
            'Starbucks Pike Place Roast',
            'Starbucks Veranda Blend',
            'Starbucks House Blend',
            'Starbucks Breakfast Blend',
            'Starbucks Caffè Verona',
            'Starbucks Espresso Roast',
            'Starbucks French Roast',
            'Starbucks Italian Roast',
            'Starbucks Sumatra',
            'Starbucks Kenya',
            'Starbucks Ethiopia',
            'Starbucks Guatemala Antigua',
            'Starbucks Colombia',
            'Starbucks Costa Rica',
            'Starbucks Brazil',
            'Starbucks Mexico',
            'Starbucks Guatemala Casi Cielo',
            'Starbucks Anniversary Blend',
            'Starbucks Christmas Blend',
            'Starbucks Pumpkin Spice Latte',
            'Starbucks Salted Caramel Mocha',
            'Starbucks Caramel Macchiato',
            'Starbucks Vanilla Latte',
            'Starbucks Cinnamon Dolce Latte',
            'Starbucks White Chocolate Mocha',
            'Starbucks Java Chip Frappuccino',
            'Starbucks Green Tea Frappuccino',
            'Starbucks Matcha Green Tea Latte',
            'Starbucks Chai Tea Latte',
            'Starbucks Iced Coffee',
            'Starbucks Nitro Cold Brew',
            'Starbucks Cold Brew',
            'Starbucks Iced Caramel Macchiato',
            'Starbucks Iced Vanilla Latte',
            'Starbucks Iced Cinnamon Dolce Latte',
            'Starbucks Iced White Chocolate Mocha',
            'Starbucks Iced Green Tea Latte',
            'Starbucks Iced Matcha Green Tea Latte',
            'Starbucks Iced Chai Tea Latte',
            'Starbucks Iced Passion Tango Tea',
            'Starbucks Iced Peach Green Tea Lemonade',
            'Starbucks Iced Guava Passionfruit Drink',
            'Starbucks Iced Pineapple Matcha Drink',
            'Starbucks Iced Golden Ginger Drink',
            'Starbucks Iced Strawberry Green Tea Lemonade',
            'Starbucks Iced Mango Dragonfruit Refresher',
            'Starbucks Iced Berry Hibiscus Refresher',
            'Starbucks Iced Peach Green Tea',
            'Starbucks Iced Guava White Tea',
            'Starbucks Iced Pineapple Matcha',
            'Starbucks Iced Golden Ginger Ale',
            'Starbucks Iced Strawberry Green Tea',
            'Starbucks Iced Mango Dragonfruit',
            'Starbucks Iced Berry Hibiscus',
            'Starbucks Iced Peach Green Tea Lemonade',
            'Starbucks Iced Guava Passionfruit Drink',
            'Starbucks Iced Pineapple Matcha Drink',
            'Starbucks Iced Golden Ginger Drink',
            'Starbucks Iced Strawberry Green Tea Lemonade',
            'Starbucks Iced Mango Dragonfruit Refresher',
            'Starbucks Iced Berry Hibiscus Refresher',
            'Starbucks Iced Peach Green Tea',
            'Starbucks Iced Guava White Tea',
            'Starbucks Iced Pineapple Matcha',
            'Starbucks Iced Golden Ginger Ale',
            'Starbucks Iced Strawberry Green Tea',
            'Starbucks Iced Mango Dragonfruit',
            'Starbucks Iced Berry Hibiscus'
        ]
        random.shuffle(coffee)
        random_coffee = random.choice(coffee)
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst keinen Kaffee ausgeben! ☕', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} einen {random_coffee} aus! ☕')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} trinkt einen {random_coffee}! ☕')

    @discord.slash_command(name="cookie", description="Iss oder teile einen Keks mit jemandem.")
    async def cookie(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du einen Keks teilen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst keinen Keks geben! 🍪', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} einen Keks! 🍪')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} isst einen Keks! 🍪')
    
    @discord.slash_command(name="dance", description="Tanze alleine oder mit jemandem.")
    async def dance(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du tanzen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} tanzt alleine! 💃🕺')
                return
            await ctx.respond(f'{ctx.author.mention} tanzt mit {member.mention}! 💃🕺')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} tanzt alleine! 💃🕺')
        ctx.send('https://cdn.discordapp.com/attachments/967862584172744775/1034587824789405807/a47kehfpj7t91.gif')

    @discord.slash_command(name="drink", description="Trinke etwas!")
    async def drink(
            self,
            ctx
        ):
        drinks = [
            'ein Glas Wasser',
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Wasser",
            "ein Glas Orangensaft",
            "ein Glas Orangensaft",
            "ein Glas Orangensaft",
            "ein Glas Orangensaft",
            "ein Glas Orangensaft",
            "ein Glas Orangensaft",
            "ein Glas Milch",
            "ein Glas Milch",
            "ein Glas Milch",
            "ein Glas Milch",
            "ein Glas Multivitaminsaft",
            "ein Glas Multivitaminsaft",
            "ein Glas Multivitaminsaft",
            "ein Glas Multivitaminsaft",
            "ein Glas Multivitaminsaft",
            "ein Glas abgestandenes Leitungswasser",
            "ein Glas abgestandenes Leitungswasser",
            "ein Glas abgestandenes Leitungswasser",
            "ein Glas abgestandenes Leitungswasser",
            "ein Glas abgestandenes Leitungswasser",
            "ein Glas von eine dubiosen Flüssigkeit..."
        ]
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587698633113660/jojos-bizarre-adventure-drinks-tea.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587699086118972/jotaro-kujo-drink.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587699547480125/shingeki-no-kyojin-levi.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587700038205520/b1aa3fdc1fd1c06b7e487ff15cc2bdd738510105.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587700478627942/tengen-uzui-drink.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587700990312448/tenya-iida-ingenium.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587701455896617/mirio-togata-my-hero-academia.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587701921456148/anya-spy-x-family.gif",


        ]

        random.shuffle(drinks)
        random_drink = random.choice(drinks)
        await ctx.respond(f'{ctx.author.mention} trinkt {random_drink}! 🥤')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="feed", description="Füttere jemanden.")
    async def feed(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du füttern möchtest."), # type: ignore
            essen: discord.Option(str, "Das Essen, das du füttern möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst füttern! 🍽️', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} füttert {member.mention} mit {essen}! 🍽️')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} füttert sich selbst! 🍽️')

    @discord.slash_command(name="fire", description="Zünde andere an!")
    async def fire(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du anzünden möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586975094706196/fire-force-anime.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586975606427658/sun-breathing.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586976172642345/CookedAntiqueIcelandicsheepdog-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586976575291552/todoroki-shoto21.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586977082806392/798f517adb0745928e6b14065226dcbc.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586977565159525/12888.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586978102034432/lO0lv6.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst anzünden! 🔥', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} zündet {member.mention} an! 🔥')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} zündet sich selbst an! 🔥')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="freeze", description="Friere andere ein!")
    async def freeze(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du einfrieren möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587230888525974/fire-force-fire-force-karim_1.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587231287001108/fire-force-fire-force-karim.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587231668678676/79f949b28233643ac74a6052370516463d760691.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587232041959544/todoroki-ice.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst einfrieren! ❄️', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} friert {member.mention} ein! ❄️')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} friert sich selbst ein! ❄️')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="geld", description="Gib oder erhalte Geld von jemandem.")
    async def geld(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du Geld teilen möchtest.", required=False), # type: ignore
            betrag: discord.Option(int, "Der Betrag, den du teilen möchtest.", required=False) # type: ignore
        ):
        if member and betrag:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst kein Geld geben! 💰', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} {betrag}€! 💰')
        elif member and not betrag:
            await ctx.respond('Bitte gib einen Betrag an!', ephemeral=True)
        elif not member and betrag:
            await ctx.respond(f'{ctx.author.mention} erhält {betrag}€! 💰')
        elif not member and not betrag:
            await ctx.respond(f'{ctx.author.mention} erhält 0€! 💰')

    @discord.slash_command(name="gesundheit", description="Wünsche anderen Gesundheit!")
    async def gesundheit(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, dem du Gesundheit wünschen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst keine Gesundheit wünschen!', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} wünscht {member.mention} Gesundheit!')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} wünscht sich selbst Gesundheit!')

    @discord.slash_command(name="goodvibes", description="Verbreite gute Vibes!")
    async def goodvibes(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, dem du gute Vibes schicken möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} verbreitet gute Vibes! 🌈')
                return
            await ctx.respond(f'{ctx.author.mention} schickt {member.mention} gute Vibes! 🌈')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} verbreitet gute Vibes! 🌈')

    @discord.slash_command(name="gruppenkuscheln", description="Kuschel mit anderen in der Gruppe.")
    async def gruppenkuscheln(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du kuscheln möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} kuschelt alleine! 🤗')
                return
            await ctx.respond(f'{ctx.author.mention} kuschelt mit {member.mention}! 🤗')
        elif not member:
            respones = [
                f'{ctx.author.mention} will den ganzen Chat kuscheln! 🤗',
                f'{ctx.author.mention} lädt alle zum Gruppenkuscheln ein! 🤗',
                f'{ctx.author.mention} kuschelt mit allen! 🤗',
                f'{ctx.author.mention} verbreitet Kuschelstimmung im Chat! 🤗',
                f'{ctx.author.mention} will eine Kuschelparty veranstalten! 🤗',
                f'{ctx.author.mention} kuschelt mit dem gesamten Server! 🤗',
                f'{ctx.author.mention} lädt alle zum Gruppenkuscheln ein! 🤗',
                f'{ctx.author.mention} kuschelt mit allen! 🤗',
                f'{ctx.author.mention} verbreitet Kuschelstimmung im Chat! 🤗',
                f'{ctx.author.mention} zerdrückt den ganzen Chat! 🤗',

            ]
            random.shuffle(respones)
            await ctx.respond(random.choice(respones))

    @discord.slash_command(name="happy", description="Mache andere glücklich!")
    async def happy(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du glücklich machen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} macht sich selbst happy! 😊')
                return
            await ctx.respond(f'{ctx.author.mention} macht {member.mention} happy! 😊')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} macht sich selbst happy! 😊')

    @discord.slash_command(name="hug", description="Umarme jemanden.")
    async def hug(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du umarmen möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584977024761916/bfd50f533f370c2f3e23542d426520215cbd81d3.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584977448378368/anya-hug.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584977830051850/hug-anime.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584978299834388/3b34e762cbb02b9a04b80e75df4989cce17923c8.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584978698285176/tumblr_orotndD1K61vyd25uo1_r1_500.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584979092537394/armin-eren.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} umarmt sich selbst! 🤗')
                return
            await ctx.respond(f'{ctx.author.mention} umarmt {member.mention}! 🤗')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} umarmt sich selbst! 🤗')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="kill", description="Töte andere!")
    async def kill(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du töten möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585343825035315/fcbac4d9b14cdd6a4bbc5f9491c02962.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585344231886858/nezuko-demon-slayer.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585344756170832/c76319fb38068493dd49d2229619c0e4.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585345217540156/1bdd0560df2972c6b7e7f199554ac789.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585345674711102/y5Pr8z.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585346131902495/c149480b72227e94f91eba6ee6c0d261.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} tötet sich selbst! 💀')
                return
            await ctx.respond(f'{ctx.author.mention} tötet {member.mention}! 💀')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} tötet sich selbst! 💀')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="knife", description="Werfe mit Messer!")
    async def knife(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du mit einem Messer treffen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dich nicht selbst mit einem Messer bewerfen! 🔪', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} wirft ein Messer auf {member.mention}! 🔪')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat ein Messer in der Hand! 🔪')

    @discord.slash_command(name="love", description="Hab andere ganz coll lieb!")
    async def love(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du lieb haben möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587519687335996/zenitsu-demon-slayer.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587520056442951/hawks-boku-no-hero-academia.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034587520471683083/Spy_x_Family_-_Episode_8_-_Yor_Lloyd_Heart_Sign.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} hat sich selbst ganz doll lieb! ❤️')
                return
            await ctx.respond(f'{ctx.author.mention} hat {member.mention} ganz doll lieb! ❤️')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat sich selbst ganz doll lieb! ❤️')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="morning", description="Wünsche anderen einen guten Morgen!")
    async def morning(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, dem du einen guten Morgen wünschen möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034588243867467877/fe42ff1c4f57ed0d63934fdf2547af8c.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034588244442099822/my-hero-academia-deku-looks-phone-m07n1oxrta64vsem.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034588244832165918/tumblr_p76ej4j5Yd1wksxcuo1_400.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034589238949326959/6e16ffd10360603454007a03d813c8a75de86347.gif",
            "https://cdn.discordapp.com/attachments/968568845113638925/1053629032073269348/Media_221217_120432.gif"
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dir selbst keinen guten Morgen wünschen! 🌞')
                return
            await ctx.respond(f'{ctx.author.mention} wünscht {member.mention} einen guten Morgen! 🌞')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} wünscht allen einen guten Morgen! 🌞')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="niesen", description="Niese. Das wars.")
    async def niesen(
        self,
        ctx,
        member: discord.Option(discord.Member, "User den du zum niesen bringen willst.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst zum niesen bringen! 🤧', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} bringt {member.mention} zum niesen! 🤧')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} niest! 🤧')

    @discord.slash_command(name="night", description="Wünsche anderen eine gute Nacht!")
    async def night(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, dem du eine gute Nacht wünschen möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585815512272987/207f10e6e3e4772b4805e8b6ff03230206477216.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585815927488512/35adf188a746079d052bf4b15fbe0d363274937d.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585816351117362/6b77f7cd83e9e8fcc41357b1b531ebe27a3aacde.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034585816732815491/spy-x-family-anya.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dir selbst keine gute Nacht wünschen! 🌙')
                return
            await ctx.respond(f'{ctx.author.mention} wünscht {member.mention} eine gute Nacht! 🌙')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} wünscht allen eine gute Nacht! 🌙')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="pat", description="Patte jemanden.")
    async def pat(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du paten möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586325799673856/Tumblr_l_1443334695105275.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586326307192923/fire-force-iris.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586326659506206/aniyuki-anya-spy-x-family-20.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586327007637595/17aed6c0025ddf36ac85fd3481b4c359.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586327355769002/pat-demon-slayer.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034586327750017064/705.gif",
        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} patted sich selbst! 🐾')
                return
            await ctx.respond(f'{ctx.author.mention} patted {member.mention}! 🐾')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} patted sich selbst! 🐾')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])
    
    @discord.slash_command(name="prost", description="Prost!")
    async def prost(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du anstoßen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst nicht zuprosten! 🍻', ephemeral=True)
                return
            if random.randint(1, 5) == 1:
                await ctx.respond(f'{ctx.author.mention} stößt mit {member.mention} auf ein Radler an! 🍻')
            else:
                await ctx.respond(f'{ctx.author.mention} stößt mit {member.mention} auf ein Bier an! 🍻')
        elif not member:
            if random.randint(1, 5) == 1:
                await ctx.respond(f'{ctx.author.mention} stoßt auf ein Radler an! 🍻')
            else:
                await ctx.respond(f'{ctx.author.mention} stoßt auf ein Bier an! 🍻')
    
    @discord.slash_command(name="punch", description="Schlage jemanden.")
    async def punch(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du schlagen möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584032991780864/Media_221025_190044.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584033352486963/26b070c9ebea28c42af73f8309f196ec.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584033776123984/giphy_1.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584034161995867/b100365c58f601417f6d02bc2dcc44e4.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584034526892162/gojo-punch.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584035034415154/AcclaimedFarClumber-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584035479007242/2ba0035666157ac1181d9be7d7dbf635.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584035835531324/tumblr_psyjc58Nvh1ru8plxo1_540.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584036208820304/60a2f913d6bd7c1597f1b7746b60a76f.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584036624052314/fd0c350027c229eb7f77a17e73cc8df8.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584127372005426/66767af902113b20978f5880593b29af.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584127762083860/giphy.gif",
            "https://cdn.discordapp.com/attachments/967862584172744775/1034584128378654760/deku-izuku-midoriya.gif",

        ]
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst schlagen! 👊', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} schlägt {member.mention}! 👊')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat das Verlangen jemanden zu schlagen! 👊')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])

    @discord.slash_command(name="sad", description="Sei traurig.")
    async def sad(
        self,
        ctx,
        member: discord.Option(discord.Member, "Der Benutzer, den du traurig machen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst traurig machen! 😢', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} macht {member.mention} traurig! 😢')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} ist traurig! 😢')

    @discord.slash_command(name="slap", description="Klatsch anderen eine.")
    async def slap(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du klatschen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} klatscht sich selbst eine! 👋', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} klatscht {member.mention} eine! 👋')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat das verlangen jemanden zu klatschen! 👋')

    @discord.slash_command(name="spoon", description="Löffle anderen eine.")
    async def spoon(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du löffeln möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} löffelt sich selbst eine! 🥄')
                return
            await ctx.respond(f'{ctx.author.mention} löffelt {member.mention} eine! 🥄')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat das Verlangen jemanden eine zu löffeln! 🥄')

    @discord.slash_command(name="stare", description="Starre jemanden an.")
    async def stare(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du anstarren möchtest.") # type: ignore
        ):
        gifs = [
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958253057446039/vibing-vivy-flourite-eyes-song.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958254168952933/anya-forger.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958253804040202/benimaru-stare.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958253426561054/jujutsu-kaisen.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958255687282829/attack-on-titan-stare.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958255091699792/mikasa-staring.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958254668058664/762cc6a148081ddb3b132616bd3f753b.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958257000108173/dabi-my-hero-academia.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958256542912622/kimetsu-no-yaiba-demon-slayer.gif",
            "https://cdn.discordapp.com/attachments/1037819436960337990/1080958256119304202/jojo-anime.gif"

        ]
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} starrt sich selbst an! 👀')
                return
            await ctx.respond(f'{ctx.author.mention} starrt {member.mention} an! 👀')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} starrt in die Leere! 👀')
        ctx.send(gifs[random.randint(0, len(gifs) - 1)])
        
    @discord.slash_command(name="stups", description="Stupse jemanden.")
    async def stups(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du stupsen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} stupst sich selbst! 👉')
                return
            await ctx.respond(f'{ctx.author.mention} stupst {member.mention}! 👉')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat das Verlangen jemanden anzustupsen! 👉')

    @discord.slash_command(name="summon", description="Beschwöre jemanden.")
    async def summon(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du beschwören möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} beschwört sich selbst! 🧙')
                return
            await ctx.respond(f'{ctx.author.mention} beschwört {member.mention}! 🧙')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} beschwört sich selbst! 🧙')

    @discord.slash_command(name="tea", description="Trinke oder teile Tee mit jemandem.")
    async def tea(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du Tee trinken möchtest.", required=False) # type: ignore
        ):
        tea = [
                "English Breakfast Tee",
                "Earl Grey Tee",
                "Green Tea",
                "Peppermint Tea",
                "Chamomile Tea",
                "Jasmine Tea",
                "Oolong Tea",
                "White Tea",
                "Matcha Tea",
                "Hibiscus Tea",
                "Rooibos Tea",
                "Lemon Ginger Tea",
                "Mint Verbena Tea",
                "Peach Tranquility Tea",
                "Passion Tango Tea",
                "Mango Black Tea",
                "Strawberry Green Tea",
                "Pineapple Kona Pop Tea",
                "Peach Citrus White Tea",
                "Rev Up Wellness Tea",
                "Royal English Breakfast Tea",
                "Emperor's Clouds and Mist Tea",
                "Mint Majesty Tea",
                "Youthberry Tea",
                "Wild Sweet Orange Tea",
                "Comfort Wellness Tea",
                "Defense Wellness Tea",
                "Rev Up Wellness Tea",
                "Refresh Wellness Tea",
                "Serenity Wellness Tea",
                "Starbucks Chai Tea",
                "Starbucks Green Tea",
                "Starbucks Matcha Tea",
                "Starbucks Earl Grey Tea",
                "Starbucks Passion Tango Tea",
                "Starbucks Peach Tranquility Tea",
                "Starbucks Mint Majesty Tea",
                "Starbucks Royal English Breakfast Tea",
                "Starbucks Emperor's Clouds and Mist Tea",
                "Starbucks Youthberry Tea",
                "Starbucks Wild Sweet Orange Tea",
                "Starbucks Comfort Wellness Tea",
                "Starbucks Defense Wellness Tea",
                "Starbucks Rev Up Wellness Tea",
                "Starbucks Refresh Wellness Tea",
                "Starbucks Serenity Wellness Tea",
        ]
        random.shuffle(tea)
        random_tea = random.choice(tea)
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst keinen Tee ausgeben! ☕', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} einen {random_tea} aus! ☕')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} trinkt einen {random_tea}! ☕')

    @discord.slash_command(name="truthordare", description="Spiele Wahrheit oder Pflicht.")
    async def truthordare(
            self,
            ctx,
            choice: discord.Option(str, "Wähle zwischen Wahrheit oder Pflicht.", choices=["Truth", "Dare"]) # type: ignore
        ):
        if choice == "Truth":
            truths = [
                'Was ist das peinlichste was dir je passiert ist?',
                'Wie viele Menschen hast du bisher geküsst?',
                'Welches Tier passt am besten zu dir und warum?',
                'Welchen Star findest du heiß?',
                'Wen auf diesen Server würdest du daten wenn du müsstest (falls du schon mit jemand hier zusammen bist, zählt diese Person nicht!)',
                'Hast du schonmal was geklaut?',
                'Wer ist dein geheimer Crush?',
                'Wann hattest du das letzte Mal Sex?',
                'Hast du schonmal eine Straftat begangen?',
                'Was würdest du tun wenn du für einen Monat das andere Geschlecht wärst?',
                'Hast du schonmal Drogen genommen (außer Alkohol und Tabak)?',
                'Wer aus der Runde sollte am dringensten zum Friseur?',
                'Was wissen deine Eltern nicht über dich?',
                'Was war deine Modesünde als Kind?',
                'Was ist der peinlichste Gegenstand in deinem Kleiderschrank?',
                'Wie oft wechselst du deine Bettwäsche?',
                'Warst du schon einmal nackt in der Öffentlichkeit?',
                'Hast du schonmal jemand geghostet?',
                'Was war der größte Fehler den du je begangen hast?',
                'Wen in der Runde würdest du küssen wenn du müsstest?'
            ]
            random.shuffle(truths)
            await ctx.respond(f'{ctx.author.mention} deine Wahrheit ist: {random.choice(truths)}')
        elif choice == "Dare":
            dares = [
                'Verteidige einen Furry wenn einer geflamed wird.',
                'Poste das neueste Bild in deiner Galerie.',
                'Joker: Gib jemanden deiner Wahl eine Aufgabe. Führe den Befehl nochmal aus um die Aufgabe für die Person zu erfahren.',
                'Mach nichts.',
                'Mach ein Foto von deiner Momentanen Sicht und poste es hier',
                'Überzeuge den gesamten Chat dazu dass du das andere Geschlecht bist',
                'Der Chat darf entscheiden was du trinken musst',
                'Der Chat darf entscheiden was deine Aufgabe ist',
                'Benimm dich 2 Minuten wie ein Huhn',
                'Schreibe eine versaute Nachricht an deinen letzten Discord/WhatsApp Kontakt. Der Chat entscheidet welche Plattform',
                'Schicke ein Screenshot von der letzten Privatnachricht die du versendet hast',
                'Sprich mit einem bayrischen/sächsischen/anderem Dialekt',
                'Führe eine 3-Minütige Stand-Up-Comendyshow auf'
            ]
            random.shuffle(dares)
            await ctx.respond(f'{ctx.author.mention} deine Pflicht ist: {random.choice(dares)}')

    @discord.slash_command(name="vc", description="Schiebe andere in den Voice Chat.")
    async def vc(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du in den Voice Chat schieben möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dich nicht selbst in den Voice Chat schieben! 🎤', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} schiebt {member.mention} in den Voice Chat! 🎤')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} chillt im Voice Chat! 🎤')

    @discord.slash_command(name="water", description="Gib oder erhalte Wasser von jemandem.")
    async def water(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, mit dem du Wasser teilen möchtest.", required=False) # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dir selbst kein Wasser geben! 💧', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} gibt {member.mention} Wasser! 💧')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} trinkt Wasser! 💧')

    @discord.slash_command(name="welcome", description="Begrüße jemanden.")
    async def welcome(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du begrüßen möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dich nicht selbst begrüßen! 👋')
                return
            await ctx.respond(f'{ctx.author.mention} begrüßt {member.mention}! 👋')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} begrüßt alle! 👋')
    
    @discord.slash_command(name="werfen", description="Bewirf andere mit Sachen")
    async def werfen(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du bewerfen möchtest.") # type: ignore
        ):
        gegenstaende = [
            'einem Toaster',
            'einer Küchenmaschine',
            'einem Kühlschrank',
            'Tom',
            'Deno',
            'einem Fernseher',
            'einer Waschmaschine',
            'einem Trockner',
            'einer Kloschüssel',
            'einer Tür',
            'Tomaten',
            'nassen Lappen',
            'einem Schlappen',
            'einer Glas Flasche',
            'einem Tisch',
            'einer PS1',
            'einer PS2',
            'einer PS3',
            'einer PS4',
            'einer PS5',
            'einer PS6',
            'einer PS7',
            'einer PS8',
            'einer PS69',
            'einer Wii-Mote weil man "vergessen" hat das Bändchen umzubinden',
            'einer Wii-Mote weil man das Bändchen umgebunden hat',
            'einem Auto',
            'einem Opel Astra',
            'einem Keyblade',
            'einem Gecko',
            'einem Sandkorn',
            'einer Genkidama',
            'einem Lichtschwert',
            'einem Pokeball... Gonna catch em all!',
            'einem Controller',
            'einer Lampe',
            'einer Granate',
            'Wurftsternen',
            'Duftbombe weil du stinkst',
            'einem Blatt',
            'einem Wattepad',
            '-1 lagigen Klopapier',
            'einer Europalette',
            'einem Gabelstapler',
            '1ct',
            'einem T-Shirt',
            'einer Jacke',
            'sich selbst. YEEET',
            'einer Portal Gun',
            'einem Waifu-Pillow',
            'einem Schredder',
            'einem Schrank',
            'einem ODM Gear',
            'einem Titan',
            'einem Shonen Protagonist',
            'Nudeln',
            'Ravioli',
            'einem Plastikstrohhalm',
            'einem Glasstrohhalm',
            'einem Plastikteller',
            'einem Pappteller',
            'einem Asthmaspray',
            'einem TicTac',
            'einer Tafel Schokolade',
            'dem Mastersword',
            'der Sonne',
            'der Sonne',
            'der Sonne',
            'der Sonne',
            'der Sonne',
            'einer aufgegessenen Chips Tüte',
            'einem Spiegel',
            'schlechten Game Design',
            'einer Spitzhacke',
            'einem Plastikflugzeug',
            'einem Papierflugzeug',
            'einer Kreditkarte',
            'einem Teddybär',
            'einer RTX 3080',
            'Nintendo Charakteren',
            'Cappy aus Mario Odyssey',
            'den Infinity Stones',
            'Stormbraker',
            'Mjolnir',
            'Captain Americas Schild',
            'einer Gardine',
            'einem Hund',
            'einer Katze',
            'einem Hamster',
            'einem Pferd',
            'einer Schlange',
            'einer giftigen Schlange',
            'einer Oculus Rift',
            'einem Ofen',
            'einem heißen Ofen',
            'einem Lehrer',
            'einem Lehrer. GET EDUCATED!',
            'GLaDOS',
            'einer Zigarette',
            'einem TARDIS',
            'einem Subwoofer',
            'einer Dubstep Gun',
            'einem Schneeball',
            'einem Dalek',
            'einem Feuerball',
            'einem Todesball',
            'einer Majoras Mask',
            'einem Triforce',
            'einer Ocarina of Time',
            'einem Drachi',
            'einem Wolfiii',
            'einem Lutz',
            'einem Floet',
            'einem Greencube',
            'einem Pikmin',
            'einem Bett',
            'Schulden',
            'einer Hochzeit',
            'einem Fussballstadion',
            'der Allianz Arena',
            'Heroin',
            'Obdachlosigkeit',
            'Scheidungspapieren',
            'einer Random Stadt',
            'nichts',
            'einem Auto',
            'ÖKOLJUHBEFPGIWUBEPFGIKUWZGE=F(IPUNWHEPI$O)G=/UZGHWEPOG)IU(HW§=$)T(/"HZ§?)T(U/HGWEPIOVNUDVPOSJvopwu48tzh0ß39284gujhaß9we487zht3ß9rgvjnaße958zg==',
            'Boomern',
            'Lebenshilfe',
            'Depression',
            'einem Bügeleisen',
            'einem traurigen Leben mit einer schlechten Karriere, einer schrecklichen Familie und Krebs im Endstadium',
            'Tot',
            'deiner Mum',
            'einem Hochzeitsring',
            'der Sonne',
            'Rickroll',
            'Hass',
            'schlechten Witzen',
            'Komplimenten',
            'Komplimenten',
            'Komplimenten',
            '~~Komplimenten~~',
            'einem Schwarzen Loch',
            'eine UNO Reverse Karte',
            'Kondomen',
            'einem Kondom',
            'einem Kondom',
            'einem Kondom',
            'einem gebrauchten Kondom',
            'Discord',
            'ICQ',
            'Gardinen',
            'ganz vielen Plüschtieren',
            'einem Kissen',
            'einem Haus',
            'einem Bett',
            'nichts',
            'einer Bibel',
            'Politikern',
            'Mathe',
            'Feenstaub',
            'Diabetis',
            'Atombomben',
            'Dem Bundeskanzler',
            'Zwillingen',
            'einem Average Discord Mod',
            'Internet',
            'einem Laptop',
            'einem IKEA Schrank',
            'einem IKEA Tisch',
            'einer Steckdose',
            'Luft',
            'Kohlenstoffdioxid',
            'Diamanten',
            'Gold',
            'Kupfer',
            'Helium',
            'Wasserbomben',
            'Russland',
            'Deutschland',
            'einem Todesstrahl',
            'einem Buch. GET EDUCATED!',
            'sich selbst',
            'einem Schornstein',
            'einer Geige',
            'Tintenfischen',
            'Salz',
            'Pfeffer',
            'Rattengift',
            'einer Schneelawine',
            'Uran',
            'Iridium',
            'Kalium',
            'einer Dilara',
            'einer Chantal',
            'einem Mehmet',
            'dem Mond',
            'dem Mond (Gewicht: ca. 1/3 deiner Mum)',
            'einem AC-130',
            'Soup',
            'Soupra',
            'Bohnensuppe',
            'Bohnensuppe (Kaffee)',
            'Beans',
            'einer Kettensäge',
            'Corona',
            'einem Affen',
            'Trump',
            'Putin',
            'Angela Merkel',
            'einer Schneeflocke',
            'einem Fussel',
            'AIDS',
            'Ligma',
            "Breath'nt",
            'einer benutzten Atombombe',
            'Kamehameha'
    ]
        gegenstaende = random.choice(gegenstaende)
        if member:
            if member == ctx.author:
                await ctx.respond('Du kannst dich nicht selbst bewerfen! 🎯', ephemeral=True)
                return
            zufallszahl = random.randint(1, 100)
            if zufallszahl <= 5:
                await ctx.respond(f'TRIPLE THROW! {ctx.author.mention} wirft {member.mention} mit {random.choice(gegenstaende)}, {random.choice(gegenstaende)} und {random.choice(gegenstaende)} ab! 🎯')
            elif zufallszahl <= 10:
                await ctx.respond(f'DOUBLE THROW! {ctx.author.mention} wirft {member.mention} mit {random.choice(gegenstaende)} und {random.choice(gegenstaende)} ab! 🎯')
            else:
                await ctx.respond(f'{ctx.author.mention} wirft {member.mention} mit {gegenstaende} ab! 🎯')

    @discord.slash_command(name="yeet", description="Yeet.")
    async def yeet(
            self,
            ctx,
            member: discord.Option(discord.Member, "Der Benutzer, den du yeeten möchtest.") # type: ignore
        ):
        if member:
            if member == ctx.author:
                await ctx.respond(f'{ctx.author.mention} du kannst dich nicht selbst yeeten! 🚀', ephemeral=True)
                return
            await ctx.respond(f'{ctx.author.mention} yeet {member.mention}! 🚀')
        elif not member:
            await ctx.respond(f'{ctx.author.mention} hat das Verlangen jemanden zu yeeten! 🚀')
            
            
    
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot

module.exports = {
    name: 'ready',
    once: true,
/**
 * @param {import('discord.js').Client} client
 */
    execute (client) {
        console.log(`Succesfully logged in as ${client.user.username} with ID ${client.user.id}!`);
        let stati = [
            'Habe ich den Ofen ausgeschaltet?',
            'Sollte ich doch nochmal pinkeln gehen?',
            'Gibt es intelligentes Leben auf der Erde?',
            'Wie heiรt Obama mit Nachnamen?',
            'Roboter รผbernehmen die Meschheit! ๐ค',
			'Wie pusten Drachen Kerzen aus?',
            'A party without a cake is just a meeting.',
            'Schaut alte Projekte an...',
            'Lรถscht alte Videos von Tom... ๐ค',
            'Geht die Audit Logs durch... ๐',
            'Kontrolliert die User... ๐',
            'Kontrolliert die Mods... ๐',
            'Kontrolliert die Admins... ๐',
            'Kontrolliert Tom... ๐',
            'Kontrolliert Deno... ๐',
            'Kontrolliert die Bots... ๐',
            'Plant neue Video Projekte...',
            'Schaut um sich umher...',
            'Schnuppert an Blumen... ๐ธ',
            'Sorgt fรผr Recht und Ordnung...',
            '๐'
        ]

        client.user.setActivity(stati[Math.floor(Math.random() * stati.length)], { type: 'PLAYING' });
    }
}
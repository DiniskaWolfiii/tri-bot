const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('stare')
        .setDescription('Starre andere Leute an')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du anstarren willst...')
                .setRequired(true)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const punchUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958253057446039/vibing-vivy-flourite-eyes-song.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958254168952933/anya-forger.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958253804040202/benimaru-stare.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958253426561054/jujutsu-kaisen.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958255687282829/attack-on-titan-stare.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958255091699792/mikasa-staring.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958254668058664/762cc6a148081ddb3b132616bd3f753b.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958257000108173/dabi-my-hero-academia.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958256542912622/kimetsu-no-yaiba-demon-slayer.gif`,
            `https://cdn.discordapp.com/attachments/1037819436960337990/1080958256119304202/jojo-anime.gif`

        ]
        await interaction.editReply(`*${interaction.user} starrt ${punchUser} an :eyes:*`)
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
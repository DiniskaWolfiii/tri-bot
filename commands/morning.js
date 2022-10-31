const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('morning')
        .setDescription('Wünsch allen einen Guten Morgen!')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User dem du einen guten Morgen wünschen willst')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const goodMorningUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034588243867467877/fe42ff1c4f57ed0d63934fdf2547af8c.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034588244442099822/my-hero-academia-deku-looks-phone-m07n1oxrta64vsem.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034588244832165918/tumblr_p76ej4j5Yd1wksxcuo1_400.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034589238949326959/6e16ffd10360603454007a03d813c8a75de86347.gif`,
        ]
        if (goodMorningUser) return await interaction.editReply(`*${interaction.user} wünscht ${goodMorningUser} einen guten Morgen!*`);
        await interaction.editReply(`*${interaction.user} wünscht allen einen guten Morgen!*`);
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('punch')
        .setDescription('Schlage andere Leute')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du schlagen willst...')
                .setRequired(true)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const punchUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584032991780864/Media_221025_190044.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584033352486963/26b070c9ebea28c42af73f8309f196ec.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584033776123984/giphy_1.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584034161995867/b100365c58f601417f6d02bc2dcc44e4.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584034526892162/gojo-punch.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584035034415154/AcclaimedFarClumber-max-1mb.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584035479007242/2ba0035666157ac1181d9be7d7dbf635.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584035835531324/tumblr_psyjc58Nvh1ru8plxo1_540.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584036208820304/60a2f913d6bd7c1597f1b7746b60a76f.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584036624052314/fd0c350027c229eb7f77a17e73cc8df8.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584127372005426/66767af902113b20978f5880593b29af.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584127762083860/giphy.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584128378654760/deku-izuku-midoriya.gif`,

        ]
        await interaction.editReply(`*${interaction.user} puncht ${punchUser}*`)
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
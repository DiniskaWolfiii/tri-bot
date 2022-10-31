const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('bonk')
        .setDescription('Bonke andere User!')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du bonken willst')
                .setRequired(true)
        ),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const bonkUser = interaction.options.getMember('user');

        let antworten = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369840529448/9c318a317dd198bb82aad58b7ca89c9e.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369525968937/MWEm.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584368766783569/b974ad89701c8dec034ff676b279b21151f1d090.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584368380919968/200.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584369186222220/707c8a90424f107fa8ee661abc2629e9.gif`
        ]
        for (let i = antworten.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const temp = antworten[i];
            antworten[i] = antworten[j];
            antworten[j] = temp;
        }

        await interaction.editReply(`*${interaction.user} bonkt ${bonkUser}*`)
        interaction.channel.send(antworten[Math.floor(Math.random() * antworten.length)]);

    },
};
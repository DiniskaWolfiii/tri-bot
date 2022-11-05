const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('kill')
        .setDescription('Bring Leute um')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du umbringen willst...')
                .setRequired(true)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const killUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585343825035315/fcbac4d9b14cdd6a4bbc5f9491c02962.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585344231886858/nezuko-demon-slayer.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585344756170832/c76319fb38068493dd49d2229619c0e4.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585345217540156/1bdd0560df2972c6b7e7f199554ac789.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585345674711102/y5Pr8z.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585346131902495/c149480b72227e94f91eba6ee6c0d261.gif`,
        ]
        await interaction.editReply(`*${interaction.user} bringt ${killUser} um :skull:*`)
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('stab')
        .setDescription('Stech\' andere Leute ab')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du abstechen willst...')
                .setRequired(true)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const punchUser = interaction.options.getMember('user');
        let gifs = [
            `hier sollte eigentlich ein gif sein...`,

        ]
        await interaction.editReply(`*${interaction.user} sticht ${punchUser} ab*`)
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
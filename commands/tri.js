const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('tri')
        .setDescription('Sag Triforce dass er ein Cutie ist'),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();

        await interaction.editReply(`${interaction.user} findet das Triforce ein Cutie ist :)`);
    },
};
const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('pat')
        .setDescription('Streichel einen anderen User')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du streicheln willst')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const patUser = interaction.options.getMember('user');
        let antworten;

        if (patUser) {
            
            antworten = [
                `*${interaction.user} patted ${patUser}*`,
                `*${interaction.user} patted ${patUser}*`,
                `*${interaction.user} patted ${patUser}*`,
                `*${interaction.user} patted ${patUser} zu Tode*`
            ]
        } else {
            antworten = [
                `*${interaction.user} will gepatted werden*`,
                `*${interaction.user} hat das Verlangen gestreichelt zu werden*`,
                `*${interaction.user} will gepatted werden*`,
                `*${interaction.user} braucht jemand der ihn/sie patted*`,
                `*${interaction.user} patted sich selbst*`,
                `*${interaction.user} patted sich selbst... Kann ihn bitte jemand helfen?*`,
                `*${interaction.user} patted sich selbst in Grund und Boden...*`
            ]
        }
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586325799673856/Tumblr_l_1443334695105275.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586326307192923/fire-force-iris.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586326659506206/aniyuki-anya-spy-x-family-20.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586327007637595/17aed6c0025ddf36ac85fd3481b4c359.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586327355769002/pat-demon-slayer.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586327750017064/705.gif`,
        ]
        await interaction.editReply(antworten[Math.floor(Math.random() * antworten.length)])
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
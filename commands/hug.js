const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('hug')
        .setDescription('Verteile Umarmungen!')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User dem du eine Umarmung geben willst! UwU')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const hugUser = interaction.options.getMember('user');

        let antworten;

        if (hugUser) {

            antworten = [
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} umarmt ${hugUser}*`,
                `*${interaction.user} zerquetscht ${hugUser}*`
            ]
        } else {
            antworten = [
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} will umarmt werden*`,
                `*${interaction.user} hat das Verlangen umarmt zu werden*`,
                `*${interaction.user} braucht jemand der ihn/sie umarmt*`,
                `*${interaction.user} umarmt sich selbst*`,
                `*${interaction.user} umarmt sich selbst... Kann bitte jemand helfen?*`,
                `*${interaction.user} zerquetscht sich selbst...*`
            ]
        }
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584977024761916/bfd50f533f370c2f3e23542d426520215cbd81d3.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584977448378368/anya-hug.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584977830051850/hug-anime.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584978299834388/3b34e762cbb02b9a04b80e75df4989cce17923c8.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584978698285176/tumblr_orotndD1K61vyd25uo1_r1_500.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034584979092537394/armin-eren.gif`,
        ]
        await interaction.editReply(antworten[Math.floor(Math.random() * antworten.length)])
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
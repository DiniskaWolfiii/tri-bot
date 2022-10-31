const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('fire')
        .setDescription('Zünde jemand an!')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User den du anzünden willst')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const fireUser = interaction.options.getMember('user');
        let antworten;

        if (fireUser) {
            
            antworten = [
                `*${interaction.user} zündet ${fireUser} an :fire:*`,
                `*${interaction.user} zündet ${fireUser} an :fire:*`,
                `*${interaction.user} zündet ${fireUser} an :fire:*`,
                `*Beim Versuch ${fireUser} anzuzünden, stolpert ${interaction.user} und setzt ausversehen den Channel in Brand :fire:*`
            ]
        } else {
            antworten = [
                `*${interaction.user} hält einen Feuerball in der Hand, und hat keine Angst diesen einzusetzen :fire:*`,
                `*${interaction.user} zündet sich selbst an :fire:*`,
                `*${interaction.user} zündet sich selbst an... :fire: You good bro?*`,
                `*${interaction.user} zündet sich selbst an :fire:*`,
                `*${interaction.user} zündet sich selbst an :fire:*`
            ]
        }
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586975094706196/fire-force-anime.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586975606427658/sun-breathing.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586976172642345/CookedAntiqueIcelandicsheepdog-size_restricted.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586976575291552/todoroki-shoto21.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586977082806392/798f517adb0745928e6b14065226dcbc.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586977565159525/12888.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034586978102034432/lO0lv6.gif`,
        ]
        await interaction.editReply(antworten[Math.floor(Math.random() * antworten.length)])
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
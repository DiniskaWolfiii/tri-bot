const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('love')
        .setDescription('Hab andere ganz doll Lieb')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User dem du deine Liebe geben willst')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const loveUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587519687335996/zenitsu-demon-slayer.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587520056442951/hawks-boku-no-hero-academia.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587520471683083/Spy_x_Family_-_Episode_8_-_Yor_Lloyd_Heart_Sign.gif`,
        ]
        if (loveUser) return await interaction.editReply(`*${interaction.user} hat ${loveUser} ganz doll Lieb :heart:*`);
        await interaction.editReply(`*Richtige Einstellung ${interaction.user}! Erstmal sich selbst lieben :heart:*`);
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
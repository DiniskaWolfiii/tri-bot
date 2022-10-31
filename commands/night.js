const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('night')
        .setDescription('Wünsch allen eine gute Nacht')
        .addUserOption(option =>
            option.setName('user')
                .setDescription('User dem du eine gute Nacht wünschen willst')
                .setRequired(false)),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();
        const goodNightUser = interaction.options.getMember('user');
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585815512272987/207f10e6e3e4772b4805e8b6ff03230206477216.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585815927488512/35adf188a746079d052bf4b15fbe0d363274937d.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585816351117362/6b77f7cd83e9e8fcc41357b1b531ebe27a3aacde.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034585816732815491/spy-x-family-anya.gif`,
        ]
        if (goodNightUser) return await interaction.editReply(`*${interaction.user} wünscht ${goodNightUser} eine gute Nacht! :zzz:*`);
        await interaction.editReply(`*${interaction.user} wünscht allen eine gute Nacht! :zzz:*`);
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);
    },
};
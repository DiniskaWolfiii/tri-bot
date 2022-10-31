const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {

    data: new SlashCommandBuilder()
        .setName('drink')
        .setDescription('Trinke etwas!'),

    /**
     * @param {import('discord.js').Interaction} interaction
     */
    async execute(interaction) {
        await interaction.deferReply();

        let antworten = [
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Wasser`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Orangensaft`,
            `${interaction.user} trinkt ein Glas Milch`,
            `${interaction.user} trinkt ein Glas Milch`,
            `${interaction.user} trinkt ein Glas Milch`,
            `${interaction.user} trinkt ein Glas Milch`,
            `${interaction.user} trinkt ein Glas Multivitaminsaft`,
            `${interaction.user} trinkt ein Glas Multivitaminsaft`,
            `${interaction.user} trinkt ein Glas Multivitaminsaft`,
            `${interaction.user} trinkt ein Glas Multivitaminsaft`,
            `${interaction.user} trinkt ein Glas Multivitaminsaft`,
            `${interaction.user} trinkt ein Glas abgestandenes Leitungswasser`,
            `${interaction.user} trinkt ein Glas abgestandenes Leitungswasser`,
            `${interaction.user} trinkt ein Glas abgestandenes Leitungswasser`,
            `${interaction.user} trinkt ein Glas abgestandenes Leitungswasser`,
            `${interaction.user} trinkt ein Glas abgestandenes Leitungswasser`,
            `${interaction.user} trinkt ein Glas von eine dubiosen Flüssigkeit...`,
        ]
        let gifs = [
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587698633113660/jojos-bizarre-adventure-drinks-tea.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587699086118972/jotaro-kujo-drink.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587699547480125/shingeki-no-kyojin-levi.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587700038205520/b1aa3fdc1fd1c06b7e487ff15cc2bdd738510105.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587700478627942/tengen-uzui-drink.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587700990312448/tenya-iida-ingenium.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587701455896617/mirio-togata-my-hero-academia.gif`,
            `https://cdn.discordapp.com/attachments/967862584172744775/1034587701921456148/anya-spy-x-family.gif`,


        ]
        for (let i = antworten.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            const temp = antworten[i];
            antworten[i] = antworten[j];
            antworten[j] = temp;
        }

        await interaction.editReply(antworten[Math.floor(Math.random() * antworten.length)])
        interaction.channel.send(gifs[Math.floor(Math.random() * gifs.length)]);

    },
};
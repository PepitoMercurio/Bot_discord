import discord
from discord.ext import commands
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Marlene, prête à l'emploi\nOption abus de pouvoir activée")

@client.command(name="delete")
async def delete(ctx):
    messages = await ctx.channel.history(limit=10)

    for each_message in messages:
        await each_message.delete()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Salut') or message.content.startswith('salut') or message.content.startswith('Bonjour') or message.content.startswith('bonjour') or message.content.startswith('Yo') or message.content.startswith('yo') or message.content.startswith('Bonsoir') or message.content.startswith('bonsoir'):
        with open('media/fanta-salut.mp4', 'rb') as f:
            video = discord.File(f)
        await message.channel.send(file=video)

    if message.content.startswith("bing chiling"):
        await message.channel.send("Zǎo shang hǎo zhōng guó!\nXiàn zài wǒ yǒu bing chilling\nWǒ hěn xǐ huān bing chilling\nDàn shì sù dù yǔ jī qíng jiǔ bǐ bing chilling\nsù dù yǔ jī qíng, sù dù yǔ jī qíng jiǔ\nWǒ zuì xǐ huān\nSuǒ yǐ xiàn zài shì yīn yuè shí jiān\nZhǔn bèi\nYī, èr, sān\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ")
    
    if message.content.startswith("berseuse"):
        await message.channel.send("https://cdn.discordapp.com/attachments/840224925657727077/936031778311897139/3f2b666262867d217ed2d23bfff480c8.mp4")

    # if 'quoi' in message.content.lower():
    #     await message.channel.send('feur')

    await client.process_commands(message)


client.run("OTA3OTY4OTk1OTkzNDY4OTg4.GoP_hF.lKBQW3xVxHM0lCw-tlEBBCSY1Xnq6RuApNqEsw")
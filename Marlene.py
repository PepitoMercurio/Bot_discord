import os
import discord
import random
from discord.ext import commands
from stack import Stack
from hashtable import hashtable_user
from tree2 import tree
from Player import Joueur

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

hashUser = hashtable_user(10)

help = "```Entrez :\n\ncommandes : pour la liste des commandes\n\ngames : pour une recherche de jeux```"

all_commands = "```!hello : Salutation\n\n!chinese : la plus connue des phrase en chinois pour votre plus grand plaisir\n\n!NewYear : Commande spécialement concue pour les plus grand évenement (attention image clignotantes)\n\n!berseuse : Petite beseuse pour bien s'endormir\n\n!Delete : supprime X message\n\n!last_command : dernière commande entrée\n\n!history : liste des dernières commandes entrées\n\n!delete history : supprime l'historique\n\n!add_q : ajout d'une question\n\n!duel : combat entre 2 joueurs\n\n!help_me : liste des commandes & recommandation de jeux```"

#Arble de discution
arbre = tree('Bonjour en quoi puis-je vous aider ?')
arbre.append_question('Voilà la liste des commandes :' + all_commands, ['commandes'], 'Bonjour en quoi puis-je vous aider ?')
arbre.append_question('Vous recherchez de quel constructeur ?', ['games'], 'Bonjour en quoi puis-je vous aider ?')

# Nintendo
arbre.append_question('Quelle console Nintendo ?', ['Nintendo'], 'Vous recherchez de quel constructeur ?')
arbre.append_question('Voilà une liste de jeux', ['Switch', 'DS', '3DS'], 'Quelle console Nintendo ?')
#PC
arbre.append_question('Voilà une liste de jeux', ['PC'], 'Vous recherchez de quel constructeur ?')
#Xbox
arbre.append_question('Quelle console Xbox?', ['Xbox'], 'Vous recherchez de quel constructeur ?')
arbre.append_question('Voilà une liste de jeux', ['Xbox', 'Xbox 360', 'Xbox One', 'Xbox Series'], 'Quelle console Xbox?')
#Playstation
arbre.append_question('Quelle console Playstation?', ['Playstation'], 'Vous recherchez de quel constructeur ?')
arbre.append_question('Voilà une liste de jeux', ['Playstion', 'PS2', 'PS3', 'PS4', 'PS5'], 'Quelle console Playstation?')

#ajout à la hashtable
def add_to_hash(name, hash, user):
    if hash.contains_key(user) == False:
        stack = Stack(name)
        hash.append(user, stack)
    else:
        s = hash.get(user)
        s.push(name)
        hash.append(user, s)

#verifie si la key existe
def check_hash(hash, user):
    if hash.contains_key(user) == False:
        stack = Stack("None")
        hash.append(user, stack)

#message de démarage
@bot.event
async def on_ready():
    print("Marlene, prête à l'emploi\nOption abus de pouvoir activée")

#dit bonjour
@bot.command()
async def hello(ctx):
    user_id = ctx.author.id
    add_to_hash("Salut", hashUser, user_id)
    base_path = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_path, 'media', 'fanta-salut.mp4')
    with open(video_path, 'rb') as f:
        video = discord.File(f)
        await ctx.send(file=video)

#parle chinois (comme John Cena)
@bot.command()
async def chinese(ctx):
    user_id = ctx.author.id
    add_to_hash("bing chiling", hashUser, user_id)
    await ctx.send("Zǎo shang hǎo zhōng guó!\nXiàn zài wǒ yǒu bing chilling\nWǒ hěn xǐ huān bing chilling\nDàn shì sù dù yǔ jī qíng jiǔ bǐ bing chilling\nsù dù yǔ jī qíng, sù dù yǔ jī qíng jiǔ\nWǒ zuì xǐ huān\nSuǒ yǐ xiàn zài shì yīn yuè shí jiān\nZhǔn bèi\nYī, èr, sān\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ\nLiǎng gè lǐ bài yǐ hòu\nSù dù yǔ jī qíng jiǔ")

#Vidéo pour une ambiance de fête
@bot.command()
async def NewYear(ctx):
    user_id = ctx.author.id
    add_to_hash("NewYear", hashUser, user_id)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_path, 'media', 'oeeee.webm')
    with open(video_path, 'rb') as f:
        video = discord.File(f)
        await ctx.send("BONNE ANNEE !!!", file=video)

#Petite berseuse avant de dormir
@bot.command()
async def berseuse(ctx) :
    user_id = ctx.author.id
    add_to_hash("Berseuse", hashUser, user_id)
    base_path = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_path, 'media', 'berseuse.mov')
    with open(video_path, 'rb') as f:
        video = discord.File(f)
        await ctx.send(file=video)

#supprime X message
@bot.command()
async def delete(ctx, amount):
    user_id = ctx.author.id
    add_to_hash("Delete", hashUser, user_id)
    await ctx.channel.purge(limit= int(amount))

#affiche la denière commande entrée
@bot.command()
async def last_command(ctx):
    user_id = ctx.author.id
    check_hash(hashUser, user_id)
    stack = hashUser.get(user_id)
    result = stack.peek()
    await ctx.send("dernière commande utilisée : " + result)

#affiche l'historique de commande
@bot.command()
async def history(ctx):
    user_id = ctx.author.id
    check_hash(hashUser, user_id)
    stack = hashUser.get(user_id)
    txt = "Liste des commandes :\n```\n"
    last_node = stack.last_node
    for i in range(0, stack.size) :
        txt += str(i+1) + "-" + stack.last_node.data + "\n"
        stack.last_node = stack.last_node.next_node
    txt += "\n```"
    stack.last_node = last_node
    await ctx.send(txt)

#supprime l'historique
@bot.command()
async def delete_history(ctx):
    user_id = ctx.author.id
    check_hash(hashUser, user_id)
    stack = hashUser.get(user_id)
    for _ in range(0, stack.size) :
        stack.pop()
    await ctx.send("Historique supprimé avec succès ||petit cochon va||")

#Discution : aide au commandes ou trouver un jeu selon la plateforme
@bot.command()
async def help_me(ctx):
    arbre.current_node = arbre.first_node
    await ctx.send(arbre.get_question() + help)
 
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        reponse = await bot.wait_for('message', check=check)

        if reponse.content.lower() == "exit":
            break
        elif reponse.content.lower() == "reset":
            arbre.current_node = arbre.first_node
            await ctx.send(arbre.get_question() + help)
        elif arbre.send_answer(reponse.content) == "Voilà une liste de jeux":
            base_path = os.path.dirname(os.path.abspath(__file__))
            txt_path = os.path.join(base_path, 'games', reponse.content + '.txt')
            file = discord.File(txt_path)
            await ctx.send(arbre.send_answer(reponse.content) + " " + reponse.content, file=file)
            break
        else :
            await ctx.send(arbre.send_answer(reponse.content))
    await ctx.send("Très bien, bonne journée !")

@bot.command()
async def add_q(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    await ctx.send("entrez la question que vous voulez ajouter")
    question = await bot.wait_for('message', check=check)

    await ctx.send("entrez la question qui précède la question à ajouter")
    previous_question = await bot.wait_for('message', check=check)

    await ctx.send("entrez la/les réponses qui redirigeront vers votre question")
    param_reponses = await bot.wait_for('message', check=check)
    reponses = param_reponses.content.split()
    
    message = await ctx.send("Confirmez les informations : \n```Question : " + question.content + " \nQuestion Précédente : " + previous_question.content + " \nReponses : " + param_reponses.content + "```")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    

    def check_react(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    reaction, user = await bot.wait_for("reaction_add", check=check_react)
    if reaction.emoji == "✅":
        arbre.append_question(question.content,reponses,previous_question.content)
        await ctx.send("La question a été enregistré")
    else:
        await ctx.send("Ajout annulé")

@bot.command()
async def duel(ctx, joueur1: discord.Member, joueur2: discord.Member):
    joueur_1 = Joueur(joueur1)
    joueur_2 = Joueur(joueur2)

    multi_1 = 1
    multi_2 = 1

    def check_j1(m):
        return m.author == joueur_1.user and m.channel == ctx.channel and m.content in ['attaque', 'défense', 'abandon']
    
    def check_j2(m):
        return m.author == joueur_2.user and m.channel == ctx.channel and m.content in ['attaque', 'défense', 'abandon']

    await ctx.send(f"{joueur1.mention} et {joueur2.mention}, que le combat commence !")

    while joueur_1.pv > 0 and joueur_2.pv > 0:
        multi_1 = 1
        multi_2 = 1


        await ctx.send(f"{joueur_1.user.mention} : {joueur_1.pv}, choisissez une action : attaque, défense, abandon")
        choix1 = await bot.wait_for('message', check=check_j1)
        while choix1.content.lower() not in ['attaque', 'défense', 'abandon'] :
            choix1 = await bot.wait_for('message', check=check_j1)

        if choix1.content.lower() == "abandon" :
            joueur_1.pv = 0
            break

        await ctx.send(f"{joueur_2.user.mention} : {joueur_2.pv}, choisissez une action : attaque, défense, abandon")
        choix2 = await bot.wait_for('message', check=check_j2)
        while choix2.content.lower() not in ['attaque', 'défense', 'abandon'] :
            choix2 = await bot.wait_for('message', check=check_j2)

        if choix2.content.lower() == "abandon" :
            joueur_2.pv = 0
            break


        x1 = random.randint(1, 8)
        x2 = random.randint(1, 8)

        if x1 == 8:
            multi_1 = 2
        elif x1 == 1:
            multi_1 = 0

        if x2 == 8:
            multi_1 = 2
        elif x2 == 1:
            multi_1 = 0

        if choix1.content.lower() == "attaque" :
            joueur_1.isAttack = True
            Attaque_1 = joueur_1.attaque * multi_1
            Defense_1 = 0
        else:
            Attaque_1 = 0
            Defense_1 = joueur_1.defense * multi_1

        if choix2.content.lower() == "attaque" :
            joueur_2.isAttack = True
            Attaque_2 = joueur_2.attaque * multi_2
            Defense_2 = 0
        else:
            Attaque_2 = 0
            Defense_2 = joueur_2.defense * multi_2
            
        Dammage_1 = Attaque_1 - Defense_2
        Dammage_2 = Attaque_2 - Defense_1
        joueur_2.pv -= Dammage_1
        joueur_1.pv -= Dammage_2
        
        await ctx.send(f"{joueur_2.user.mention} reçoit {Dammage_1} dégats")
        if Dammage_1 == 20 :
            await ctx.send("Coup Critique")
        elif Dammage_1 == 0 and joueur_1.isAttack:
            await ctx.send("Echec Critique")

        await ctx.send(f"{joueur_1.user.mention} reçoit {Dammage_2} dégats")
        if Dammage_2 == 20 :
            await ctx.send("Coup Critique")
        elif Dammage_2 == 0 and joueur_1.isAttack:
            await ctx.send("Echec Critique")

    if joueur_1.pv <= 0:
        await ctx.send(f"victoire de {joueur_2.user.mention} !!!")
    else:
        await ctx.send(f"victoire de {joueur_1.user.mention} !!!")


# sauvegarde
# @bot.command()
# async def save(ctx):
#     await ctx.send("Sauvegarde en cours veuillez patienter...")
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     json_path = os.path.join(base_path, 'Saves', 'SaveHistory.txt')

#     with open(json_path, 'w') as f:
#         json.dump(hashUser.__dict__, f)
#     await ctx.send("Sauvegarde terminée")

    
bot.run(TOKEN)
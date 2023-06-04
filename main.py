import io
import os
import discord
from discord.ext import commands
from commande.commande_dollar import send_embed
from commande.commande_interogation import send_message_priver
from storage.Livre import Livre

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def hello(ctx):
    print('Hello command received')
    await ctx.send('Hello, Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username} said "{user_message}" ({channel}')
    
    if user_message[0] == '§':
        user_message = user_message[1:]
        print("its working with §")
        await send_embed(message, user_message, is_private=False)
        
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message_priver(username, message, user_message, is_private=True)

    if user_message == "mot spécial":
        csv_path = os.path.join(os.path.dirname(__file__), "documentation", "my_mangas.csv")

        # Vérifier si le fichier existe
        if os.path.exists(csv_path):
            # Ouvrir le fichier CSV et lire son contenu
            with open(csv_path, "r") as file:
                csv_content = file.read()
            
            # Envoyer le fichier CSV dans le canal de discussion
            channel = message.channel
            await channel.send(file=discord.File(io.BytesIO(csv_content.encode()), filename="my_mangas.csv"))
        else:
            print("Le fichier CSV n'existe pas.")

    await bot.process_commands(message)


        
    # elif user_message[0] == '*':
    #     user_message = user_message[1:]
    #     await send_message_priver_api(username, message, user_message, is_private=True)
        
    # elif user_message[:7] == '/manga/':
    #     user_message = user_message[7:]
    #     await send_manga(message, user_message, is_private=False)
        

bot.run('MTA2ODgxMDIwNTM2MzcyMDI1Mg.GwfKou.e2HuSGdfk7PUJhqsuJgn9nyk1RCY34wWnJ2MDU')
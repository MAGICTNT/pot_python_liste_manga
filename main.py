import discord
from discord.ext import commands
from config import MY_CONFIG
from storage.Utilisateur import Utilisateur
from storage.Collection import Collection
from storage import  Session, base

from commande.collection_info import collections
from commande.attribut_info import attributs

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_message(message):

    if message.content.startswith('/'):
        print(f'{message}')
    
    # if message.content.startswith('/voir'):
    #     users = []
    #     with Session() as session:
    #         query = session.query(Utilisateur).all()
    #         for user in query:
    #             user_id = user.id
    #             username = user.pseudo
    #             users.append(f"ID: {user_id}, Username: {username}")

    #     # Envoi des résultats dans le salon Discord
    #     await message.channel.send("\n".join(users))
    if message.content.startswith('*add*manga'):
        mot_split = message.content.split("*")
        await message.channel.send(f'{mot_split}')


    if message.content.startswith('/all/collection'):
        list_collection = collections()
        await message.channel.send(f'{list_collection}')
    elif message.content.startswith('/all/attribut'):
        list_attribut = attributs()
        await message.channel.send(f'{list_attribut}')
    # elif message.content.startswith('all/utilisateur'):
    #     list_utilisateur = utilisateurs()
    #     await message.channel.send(f'{list_utilisateur}')
    if message.content.startswith('/add/collection/'):
        collection = message.content.split('/add/collection/')[1]
        with Session() as session:
            collection_in_data_base = session.query(Collection).filter(Collection.nom == collection).order_by(Collection.id).all()

            if collection_in_data_base:
                await message.channel.send(f'Je suis désoler mais il existe une collection {collection}.')
            else:
                all_collection = session.query(Collection).all()
                new_collection = Collection(id=len(all_collection)+1 ,nom = collection)
                session.add(new_collection)
                session.commit()
                await message.channel.send(f'add de la collection: {collection_in_data_base}')
    if message.content.startswith('/manga/update/'):
        name = message.content.split('/manga/update/')[1]
        await message.channel.send(f"Le manga a mettre a jour est: {name}!")
        await message.content.split('/manga/update/')
    elif message.content.startswith('/manga/delete/'):
        name = message.content.split('/manga/delete/')[1]
        await message.channel.send(f"Le manga a supprimer est: {name}!")

    await bot.process_commands(message)


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     username = str(message.author)
#     user_message = str(message.content)
#     channel = str(message.channel)
#     print(f'{username} said "{user_message}" ({channel}')
    
#     if user_message[0] == '§':
#         user_message = user_message[1:]
#         print("its working with §")
#         await send_embed(message, user_message, is_private=False)
        
#     if user_message[0] == '?':
#         user_message = user_message[1:]
#         await send_message_priver(username, message, user_message, is_private=True)

#     if user_message == "mot spécial":
#         csv_path = os.path.join(os.path.dirname(__file__), "documentation", "my_mangas.csv")

#         # Vérifier si le fichier existe
#         if os.path.exists(csv_path):
#             # Ouvrir le fichier CSV et lire son contenu
#             with open(csv_path, "r") as file:
#                 csv_content = file.read()
            
#             # Envoyer le fichier CSV dans le canal de discussion
#             channel = message.channel
#             await channel.send(file=discord.File(io.BytesIO(csv_content.encode()), filename="my_mangas.csv"))
#         else:
#             print("Le fichier CSV n'existe pas.")

#     await bot.process_commands(message)


        
#     # elif user_message[0] == '*':
#     #     user_message = user_message[1:]
#     #     await send_message_priver_api(username, message, user_message, is_private=True)
        
#     # elif user_message[:7] == '/manga/':
#     #     user_message = user_message[7:]
#     #     await send_manga(message, user_message, is_private=False)
        

bot.run(MY_CONFIG['token'])
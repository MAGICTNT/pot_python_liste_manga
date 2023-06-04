import responses
import requests
import discord
from outil.csv import lecteur
from outil.ajout import ajout_livre,ajout_style

async def send_embed(message, user_message, is_private):
    if user_message.lower() == "all_manga":
        try:
            response_manga = get_manga_all()
            for r in response_manga[1:]:
                url = "https://api.jikan.moe/v4/manga?q=" + r.nom
                reponse = requests.get(url).json()
                image = ""
                lien = ""
                for reponse_data in reponse["data"]:
                    lien = reponse_data["url"]
                    for reponse_images in reponse_data['titles']:
                        if reponse_images["title"].lower() == r.nom.lower():
                            image = reponse_data["images"]["jpg"]["large_image_url"]
                            lien = reponse_data["url"]

                print(lien + "<-")
                embedVar = discord.Embed(title="   **__Nom__** : " + r.nom, url="https://realdrewdata.medium.com/",
                                         description="\n**__Volume__** : " + r.volume, color=0x00ff00)
                embedVar.set_image(url=image)
                embedVar.add_field(name="exmple", value="e", inline=False)
                await message.channel.send(embed=embedVar)
        except Exception as e:
            print(e)
    else:
        try:
            response_manga = responses.get_mangas(user_message)
            for r in response_manga:
                url = "https://api.jikan.moe/v4/manga?q=" + r.nom
                reponse = requests.get(url).json()
                image = ""
                etat = "En cour"
                authors = ""
                genres = ""
                serializations = ""
                for reponse_data in reponse["data"]:
                    for reponse_images in reponse_data['titles']:
                        if reponse_images["title"].lower() == r.nom.lower():
                            image = reponse_data["images"]["jpg"]["large_image_url"]
                            etat = reponse_data["status"]
                            authors = reponse_data["authors"][0]["name"]
                            serializations = reponse_data["serializations"][0]['name']
                            genres =  reponse_data["demographics"][0]["name"]

                embedVar = discord.Embed(title="   **__Nom__** : " + r.nom,
                                         description="\n**__Volume__** : " + r.volume, color=0x00ff00)
                embedVar.add_field(name="**__état:__**", value=etat, inline=True)
                embedVar.add_field(name="**__auteur:__**", value=authors, inline=True)
                embedVar.add_field(name="**__édition:__**", value=serializations, inline=False)
                embedVar.add_field(name="**__style:__**", value=genres, inline=False)
                embedVar.set_image(url=image)
                await message.channel.send(embed=embedVar)

        except Exception as e:
            print(e)
    await message.author.send("\n\nFin de liste") if is_private else await message.channel.send("\n\nFin de liste")


def get_manga_all():
    liste_csv_livre = lecteur('./documentation/my_mangas.csv')
    liste_manga = ajout_style(["Manga", "Comics", "Roman", "Magazine"])
    # for li in liste_manga:
    #    print(li.to_string())
    liste_livre = ajout_livre(liste_csv_livre)

    return liste_livre
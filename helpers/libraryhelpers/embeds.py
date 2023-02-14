import os
import disnake
import ast
from helpers.genhelp.embedhelper import embedbuilder

links = os.environ['DocLinks']
links = ast.literal_eval(links)
selnatainfo = links[0][1]
daervyninfo = links[1][1]
daervynweb = links[2][1]
vayleinfo = links[3][1]
vaporinfo = links[4][1]
ofuriainfo = links[5][1]
tempestiainfo = links[6][1]
lanaetuinfo = links[7][1]
Maps = ["Selnata","Veridian","Daervyn","Vayle","Vapor","Ofuria","Lanae'tu","Tempestia"]
DriveMaps = ast.literal_eval(os.environ['Drive'])
Race = os.environ['races']
Rules = ast.literal_eval(os.environ['RuleLinks'])
Extras = ast.literal_eval(os.environ['extralinks'])
# Extras[ACS,Spells,Guilds,History]


async def libraryembeds(cf):
  category = cf[0]
  if category == "Planes":
    file = cf[1]
    if "J" in file:
      file = file.replace("J","")
      if file == "All":
        embed = await embedbuilder(
          title = "The Planes Known to the Syndicate",
          desc = "These are the seven remaining planes explored by and homes to various members of the Syndicate. Enjoy exploring their rich and in-depth histories! \n- Aasta",
          fieldlist = [["", f"[Selnata]({selnatainfo})",True],["",f"[Daervyn]({daervyninfo})\n[Daervyn Website]({daervynweb})",True],["",f"[Vayle]({vayleinfo})",True],["",f"[Vapor]({vaporinfo})",True],["",f"[Ofuria]({ofuriainfo})\n",True],["",f"[Tempestia]({tempestiainfo})",True],["",f"[Lanae'tu]({lanaetuinfo})",True]],
          author = [">Library >Planes >Info",""]
        )
        return embed
      elif file == "Selnata":
        embed = await embedbuilder(
          title = "The Plane of Selnata",
          desc = "Selnata is the plane which the Syndicate has set up shop, as they say. Though don't think they own the plane. The Syndicate home for their guilds is located on a small island called *The Veridian Isle*. It is quite surprising how small it is compared to the rest of Selnata.\n- Aasta",
          fieldlist = [["",f"[Selnata Document]({selnatainfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Daervyn":
        embed = await embedbuilder(
          title = "The Plane of Daervyn",
          desc = "Daervyn is known for it's races and the Shards. Across Daervyn there are Kitsune Tribes that protect portals to the spirit realm and each tribe is named after a different shard. The Shards are godlike beings, though I can't say much more seeing as not much is known about them. Due to the presence of the Kitsune and the Spirit Realm of Daervyn, Necromancy is extremely hated in many areas and are hunted by some Kitsune. So beware if you intend to raise a soul on the plane... \n- Aasta",
          fieldlist = [["",f"[Daervyn Document]({daervyninfo})",True],["",f"[Daervyn Website]({daervynweb})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Vayle":
        embed = await embedbuilder(
          title = "The Plane of Vayle",
          desc = "Vayle, the plane of Light and Dark. A seemingly constant war between light and dark which has caused those living within it to have difficult lives. Many find peace in the religious aspect of the plane. Believeing in Angelic entities that may roam the plane. You'll be hard pressed to find people on the plane who are familiar with the Syndicate, so keep that in mind... \n- Aasta",
          fieldlist = [["",f"[Vayle Document]({vayleinfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Vapor":
        embed = await embedbuilder(
          title = "The Plane of Vapor",
          desc = "Vapor, the land of steam. It is home to the steam powered vehicles and has the general Western Vibe to it. If you're a tinkerer, this is the place to be. With it's mechs created by its people to help defend the plane from hostility. It is also said only in myths, that dragons have made their home on the plane, but none seem to know the truth behind it. \n- Aasta",
          fieldlist = [["",f"[Vapor Document]({vaporinfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Ofuria":
        embed = await embedbuilder(
          title = "The Plane of Ofuria",
          desc = "Ofuria once a plane of magic, is now a plane crystallized into rubies. Magic is now frowned upon due to mage involvement in the crystallization of the plane. The plane of rubies and ruin is home to the red irised Ofurians that once lived in utopious civilizations. Life has become difficult for the residents of Ofuria, having lost their lavish lives, they rely on other planes to support them as the export the rubies found all over the plane. \n- Aasta",
          fieldlist = [["",f"[Ofuria Document]({ofuriainfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Tempestia":
        embed = await embedbuilder(
          title = "The Plane of Tempestia",
          desc = "Tempestia, the world of storms. The harsh environment has had a large effect on the inhabitants of the plane with some races adapting to their environment in areas they can survive or regions becoming uninhabitable. The plane is home to many specicies of Nymphs but are also home to Elves and various non-planar races. I don't know much more about it, but you should definitely check it out for me! \n- Aasta",
          fieldlist = [["",f"[Tempestia Document]({tempestiainfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
      elif file == "Lanae'tu":
        embed = await embedbuilder(
          title = "The Plane of Lanae'tu",
          desc = "As any who have heard of the plane of Lanae’tu know, it’s a realm primarily composed of sea interspersed by small islands beneath a magnificent, rich skyscape that - at night - is studded with nebulae like jewels in a celestial crown. \n\nSeveral islands and continents of varying sizes dot the plane, from the busy, mercantile port of Lanay Katu, to the pirate nation of Scarda, the idyllic Arcadian Greenlands, and the environmentally diverse continent of Temikor. The island of Juka is home to a great jungle, the lush land of Fae'lu is blanketed by powerful illusions, and Capricorn is home to the magnificent Library of Enka. The Mists of the Wastes are dangerous and ever changing, inhabited by the fearsome Leviathans.\n\nThe islands are home to a broad swathe of peoples, from farmers to aristocrats, and the seas around the islands are home to different Merfolk, each having claimed a portion of the oceans for themselves when they do not dalliance and come onto land. The waves are braved by pirates and sailors, and beneath them, just beneath the hull of their ships, lay creatures as of yet undiscovered.\n\nWelcome to Lanae'tu. \n- Aasta",
          fieldlist = [["",f"[Lanae'tu Document]({lanaetuinfo})",True]],
          author = [">Library >Planes >Info",None]
        )
        return embed
    elif "Z" in file:
      file = file.replace("Z","")
      embeds = []
      if file == "AllMaps":
        for plane in range(len(Maps)):
          planesimp = Maps[plane].replace("'","")
          Map = disnake.File(f"/home/runner/Aasta/databases/images/maps/{planesimp}.png")
          embed = await embedbuilder(
            title = f"{Maps[plane]} Map",
            desc = f"This is the map for {Maps[plane]}",
            image = Map,
            author = [">Library >Planes >Maps",None],
            fieldlist = [["",f"[{Maps[plane]} Map]({DriveMaps[planesimp]})",True]]
          )
          embeds.append(embed)
        return embeds
      elif file != "AllMaps":
        planesimp = file.replace("'","")
        Map = disnake.File(f"/home/runner/Aasta/databases/images/maps/{planesimp}.png")
        embed = await embedbuilder(
          title = f"{file} Map",
          desc = f"This is the map for {file}",
          image = Map,
          author = [">Library >Planes >Maps",None],
          fieldlist = [["",f"[{file} Map]({DriveMaps[planesimp]})",True]]
        )
        return embed
    elif file == "Races":
      embed = await embedbuilder(
        title = "Playable Races",
        desc = "If you're going to play on the Syndicate you've got to be someone from somewhere. So this link below will show you what you can be and from where. Though be aware if it says PA approval you have to check with the Planar Architect over that plane if you want to make a chracter of that race. \n\nWith that said, have fun character creating! \n- Aasta",
        author = [">Library >Planes >Races",None],
        fieldlist = [["",f"[Race Document]({Race})",True]]
      )
      return embed
    else:
      pass
  elif category == "Rules":
    file = cf[1]
    embed = await embedbuilder(
      title = "Rules of the Syndicate",
      desc = "*Hear ye, Hear ye! The Syndicate has declared the laws that those within it must follow!*\n\nAnyway... Here is all of the major rule documents for the the Syndicate. Please take your time to read through these if it is your first time using this command or reading these files. If you are someone who has read these and are just showing someoneelse, Good job to you.\n\nAll jokes aside this files are important to read and let sink in so that you can enjoy playing with us on this server. So have a nice day and roll on! \n- Aasta",
      author = [">Library >Rules",None],
      fieldlist = [["Links!",f"[Rules Folder]({Rules[0]})",False],["",f"[Syndicate Handbook]({Rules[3]})",False],["",f"[Code of Conduct]({Rules[1]})",False],["",f"[Punitive Measures]({Rules[2]})",False]]
    )
    return embed
  elif category == "Magical":
    file = cf[1]
  
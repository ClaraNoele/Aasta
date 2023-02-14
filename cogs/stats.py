#Main Imports
import os
import disnake
from disnake import AllowedMentions, Intents
from disnake.ext import commands, tasks
from enum import Enum
import pytz
from datetime import datetime
import d20
#Other Sheet Imports
from functions.functions import guild
import functions.sheetstats
from functions.sheetstats import Stat_List


stl = Stat_List() 
Skills = commands.option_enum({
  "Athletics":"Athletics",
  "Endurance":"Endurance",
  "Agility":"Agility",
  "Stealth":"Stealth",
  "History":"History",
  "People":"People",
  "Tinkerer":"Tinkerer",
  "Academics":"Academics",
  "Alchemy":"Alchemy",
  "Mysticism":"Mysticism",
  "Fieldcraft":"Fieldcraft",
  "Spirituality":"Spirituality",
  "Animal Handling":"Animal_Handling",
  "Non Magical Healing":"Non_Magical_Healing",
  "Riding":"Riding",
  "Performance":"Performance",
  "Persuasion":"Persuasion",
  "Intimidation":"Intimidation",
  "Deception":"Deception",
  "Observation":"Observation"
})
CPrimary = commands.option_enum({
  "Body":'Body',
  "Dexterity":'Dexterity',
  "Perception":'Perception',
  "Mind":'Mind',
  "Spirit":'Spirit',
  "Charisma":'Charisma',
  "Mental Acuity":'Mental_Acuity',
  "Push Through":'Push_Through',
  "Quick Reflexes":'Quick_Reflexes'
})
Advantage = commands.option_enum({
  "Normal": 0,
  "Advantage": 1,
  "Disadvantage": 2
})

class Stats(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  @commands.slash_command(name = "statsall", description = "All your stats in a nice window!")
  async def all(inter:disnake.ApplicationCommandInteraction):
    did = inter.author.id
    asset = inter.author.display_avatar
    url = asset.url
    didtrue = str(did)
    await inter.response.defer()
    Guildf = await guild(didtrue)
    if (Guildf == '638'):
      await inter.edit_original_response(f"So uh... You don't have a character on my sheet... \n\nPlease refer yourself to a Judicator (Please Ping them for me!) and get yourself set up with a character or get you on my sheet. Thanks!")

    elif (Guildf == '639'):
      await inter.edit_original_response(f"You know this is quite interesting and unusual. \n\nApparently you have no active character on my sheet. Weird right? Go ahead and ping a Judicator about this and see if they can help fix this error.")
    elif (Guildf == '640'):
      await inter.edit_original_response(f"So it seems like you haven't opted in yet... \n\nGo ahead and ping a Judicator and get yourself set up with me! Thanks!")
    values = await stl.all(didtrue)
    if (values == '638'):
      await inter.edit_original_response(f"So uh... You don't have a character on my sheet... \n\nPlease refer yourself to a Judicator (Please Ping them for me!) and get yourself set up with a character or get you on my sheet. Thanks!")

    elif (values == '639'):
      await inter.edit_original_response(f"You know this is quite interesting and unusual. \n\nApparently you have no active character on my sheet. Weird right? Go ahead and ping a Judicator about this and see if they can help fix this error.")
    elif (values == '640'):
      await inter.edit_original_response(f"So it seems like you haven't opted in yet... \n\nGo ahead and ping a Judicator and get yourself set up with me! Thanks!")
    Body, Dex, Perc, Mind, Spirit, Cha, Init, MA, PT, QR, Athl, Endu, Agil, Stea, Hist, Peop, Tink, Acad, Alch, Myst, Fiel, Spir, Anim, NMH, Ridi, Perf, Pers, Inti, Dece, Obse, LB, HB, Pole, Unar, Bows, Shie, Blud, Firea, Fire, Water, Earth, Dark, Light, Wind, Name, Level, Race, Money, CHP, HP, CTHP, THP, CMana, Mana = values
    embed = disnake.Embed(
      title=f"{Name}'s Stats!\n\nLevel: {Level}\nRace: {Race}",
      description=f"\n**Rasps:** {Money}\n**Guild:** {Guildf}\n\nYour Main Stats!\n**HP:** {CHP}/{HP}\n**Temp HP:** {CTHP}/{THP}\n**Mana:** {CMana}/{Mana}\n**Body:** {Body} \u200b**Dexterity:** {Dex} \u200b **Perception:** {Perc}\n**Mind:** {Mind} \u200b **Spirit:** {Spirit} \u200b **Charisma:** {Cha}\n**Initiative:** {Init}\n**Mental Acuity:** {MA}\n**Push Through:** {PT}\n**Quick Reflexes:** {QR}\n\nYour Skills!\n**Academics:** {Acad} \n**Agility:** {Agil} \n**Alchemy:** {Alch} \n**Animal Handling:** {Anim} \n**Athletics:** {Athl} \n**Deception:** {Dece} \n**Endurance:** {Endu} \n**Fieldcraft:** {Fiel} \n**History:** {Hist} \n**Intimidation:** {Inti} \n**Mysticism:** {Myst} \n**Non-Magical Healing:** {NMH} \n**Observation:** {Obse} \n**People:** {Peop} \n**Performance:** {Perf} \n**Persuasion:** {Pers} \n**Riding:** {Ridi} \n**Spirituality:** {Spir} \n**Stealth:** {Stea} \n**Tinkerer:** {Tink} \n\nYour Combat Stats!\n**Bludgeons:** {Blud} \n**Bows:** {Bows} \n**Firearms:** {Firea} \n**Heavy Blades:** {HB} \n**Light Blades:** {LB} \n**Polearms:** {Pole} \n**Shields:** {Shie} \n**Unarmed:** {Unar} \n\nYour Magic!\n**Dark:** {Dark} \n**Earth:** {Earth} \n**Fire:** {Fire} \n**Light:** {Light} \n**Water:** {Water} \n**Wind:** {Wind}",
      color=0x8d0d0d,
      timestamp=datetime.now())
    embed.set_author(
      name=f"Your stat page!",
      icon_url=url)
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_thumbnail(url=url)
  
    await inter.edit_original_response(embed=embed)
  @commands.slash_command(name = "check",description = "Roll a stat check for a specified stat")
  #Start of the stat checks
  async def check(*args,**kwargs):
    pass

  @check.sub_command(name = "primary",description = "Roll a check for your Primary stats!")
  #Stat check for Primary stats
  async def Primary(inter: disnake.ApplicationCommandInteraction, stats: CPrimary):
    did = inter.author.id
    asset = inter.author.display_avatar
    url = asset.url
    didtrue = str(did)
    ch = {stats}
    await inter.response.defer()
    Name,Level,shtlink = await stl.atr({'NameLvl'},didtrue,'None')
  
    if (Name == '638'):
      await inter.edit_original_response(f"So uh... You don't have a character on my sheet... \n\nPlease refer yourself to a Judicator (Please Ping them for me!) and get yourself set up with a character or get you on my sheet. Thanks!")

    elif (Name == '639'):
      await inter.edit_original_response(f"You know this is quite interesting and unusual. \n\nApparently you have no active character on my sheet. Weird right? Go ahead and ping a Judicator about this and see if they can help fix this error.")
    elif (Name == '640'):
      await inter.edit_original_response(f"So it seems like you haven't opted in yet... \n\nGo ahead and ping a Judicator and get yourself set up with me! Thanks!")
    else:
      stat = await stl.atr(ch,didtrue,shtlink)
      if stat == None:
        stat = 0
      ints = stat.replace('+','')
      die = "1d20+" + ints
      roll = d20.roll(die)
      embed = disnake.Embed(
        title=f"{Name} is making a {stats} Check!",
        description=f"**{roll.result}**",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      embed.set_thumbnail(url=url)
      await inter.edit_original_response(embed=embed)
  @check.sub_command(name = "skills",description = "Roll a check for your Skill stats!")
  #Stat check for Skills
  async def Skill(inter: disnake.ApplicationCommandInteraction, stats: Skills):
    did = inter.author.id
    asset = inter.author.display_avatar
    url = asset.url
    didtrue = str(did)
    ch = {stats}
    await inter.response.defer()
    Name,Level,shtlink = await stl.atr({'NameLvl'},didtrue,'None')
  
    if (Name == '638'):
      await inter.edit_original_response(f"So uh... You don't have a character on my sheet... \n\nPlease refer yourself to a Judicator (Please Ping them for me!) and get yourself set up with a character or get you on my sheet. Thanks!")

    elif (Name == '639'):
      await inter.edit_original_response(f"You know this is quite interesting and unusual. \n\nApparently you have no active character on my sheet. Weird right? Go ahead and ping a Judicator about this and see if they can help fix this error.")
    elif (Name == '640'):
      await inter.edit_original_response(f"So it seems like you haven't opted in yet... \n\nGo ahead and ping a Judicator and get yourself set up with me! Thanks!")
    else:
      stat = await stl.atr(ch,didtrue,shtlink)
      if stat == None:
        stat = 0
      ints = stat.replace('+','')
      die = "1d20+" + ints
      roll = d20.roll(die)
      embed = disnake.Embed(
        title=f"{Name} is making a {stats} Check!",
        description=f"**{roll.result}**",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      embed.set_thumbnail(url=url)
      await inter.edit_original_response(embed=embed)




def setup(commands: commands.Bot):
    commands.add_cog(Stats(commands))
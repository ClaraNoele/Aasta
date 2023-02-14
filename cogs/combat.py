import disnake
import disnake.ext
from disnake.ext import commands
import datetime
import d20

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
Combat = commands.option_enum({
  "Light Blades":"Light_Blades",
  "Heavy Blades":"Heavy_Blades",
  "Polearms":"Polearms",
  "Unarmed":"Unarmed",
  "Bows":"Bows",
  "Shields":"Shields",
  "Bludgeons":"Bludgeons",
  "Firearms":"Firearms",
  "Fire":"Fire",
  "Water":"Water",
  "Earth":"Earth",
  "Dark":"Dark",
  "Light":"Light",
  "Wind":"Wind"
})
CPrimary = commands.option_enum({
  "Body":'Body',
  "Dexterity":'Dexterity',
  "Perception":'Perception',
  "Mind":'Mind',
  "Spirit":'Spirit',
  "Charisma":'Charisma',
  "Initiative":'Initiative',
  "Mental Acuity":'Mental_Acuity',
  "Push Through":'Push_Through',
  "Quick Reflexes":'Quick_Reflexes'
})
Advantage = commands.option_enum({
  "Normal": 0,
  "Advantage": 1,
  "Disadvantage": 2
})

class Combat(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  
  @commands.slash_command(name = "attack",description = "Roll an Attack during Combat!")
  #Combat Framework
  async def Combat(inter: disnake.ApplicationCommandInteraction, stats: Combat, adv: Advantage):
    did = inter.author.id
    asset = inter.author.display_avatar
    url = asset.url
    didtrue = str(did)
    ch = {stats}
    await inter.response.defer()
    Name,Level,shtlink = await stl.atr('NameLvl',didtrue,'None')
    
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
      critfinal = 'Normal Attack'
      if adv == 0:
        advnote = 'No Advantage'
        advfinal = '1d20+'
      if adv == 1:
        advnote = 'With Advantage'
        advfinal = '2d20kh1+'
      elif adv == 2:
        advnote = 'With Disadvantage'
        advfinal = '2d20kl1+'
      statname = stats.replace('_',' ')
      ints = stat.replace('+','')
      die = f"{advfinal}" + ints
      roll = d20.roll(die)
      if roll.crit == 'CritType.CRIT':
        crit = d20.roll('1d6')
        critfinal = f"**Crit: {crit}**\nNote: Unless you have an IASC*."
      elif roll.crit == 'CritType.FAIL':
        critfinal = f"**You have been Reprimanded!**\nUnless you have an IASC*."
      embed = disnake.Embed(
        title=f"{Name} is making a {statname} Attack!\n{advnote}",
        description=f"**Total: {roll.total}**\n**{roll.result}**\n\n{critfinal}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      embed.set_thumbnail(url=url)
      await inter.edit_original_response(embed=embed)
    
  @commands.slash_command(name = "initiative",description = "Roll Initiative!")
  #The Initiative command
  async def init(inter: disnake.ApplicationCommandInteraction):
    did = inter.author.id
    asset = inter.author.display_avatar
    url = asset.url
    didtrue = str(did)
    await inter.response.defer()
    Name,Level,shtlink = await stl.atr({'NameLvl'},didtrue,'None')
    
    if (Name == '638'):
      await inter.edit_original_response(f"So uh... You don't have a character on my sheet... \n\nPlease refer yourself to a Judicator (Please Ping them for me!) and get yourself set up with a character or get you on my sheet. Thanks!")

    elif (Name == '639'):
      await inter.edit_original_response(f"You know this is quite interesting and unusual. \n\nApparently you have no active character on my sheet. Weird right? Go ahead and ping a Judicator about this and see if they can help fix this error.")
    elif (Name == '640'):
      await inter.edit_original_response(f"So it seems like you haven't opted in yet... \n\nGo ahead and ping a Judicator and get yourself set up with me! Thanks!")
    else:
      stat = await stl.atr({'Initiative'},didtrue,shtlink)
      if stat == None:
        stat = 0
      ints = stat.replace('+','')
      die = "1d20+" + ints
      roll = d20.roll(die)
      embed = disnake.Embed(
        title=f"{Name} is rolling for Initiative",
        description=f"**{roll.result}**",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      embed.set_thumbnail(url=url)
      await inter.edit_original_response(embed=embed)




def setup(bot: commands.Bot):
    bot.add_cog(Combat(bot))
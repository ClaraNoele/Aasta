import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
from datetime import datetime
from functions.important.client import client
from enum import Enum
import databases.spells

Dark15 = commands.option_enum({
  "Bite of the Bat (1)":"Bite of the Bat",
  "Stinging Curse (1)":"Stinging Curse",
  "Vampiric Strike (2)":"Vampiric Strike",
  "Bite of the Naga (3)":"Bite of the Naga",
  "Cloud of Darkness (3)":"Cloud of Darkness",
  "Lesser Exchange (3)":"Lesser Exchange",
  "Meat Shield (3)":"Meat Shield",
  "Osseous Armor (3)":"Osseous Armor",
  "Vital Division (3)":"Vital Division",
  "Dipped in Blood (4)":"Dipped in Blood",
  "Exchange (4)":"Exchange",
  "Raise Dead (4)":"Raise Dead",
  "Reaper's Essence, Lesser (4)":"Reaper's Essence, Lesser",
  "Unmend Injuries (4)":"Unmend Injuries",
  "Vile Remorse (4)":"Vile Remorse",
  "Bloodletting Armor (5)":"Bloodletting Armor",
  "Crush Their Resolve (5)":"Crush Their Resolve",
  "Greater Exchange (5)":"Greater Exchange",
  "Mortal Wound (5)":"Mortal Wound",
  "Teeth of the Lycan (5)":"Teeth of the Lycan"
})
Dark610 = commands.option_enum({
  "Bathe in Carnage (6)":"Bathe in Carnage",
  "Bite of the Vampire (6)":"Bite of the Vampire",
  "Mortal Barrier (6)":"Mortal Barrier",
  "Reaper's Essence, Greater (6)":"Reaper's Essence, Greater",
  "Transfer Wounds (6)":"Transfer Wounds",
  "Death's Curse (7)":"Death's Curse",
  "Raise Zombie (7)":"Raise Zombie",
  "Redirect (7)":"Redirect",
  "Corruption (8)":"Corruption",
  "Grisly Execution (8)":"Grisly Execution",
  "Siphon Dregs of Life (8)":"Siphon Dregs of Life",
  "Vivisect (8)":"Vivisect",
  "Wound Link (9)":"Wound Link",
  "Life Steal Aura (10)":"Life Steal Aura",
  "Essence Vamp (10)":"Essence Vamp"
})
Earth15 = commands.option_enum({
  "Mending (1)":"Mending",
  "Skin of Reeds (1)":"Skin of Reeds",
  "Stone Jab (1)":"Stone Jab",
  "Coat of Bark (2)":"Coat of Bark",
  "Earthen Barrier (2)":"Earthen Barrier",
  "Granite Cross (2)":"Granite Cross",
  "Commune with Nature (3)":"Commune with Nature",
  "Constricting Vines (3)":"Constricting Vines",
  "Mantle of Wood (3)":"Mantle of Wood",
  "Poison Spray (3)":"Poison Spray",
  "Stone Hammer (3)":"Stone Hammer",
  "Vine Bite (3)":"Vine Bite",
  "Constricting Whip (4)":"Constricting Whip",
  "Earthen Uppercut (4)":"Earthen Uppercut",
  "Primal Reflexes (4)":"Primal Reflexes",
  "Shield of Oak (4)":"Shield of Oak",
  "Thorn (4)":"Thorn",
  "Crushing Kick (5)":"Crushing Kick",
  "Earthen Command (5)":"Earthen Command",
  "Greater Slow (5)":"Greater Slow",
  "Mud Trap (5)":"Mud Trap",
  "Snail Speed (5)":"Snail Speed",
  "Suit of Pine (5)":"Suit of Pine",
  "Ward (5)":"Ward"
})
Earth610 = commands.option_enum({
  "Entomb (6)":"Entomb",
  "Healing Grove (6)":"Healing Grove",
  "Healing Spores (6)":"Healing Spores",
  "Stone Roundhouse (6)":"Stone Roundhouse",
  "Chrysalis (7)":"Chrysalis",
  "Hail of Stone (7)":"Hail of Stone",
  "Plate of Elder Birch (7)":"Plate of Elder Birch",
  "Earthquake (8)":"Earthquake",
  "Rampant Growth (8)":"Rampant Growth",
  "Shattering Earth (8)":"Shattering Earth",
  "Mantle of Buloke (9)":"Mantle of Buloke",
  "Stone Golem (10)":"Stone Golem",
  "Stone Roil (10)":"Stone Roil"
})
Fire15 = commands.option_enum({
  "Cauterize (1)":"Cauterize",
  "Fire Spit (1)":"Fire Spit",
  "Provoke (1)":"Provoke",
  "Sloppy Execution (1)":"Sloppy Execution",
  "Blinding Flare (2)":"Blinding Flare",
  "Fire Bolt (2)":"Fire Bolt",
  "Flaming Dash (2)":"Flaming Dash",
  "Ignite (2)":"Ignite",
  "Reckless Fury (2)":"Reckless Fury",
  "Enamor (3)":"Enamor",
  "Fireball (3)":"Fireball",
  "Heat Metal (3)":"Heat Metal",
  "Remove Spell (3)":"Remove Spell",
  "Spontaneous Immolation (3)":"Spontaneous Immolation",
  "Accelerate (4)":"Accelerate",
  "Alluring Daze (4)":"Alluring Daze",
  "Flame Strike (4)":"Flame Strike",
  "Heat Sink (4)":"Heat Sink",
  "Jet Shot (4)":"Jet Shot",
  "Flame Javelin (5)":"Flame Javelin",
  "Itching Violence (5)":"Itching Violence",
  "Reckless Rage (5)":"Reckless Rage",
  "Ring of Fire (5)":"Ring of Fire"
})
Fire610 = commands.option_enum({
  "Enrage (6)":"Enrage",
  "Persuasive Passion (6)":"Persuasive Passion",
  "Propelled Projectile (6)":"Propelled Projectile",
  "Blinded By Rage (7)":"Blinded By Rage",
  "Explosion (7)":"Explosion",
  "Focused Violence (7)":"Focused Violence",
  "Incinerate Arcana (7)":"Incinerate Arcana",
  "Phoenix Rising (7)":"Phoenix Rising",
  "Searing Flame (7)":"Searing Flame",
  "Growing Fire (8)":"Growing Fire",
  "Double Edged Ego (9)":"Double Edged Ego",
  "Ignite Arcana (9)":"Ignite Arcana",
  "Scorched Earth (9)":"Scorched Earth",
  "Nova (10)":"Nova"
})
Light15 = commands.option_enum({
  "Cast Light (1)":"Cast Light",
  "Minor Heal (1)":"Minor Heal",
  "Shed Some Light (1)":"Shed Some Light",
  "Illuminate Condition (2)":"Illuminate Condition",
  "Make Covenant (2)":"Make Covenant",
  "Pacifist’s Reprieve (2)":"Pacifist's Reprieve",
  "Seek (2)":"Seek",
  "Blinding Flash (3)":"Blinding Flash",
  "Burden of Sin (3)":"Burden of Sin",
  "Clarity (3)":"Clarity",
  "Protect (3)":"Protect",
  "Cleanse (4)":"Cleanse",
  "Force Field (4)":"Force Field",
  "Healing Aura (4)":"Healing Aura",
  "Major Heal (4)":"Major Heal",
  "Smite (4)":"Smite",
  "Barrier (5)":"Barrier",
  "Giver’s Mercy (5)":"Giver's Mercy",
  "Hardlight Armor (5)":"Hardlight Armor",
  "Revive (5)":"Revive",
  "Sanctuary (5)":"Sanctuary"
})
Light610 = commands.option_enum({
  "Confession (6)":"Confession",
  "Fist of Judgment (6)":"Fist of Judgment",
  "Greater Cleanse (6)":"Greater Cleanse",
  "Refracting Ray (6)":"Refracting Ray",
  "Righteous Perseverance (6)":"Righteous Perseverance",
  "Greater Force Field (7)":"Greater Force Field",
  "Officiate Duel (7)":"Officiate Duel",
  "Teleport (7)":"Teleport",
  "Blessed Persistence (9)":"Blessed Persistence",
  "Revitalize (9)":"Revitalize",
  "True Resurrect (10)":"True Resurrect",
  "Radiance (10)":"Radiance"
})
Water15 = commands.option_enum({
  "Disrupt (1)":"Disrupt",
  "Draining Burst (1)":"Draining Burst",
  "Flash Freeze (1)":"Flash Freeze",
  
  "Detection (2)":"Detection",
  "Frozen Plate (2)":"Frozen Plate",
  "Mana Transfer (2)":"Mana Transfer",

  "Arcane Theft (3)":"Arcane Theft",
  "Douse (3)":"Douse",
  "Hush (3)":"Hush",
  "Ice Spike (3)":"Ice Spike",

  "Interrupt (4)":"Interrupt",
  "Polar Snap (4)":"Polar Snap",
  "Reflect Spell (4)":"Reflect Spell",
  "Spectral Sight (4)":"Spectral Sight",
  "Suggest (4)":"Suggest",

  "Mana Burn (5)":"Mana Burn",
  "Slumber (5)":"Slumber"
})
Water610 = commands.option_enum({
  
  "Arcane Bolt (6)":"Arcane Bolt",
  "Disappearance (6)":"Disappearance",
  "Waterbreathing (6)":"Waterbreathing",
  "Mana Lock (6)":"Mana Lock",

  "Mana Fount (7)":"Mana Fount",
  "Shatter (7)":"Shatter",
  "Undertow (7)":"Undertow",

  "Arcane Hemorrhage (8)":"Arcane Hemorrhage",
  "Arcane Missile (8)":"Arcane Missile",
  "Mirror Spell (8)":"Mirror Spell",
  "Spell Shield (8)":"Spell Shield",

  "Extinguish Arcana (9)":"Extinguish Arcana",
  "Spell Surge (9)":"Spell Surge",

  "Glacial Barrage (10)":"Glacial Barrage",
  "Tidal Wave (10)":"Tidal Wave",
  "Torrential Downpour (10)":"Torrential Downpour"

})
Wind15 = commands.option_enum({
  "Dart Draft (1)":"Dart Draft",
  "Forced Focus (1)":"Forced Focus",
  "Inner Voice (1)":"Inner Voice",
  "Light Hearted (1)":"Light Hearted",

  "Reach Beyond (2)":"Reach Beyond",
  "Stinging Stream (2)":"Stinging Stream",

  "Bruising Blast (3)":"Bruising Blast",
  "Great Gust (3)":"Great Gust",
  "Resolute Soul (3)":"Resolute Soul",
  "Steal Breath (3)":"Steal Breath",
  "Wall of wind (3)":"Wall of Wind",
  "Whirling Wind (3)":"Whirling Wind",

  "Air’s Agility (4)":"Air's Agility",
  "Call to Aid (4)":"Call to Aid",
  "Cloak of Winds (4)":"Cloak of Winds",
  "Crosswind (4)":"Crosswind",
  "Force From Within (4)":"Force From Within",
  "Soul Tether (4)":"Soul Tether",
  "Whip of Wind (4)":"Whip of Wind",

  "Crushing Gust (5)":"Crushing Gust",
  "Howling Curse (5)":"Howling Curse",
  "Sending Zephyr (5)":"Sending Zephyr",
  "Collected Focus (5)":"Collected Focus"
})
Wind610 = commands.option_enum({
  "Awaken Speed (6)":"Awaken Speed",
  "Sonic Flight (6)":"Sonic Flight",
  "Splitting Gusts (6)":"Splitting Gusts",
  "Tossing Tempest (6)":"Tossing Tempest",
  "Wind Prison (6)":"Wind Prison",
  "Winds of Pacifism (6)":"Winds of Pacifism",

  "Air Heist (7)":"Air Heist",
  "Delay Fate (7)":"Delay Fate",
  "Roaring Zephyr (7)":"Roaring Zephyr",

  "Beyond Self (8)":"Beyond Self",

  "Hurling Hurricane (9)":"Hurling Hurricane"

})

class Spells(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot

  
  @commands.slash_command(name = "cast",description = "Spellcasting!")
  async def cast(*args,**kwargs):
    pass
  @commands.slash_command(name = "cast2",description = "Spellcasting!")
  async def cast2(*args,**kwargs):
    pass
  @cast.sub_command_group(name = "dark",description = "Dark Spell list")
  async def dark(*args,**kwargs):
    pass
  @dark.sub_command(name = "lvls1-5",description = "Dark Spells levels 1 through 5")
  async def dark15(inter: disnake.ApplicationCommandInteraction, spell:Dark15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.dark_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @dark.sub_command(name = "lvls6-10",description = "Dark Spells levels 6 through 10")
  async def dark610(inter: disnake.ApplicationCommandInteraction, spell:Dark610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.dark_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    


  @cast.sub_command_group(name = "earth", description = "Earth Spell list")
  async def earth(*args,**kwargs):
    pass
  @earth.sub_command(name = "lvls1-5",description = "Earth Spells levels 1 through 5")
  async def earth15(inter: disnake.ApplicationCommandInteraction, spell:Earth15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.earth_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)

  @earth.sub_command(name = "lvls6-10",description = "Earth Spells levels 6 through 10")
  async def earth610(inter: disnake.ApplicationCommandInteraction, spell:Earth610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.earth_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @cast.sub_command_group(name = "fire",description = "Fire Spell list")
  async def fire(*args,**kwargs):
    pass
  @fire.sub_command(name = "lvls1-5",description = "Fire Spells levels 1 through 5")
  async def fire15(inter: disnake.ApplicationCommandInteraction, spell:Fire15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.fire_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)

  @fire.sub_command(name = "lvls6-10",description = "Fire Spells levels 6 through 10")
  async def fire610(inter: disnake.ApplicationCommandInteraction, spell:Fire610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.fire_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @cast2.sub_command_group(name = "light",description = "Light Spell list")
  async def light(*args,**kwargs):
    pass
  @light.sub_command(name = "lvls1-5",description = "Light Spells levels 1 through 5")
  async def light15(inter: disnake.ApplicationCommandInteraction, spell:Light15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.light_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)

  @light.sub_command(name = "lvls6-10",description = "Light Spells levels 6 through 10")
  async def light610(inter: disnake.ApplicationCommandInteraction, spell:Light610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.light_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @cast2.sub_command_group(name = "water",description = "Water Spell list")
  async def water(*args,**kwargs):
    pass

  @water.sub_command(name = "lvls1-5",description = "Water Spells levels 1 through 5")
  async def water15(inter: disnake.ApplicationCommandInteraction,spell:Water15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.water_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Mastery,Prof15 = values
    if Prof10 == None and Mastery == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Mastery == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:**  {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Mastery == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Mastery == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Mastery != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Flowing Mastery:** {Mastery}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Mastery != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Flowing Mastery:** {Mastery}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Mastery != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Flowing Mastery:** {Mastery}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Mastery != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Flowing Mastery:** {Mastery}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)

  @water.sub_command(name = "lvls6-10",description = "Water Spells levels 6 through 10")
  async def water610(inter: disnake.ApplicationCommandInteraction,spell:Water610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.water_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Mastery,Prof15 = values
    if spelly == "Undertow":
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 == None and Mastery == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 != None and Mastery == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 != None and Mastery == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 == None and Mastery == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 == None and Mastery != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Flowing Mastery:** {Mastery}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 != None and Mastery != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Flowing Mastery:** {Mastery}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 != None and Mastery != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Flowing Mastery:** {Mastery}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif Prof10 == None and Mastery != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Flowing Mastery:** {Mastery}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @cast2.sub_command_group(name = "wind",description = "Wind Spell list")
  async def wind(*args,**kwargs):
    pass
  @wind.sub_command(name = "lvls1-5",description = "Wind Spells levels 1 through 5")
  async def wind15(inter: disnake.ApplicationCommandInteraction, spell:Wind15):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.wind_lvlone_five.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)

  @wind.sub_command(name = "lvls6-10",description = "Wind Spells levels 6 through 10")
  async def wind610(inter: disnake.ApplicationCommandInteraction, spell:Wind610):
    await inter.response.defer()
    spelly = f"{spell}"
    values = databases.spells.Wind_lvlsix_ten.get(spelly)
    Purpose,Lvl,MP,Range,Ability,Prof10,Prof15 = values
    if Prof10 == None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 != None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}\n**Prof 15:** {Prof15}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 != None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}\n**Upgrade:** You can choose to use upgraded effects when you unlock the proper proficiency, spending the new mana cost.\n**Prof 10:** {Prof10}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    if Prof10 == None and Prof15 == None:
      embed = disnake.Embed(
        title=f"{spelly}",
        description=f"**{Purpose}**\n**Lvl:** {Lvl}\n**MP:** {MP}\n**Range:** {Range}\n**Ability:** {Ability}",
        color=0x8d0d0d,
        timestamp=datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)




def setup(commands: commands.Bot):
    commands.add_cog(Spells(commands))
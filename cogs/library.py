import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
import datetime
from functions.important.client import client
from enum import Enum

import helpers.libraryhelpers.embeds as hpem


planeinfo = commands.option_enum({
  "All Planes":"AllJ",
  "Selnata":"SelnataJ",
  "Daervyn":"DaervynJ",
  "Vayle":"VayleJ",
  "Vapor":"VaporJ",
  "Ofuria":"OfuriaJ",
  "Tempestia":"TempestiaJ",
  "Lanae'tu":"Lanae'tuJ",
  "All Maps":"AllMapsZ",
  "Selnata Map":"SelnataZ",
  "Veridian Isle Map":"VeridianZ",
  "Daervyn Map":"DaervynZ",
  "Vayle Map":"VayleZ",
  "Vapor Map":"VaporZ",
  "Ofuria Map":"OfuriaZ",
  "Tempestia Map":"TempestiaZ",
  "Lanae'tu Map":"Lanae'tuZ",
  "Races":"Races",
})


class Library(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  @commands.slash_command(name="library",description = "Start of my Library command line")
  async def library(*args,**kwargs):
    pass
  @library.sub_command(name = "planes",description = "Plane Folder from the Syndicate Library")
  async def planes(inter: disnake.ApplicationCommandInteraction,pi:planeinfo):
    await inter.response.defer()
    cf = ["Planes",pi]
    embed = await hpem.libraryembeds(cf)
    if type(embed) == list:
      i = 0
      for fif in range(len(embed)):
        if i == 0:
          await inter.edit_original_response(embed=embed[0])
          i += 1
        elif i >= 1:
          await inter.followup.send(embed=embed[fif])
    elif type(embed) != list:
      await inter.edit_original_response(embed=embed)
    else:
      await inter.edit_originial_response(f"Something Went Wrong")


  @library.sub_command(name = "rules",description = "Syndicate Rules")
  async def rules(inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    cf = ["Rules",None]
    embed = await hpem.libraryembeds(cf)
    await inter.edit_original_response(embed=embed)
  @library.sub_command(name = "magical",description = "The collection for Spells and Abilities")
  async def magical(inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    cf = ["Magical",None]
    embed = await hpem.libraryembeds(cf)
    await inter.edit_original_response(embed=embed)
  
def setup(commands: commands.Bot):
    commands.add_cog(Library(commands))
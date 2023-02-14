import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
import datetime
from functions.important.client import client

class Weavers(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  @commands.has_role("Questmaster")
  @commands.slash_command(name = "champcheck",description = "For QMs and FWs to check characters champ status")
  async def champcheck(self,inter: disnake.ApplicationCommandInteraction,dids):
    await inter.response.defer()
    libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
    didlist = dids.split(",")
    embedstring = "The following characters are classified as follows:\n"
    if len(didlist) > 1:
      for did in range(len(didlist)):
        cellst = libsheet.findall(didlist[did],in_column=45)
        for each in cellst:
          rowvalue = each.row
          val = libsheet.cell(rowvalue,42).value
          if val == 'TRUE':
            level = int(libsheet.cell(rowvalue,5).value)
            name = libsheet.cell(rowvalue,2).value
            break
          elif val == 'FALSE':
            continue
        list = [name,level]
        if list[1] >= 10:
          didstring = f"<@!{didlist[did]}>'s character, {list[0]}, is a Champion!\n"
        elif list[1] <= 9:
          didstring = f"<@!{didlist[did]}>'s character, {list[0]}, is an Adventurer!\n"
        embedstring = embedstring + didstring
      embed = disnake.Embed(
        title=f"Champion Checker!",
        description=embedstring,
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    else:
      cellst = libsheet.findall(didlist[0],in_column=45)
      for each in cellst:
        rowvalue = each.row
        val = libsheet.cell(rowvalue,42).value
        if val == 'TRUE':
          level = int(libsheet.cell(rowvalue,5).value)
          name = libsheet.cell(rowvalue,2).value
          break
        elif val == 'FALSE':
          continue
      list = [name,level]
      if list[1] >= 10:
        didstring = f"<@!{didlist[0]}>'s character, {list[0]}, is a Champion!\n"
      elif list[1] <= 9:
        didstring = f"<@!{didlist[0]}>'s character, {list[0]}, is an Adventurer!\n"
      embedstring = embedstring + didstring
    embed = disnake.Embed(
      title=f"Champion Checker!",
      description=embedstring,
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    await inter.edit_original_response(embed=embed)
    


def setup(commands: commands.Bot):
    commands.add_cog(Weavers(commands))
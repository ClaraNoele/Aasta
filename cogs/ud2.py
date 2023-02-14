import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
import datetime
from functions.important.client import client

from helpers.d2helpers.basichelpers import helpers
from helpers.d2helpers.changer import charlist

import functions.sheetstats
from functions.sheetstats import Stat_List as stl

from helpers.genhelp.embedhelper import embedbuilder

import functions.log
from functions.log import errorlog
groles = {
  'Hallowed Vanguard':565128126804393992,
  'Neverdawn Network':565128188565651458,
  'Oathbreakers':878401513049952326,
  'Steadfast':632269085610082305,
  'Feast':949072147345723492,
  'Order of the Morning':945550823159652414
}
rolelist = [565128126804393992,565128188565651458,878401513049952326,632269085610082305,949072147345723492,945550823159652414]
rolelit = [1037099906873172009,1037099948153516154,1037099956911210588,1025216777652813874]
class UserD2(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
    
  @commands.slash_command(name = "change",description = "Process to change your character on the server")
  async def change(self,inter: disnake.ApplicationCommandInteraction):
    did = inter.author.id
    authoritem = inter.author
    didtrue = str(did)
    guild1 = inter.guild
    guild2 = self.bot.get_guild(558375078258147349)
    member = self.bot.get_guild(558375078258147349).get_member(did)
    guilds = [guild1,guild2,member]
    channel = inter.channel_id
    if channel == 631563912558542868:
      await inter.send(f"Gathering your characters...")
      try:
        valid,time = await helpers.valid(didtrue)
      except Exception as e:
        await errorlog(e)
        embed = disnake.Embed(
          title=f"**Error Occured**",
          description=f"Sorry it looks like I was unable to determine what the time was when you last changed characters.",
          color=0x8d0d0d,
          timestamp=datetime.datetime.now())
        embed.set_footer(
          text="Aasta by Clara Noele",
          icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
        await inter.edit_original_response(embed=embed)
      if valid == 'valid':
        autolog = await self.bot.fetch_channel(577603764513669142)
        menu, v = await helpers.userd2(didtrue)
        char = charlist()
        iteri = 1
        charmenu = char.SelectView(didtrue,menu,v,inter,iteri,autolog,time,authoritem,guilds)
        if menu == "780":
          await inter.edit_original_response(f"It doesn't seem to be that you have more than one character that isn't retired or active. Sorry that means you cannot use this command. \n\nIf this is wrong, please contact Clara.")
        else:
          await inter.edit_original_response("Choose a Character!",view=charmenu)
      elif valid == 'invalid':
        embed = disnake.Embed(
          title=f"**Change Failed!**",
          description=f"Sorry, <@!{didtrue}>. \nIt seems you still have {time} until you can change your character again. \n\nPlease come back then.",
          color=0x8d0d0d,
          timestamp=datetime.datetime.now())
        embed.set_footer(
          text="Aasta by Clara Noele",
          icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
        await inter.edit_original_response(embed=embed)
    elif channel != 631563912558542868:
      await inter.send(f"This command cannot be used in any other channel except <#631563912558542868>! Please go to that channel to use this command.")
  @commands.has_role("Judicator")
  @commands.slash_command(name = "freebie",description = "Judicator update tool")
  async def freebie(self,inter: disnake.ApplicationCommandInteraction,did: str):
    await inter.response.defer()
    channel = inter.channel_id
    if channel == 565131192819646493:
      sheet = client.open('Timesheet').sheet1
      didfinal = sheet.find(did,in_column=1)
      if didfinal != None:
        row = didfinal.row
        time = sheet.cell(row,2).value
        timeint = int(time)
        freebie = (timeint-604800)
        sheet.update(f"B{row}",freebie)
        await inter.edit_original_response(f"Updated <@!{did}>'s time sheet. \nThey can now change their character again.")
      else:
        await inter.edit_original_response(f"<@!{did}> is not on the time sheet.")
        await inter.delete_original_response(delay=30)
    elif channel != 565131192819646493:
      await inter.edit_original_response(f"Sorry Judicator, you need to keep this command secret. Please use it in <#565131192819646493>!")
      await inter.delete_original_response(delay=30)
  @commands.slash_command(name = "timecheck",description = "Checks whether or not you can change characters.")
  async def timecheck(self,inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    did = inter.author.id
    didtrue = str(did)
    valid,time = await helpers.valid(didtrue)
    if valid == 'valid':
      embed = disnake.Embed(
        title=f"**Change Available!**",
        description=f"<@!{didtrue}>! It looks like you're good to change your character at any time! \n\nI look forward to seeing who you change into next!",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
    elif valid == 'invalid':
      embed = disnake.Embed(
        title=f"**Change Unavailable!**",
        description=f"<@!{didtrue}>! \nYou still have {time} until you can change your character again. \n\nHope this helps!",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await inter.edit_original_response(embed=embed)
  @commands.slash_command(name = "update",description = "Updates a characters timesheet in case I was asleep!")
  async def update(self, inter: disnake.ApplicationCommandInteraction,userid: str,changetime: str):
    await inter.response.defer()
    check = await helpers.updatetime(userid,changetime)
    if check == 'Done':
      embed = await embedbuilder(
        title = "Timesheet Updated!",
        desc = f"I changed the timesheet for <@!{userid}>! \n\nSorry for taking a nap on the job. Everyone needs a break sometimes. *yawn*"
      )
    elif check == "Failure":
      embed = await embedbuilder(
        title = "Update Failed",
        desc = f"Looks like <@!{userid}> is not on my timesheet, looks like they haven't used the /change command!"
      )
    else:
      embed = await embedbuilder(
        title = "Error!",
        desc = f"There was an error trying to change the time for <@!{userid}>!"
      )
    await inter.edit_original_response(embed=embed)
  
def setup(commands: commands.Bot):
    commands.add_cog(UserD2(commands))
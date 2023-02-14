import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
import datetime
from functions.important.client import client
from helpers.reghelp.reghelper import reghelp
from helpers.reghelp.basichelpers import helpers

class Register(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  @commands.slash_command(name = "register",description = "Input your character sheet link and choose a character!")
  async def register(self, inter: disnake.ApplicationCommandInteraction, charactersheetlink: str):
    shtlink = charactersheetlink
    did = inter.author.id
    didtrue = str(did)
    channel = inter.channel_id
    if channel == 631563912558542868:
      await inter.send(f"Fetching your characters...")
      autolog = await self.bot.fetch_channel(577603764513669142)
      charlist, guildlist = await helpers.registercheck(didtrue)
      reg = reghelp()
      charmenu = reg.SelectView(did,charlist,guildlist,inter,autolog,shtlink)
      if charlist == "890":
        await inter.edit_original_response(f"Seems we've gotten you squared away! No need to use this command anymore. \n\nThough is this is incorrect please contact a Judicator about this message.\n**Have a Nice Day!**")
      else:
        await inter.edit_original_response("Which Character's Sheet is this?",view=charmenu)
    elif channel != 631563912558542868:
      await inter.send(f"This command cannot be used in any other channel except <#631563912558542868>! Please go to that channel to use this command.")
    




def setup(commands: commands.Bot):
    commands.add_cog(Register(commands))
import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime

from helpers.reghelp.basichelpers import helpers
from helpers.reghelp.buttons import buttonset


class reghelp():
  
  class Select(disnake.ui.Select):
    def __init__(self,did,charlists,guildv,inter,autolog,link):
      self.inter = inter
      self.link = link
      self.autolog = autolog
      self.did = did
      self.charlist = charlists
      self.guildv = guildv
      self.options = []
      for i in range(len(self.charlist)):
        optionselect = disnake.SelectOption(label=self.charlist[i], value=self.charlist[i], description=f"is a {self.guildv[i]} member.")
        self.options.append(optionselect)
      super().__init__(placeholder="Choose One!",options=self.options)
    async def callback(self,inter):
      buttons = await buttonset(self.did,self.values[0],self.inter,self.autolog,self.link)
      button3 = Button(style=disnake.ButtonStyle.primary,label="Wrong One!",custom_id="back")
      async def button_callback3(interaction):
        men = reghelp.Select(self.did,self.charlist,self.guildv,self.inter,self.autolog,self.link)
        charmenu = disnake.ui.View()
        charmenu.add_item(men)
        
        await inters.followup.send("Choose One!",view=charmenu,delete_after=15)
      button3.callback = button_callback3
      buttons.add_item(button3)
      
      await self.inter.delete_original_response(delay=0)
      
      await self.inter.followup.send(f"<@!{self.did}>!\nThis will register **{self.values[0]}**.\nIs this the correct sheet for the character or should we go back?\n\nYou can **cancel** this interaction with **I Changed my Mind**.",view=buttons,delete_after=15)
      
  class SelectView(disnake.ui.View):
      def __init__(self,did,charlists,guildv,inter,autolog,link):
          timeout = 180
          super().__init__(timeout=timeout)
          self.add_item(reghelp.Select(did,charlists,guildv,inter,autolog,link))
import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime
import helpers.d2helpers.basichelpers
import helpers.d2helpers.buttons
from helpers.d2helpers.buttons import buttonset1
from helpers.d2helpers.basichelpers import helpers

async def truefalse(tf):
  libsheet = client.open('Character Library').sheet1
  if tf == 'TRUE':
    libsheet.update('B11', True)
    return 'TRUE'
  if tf == 'FALSE':
    libsheet.update('B11',False)
    return 'FALSE'



class charlist():
  
  class Select(disnake.ui.Select):
    def __init__(self,did,charlists,guildv,inter,iteri,autolog,first,author,guilds):
      self.inter = inter
      self.iteri = iteri
      self.first = first
      self.guilds = guilds
      self.author = author
      self.autolog = autolog
      self.did = did
      self.charlist = charlists
      self.guildv = guildv
      self.options = []
      for i in range(len(self.charlist)):
        optionselect = disnake.SelectOption(label=self.charlist[i], value=self.charlist[i], description=f"is a {self.guildv[i]} member.")
        self.options.append(optionselect)
      super().__init__(placeholder="Choose a Character",options=self.options)
    async def callback(self,inter):
      inters = self.inter
      buttons = await buttonset1(self.did,self.values[0],self.inter,self.autolog,self.first,self.author,self.guilds)
      button3 = Button(style=disnake.ButtonStyle.primary,label="Take Me Back",custom_id="back")
      async def button_callback3(interaction):
        buttons.stop()
        iteri = 2
        men = charlist.Select(self.did,self.charlist,self.guildv,self.inter,self.iteri,self.autolog,self.first,self.author,self.guilds)
        charmenu = disnake.ui.View()
        charmenu.add_item(men)
        
        await inters.followup.send("Choose a Character!",view=charmenu,delete_after=30)
      button3.callback = button_callback3
      buttons.add_item(button3)
      
      await self.inter.delete_original_response(delay=0)
      self.iteri = 2
    
      await self.inter.followup.send(f"<@!{self.did}>!\nThis will change you to **{self.values[0]}**. \nAfter you are changed to **{self.values[0]}** you will have to wait a week before you can change again. \n\nAre you sure you want to change to this character or would you like to return to the menu?",view=buttons,delete_after=20)
      print(datetime.datetime.now())

  class SelectView(disnake.ui.View):
      def __init__(self,did,charlists,guildv,inter,iteri,autolog,first,author,guilds):
          timeout = 180
          super().__init__(timeout=timeout)
          self.add_item(charlist.Select(did,charlists,guildv,inter,iteri,autolog,first,author,guilds))
  #async def start(self,did):
    #self.charlist, self.guildlist = await helpers.userd2(did)
    #self.did = self.did
    #view = self.SelectView()
    #return view
    


    #appears as a list ['Nemo','Ryler Moonshine','Emmanuel de Borel']
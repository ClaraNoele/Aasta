import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime

from helpers.reghelp.basichelpers import helpers

async def buttonset(did,name,inter,autolog,link):
  intertrue = inter
  view2 = disnake.ui.View()
  button1 = Button(style=disnake.ButtonStyle.success,label="This is Correct!",custom_id="yes")
  button2 = Button(style=disnake.ButtonStyle.danger,label="I Changed my Mind",custom_id="no")
  async def button_callback1(interaction):
    view2.stop()
    await intertrue.followup.send(f"Alright, let me get {name} squared away on our sheet! \nOne Moment...",delete_after=10)
    done = await helpers.register(name,link)
    if done == "Done":
      embed = disnake.Embed(
        title=f"**Registration Successful!**",
        description=f"Thank you,<@!{did}>!\nI have registered {name} into the system!\n\nYou may now use the /stats and /check commands without issue! **Hopefully**\n\nHave a nice day!",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Character Registered**",
        description=f"<@!{did}> registered their character, **{name}**!",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
    else:
      await intertrue.followup.send(f"**Interaction Failed**\nSomething went wrong!")
  async def button_callback2(interaction):
    view2.stop()
    embed = disnake.Embed(
      title=f"**Registration Canceled**",
      description=f"Alright <@!{did}>! \nYour character registration was **canceled**.\n\nIf you change your mind feel free to use this command again!",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    await intertrue.followup.send(embed=embed)
  button1.callback = button_callback1
  button2.callback = button_callback2

  view2.add_item(button1)
  view2.add_item(button2)
  return view2
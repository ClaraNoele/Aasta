import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime
from helpers.d2helpers.basichelpers import helpers

async def buttonset3(did,name,inter,autolog,author,choice,guilds):
  intertrue = inter
  view4 = disnake.ui.View()
  button1 = Button(style=disnake.ButtonStyle.success,label="Yes",custom_id="yes")
  button2 = Button(style=disnake.ButtonStyle.danger,label="No",custom_id="no")
  async def button_callback1(interaction):
    view4.stop()
    autochoice = "Ask"
    await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
    done1 = await helpers.change(did,name)
    done2, time= await helpers.timetrack(did,name,autochoice)
    done3 = await helpers.guild(name,author,guilds)
    if done1 and done2 and done3 == "Done":
      embed = disnake.Embed(
        title=f"**Change Successful!**",
        description=f"Thank you,<@!{did}>!\nYour guild will be changed automatically in both servers when you change your character. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Change Occurred**",
        description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
  async def button_callback2(interaction):
    view4.stop()
    autochoice = "Ask"
    await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
    done1 = await helpers.change(did,name)
    done2, time= await helpers.timetrack(did,name,autochoice)
    if done1 and done2 == "Done":
      embed = disnake.Embed(
        title=f"**Change Successful!**",
        description=f"Thank you,<@!{did}>!\nYour guild was not changed so please contact a Judicator if you wish to change your guild tags. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Change Occurred**",
        description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**\nTheir guild tags were **not** changed due to their response.",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
  button1.callback = button_callback1
  button2.callback = button_callback2

  view4.add_item(button1)
  view4.add_item(button2)
  return view4

async def buttonset2(did,name,inter,autolog,author,guilds):
  intertrue = inter
  view3 = disnake.ui.View()
  button1 = Button(style=disnake.ButtonStyle.success,label="Yes",custom_id="yes")
  button2 = Button(style=disnake.ButtonStyle.danger,label="Not Interested",custom_id="no")
  button3 = Button(style=disnake.ButtonStyle.primary,label="Ask Me",custom_id="ask")
  async def button_callback1(interaction):
    view3.stop()
    await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
    autochoice = 'Auto'
    done1 = await helpers.change(did,name)
    done2, time= await helpers.timetrack(did,name,autochoice)
    done3 = await helpers.guild(name,author,guilds)
    if done1 and done2 and done3 == "Done":
      embed = disnake.Embed(
        title=f"**Change Successful!**",
        description=f"Thank you,<@!{did}>!\nYour guild will be changed automatically in both servers when you change your character. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Change Occurred**",
        description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
  async def button_callback2(interaction):
    view3.stop()
    await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
    autochoice = "N/A"
    done1 = await helpers.change(did,name)
    done2, time= await helpers.timetrack(did,name,autochoice)
    if done1 and done2 == "Done":
      embed = disnake.Embed(
        title=f"**Change Successful!**",
        description=f"Thank you,<@!{did}>!\nYour guild was not changed so please contact a Judicator if you wish to change your guild tags and I will not change your guild from here on out! \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Change Occurred**",
        description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**\nTheir guild tags were **not** changed due to their response.",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
  async def button_callback3(interaction):
    view3.stop()
    await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
    autochoice = "Ask"
    done1 = await helpers.change(did,name)
    done2, time= await helpers.timetrack(did,name,autochoice)
    done3 = await helpers.guild(name,author,guilds)
    if done1 and done2 and done3 == "Done":
      embed = disnake.Embed(
        title=f"**Change Successful!**",
        description=f"Thank you,<@!{did}>!\nYou will be asked from here on out, but I changed your guild for you this time. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change!\n\nHave a nice day! Id:{time}",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await intertrue.followup.send(embed=embed)
      embed = disnake.Embed(
        title=f"**Change Occurred**",
        description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**",
        color=0x8d0d0d,
        timestamp=datetime.datetime.now())
      embed.set_footer(
        text="Aasta by Clara Noele",
        icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
      await autolog.send(embed=embed)
  button1.callback = button_callback1
  button2.callback = button_callback2
  button3.callback = button_callback3

  view3.add_item(button1)
  view3.add_item(button2)
  view3.add_item(button3)
  return view3


async def buttonset1(did,name,inter,autolog,first,author,guilds):
  intertrue = inter
  view2 = disnake.ui.View()
  button1 = Button(style=disnake.ButtonStyle.success,label="I'm Sure",custom_id="yes")
  button2 = Button(style=disnake.ButtonStyle.danger,label="Not Right Now",custom_id="no")
  async def button_callback1(interaction):
    view2.stop()
    if first == "first":
      view3 = await buttonset2(did,name,inter,autolog,author,guilds)
      await intertrue.followup.send(f"Would you, <@!{did}>, like to have me automatically change your guild roles? \n\n**Warning**: Your choice is **permanent** and will be kept track of! So if you select **Not Interested** your roles will not be changed and you will not have this option available.\n\nThough if you would like to change this please ask, <@!539623070202069023>.",view=view3,delete_after=20)
    elif first == "normal":
      await intertrue.followup.send(f"Give me a couple seconds... Please **do not** touch anymore buttons whilst I do this! \nIn the meantime, have you tried my /register command? It gives you access to some cool commands to help you with RP!",delete_after=10)
      sheet = client.open('Timesheet').sheet1
      dfind = sheet.find(did,in_column=1)
      row = dfind.row
      autochoice = sheet.cell(row,3).value
      if autochoice == "Auto":
        done1 = await helpers.change(did,name)
        done2, time= await helpers.timetrack(did,name,autochoice)
        done3 = await helpers.guild(name,author,guilds)
        if done1 and done2 and done3 == "Done":
          embed = disnake.Embed(
            title=f"**Change Successful!**",
            description=f"Thank you,<@!{did}>! \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
            color=0x8d0d0d,
            timestamp=datetime.datetime.now())
          embed.set_footer(
            text="Aasta by Clara Noele",
            icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
          await inter.followup.send(embed=embed)
          embed = disnake.Embed(
            title=f"**Change Occurred**",
            description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**",
            color=0x8d0d0d,
            timestamp=datetime.datetime.now())
          embed.set_footer(
            text="Aasta by Clara Noele",
            icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
          await autolog.send(embed=embed)
      elif autochoice == "N/A":
        done1 = await helpers.change(did,name)
        done2, time = await helpers.timetrack(did,name,autochoice)
        if done1 and done2 == "Done":
          embed = disnake.Embed(
            title=f"**Change Successful!**",
            description=f"Thank you,<@!{did}>! \nYour character change to **{name}** was successful! You will be able to change again in one week.\nThis did not include your guild role change!\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id: {time}",
            color=0x8d0d0d,
            timestamp=datetime.datetime.now())
          embed.set_footer(
            text="Aasta by Clara Noele",
            icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
          await inter.followup.send(embed=embed)
          embed = disnake.Embed(
            title=f"**Change Occured**",
            description=f"<@!{did}> changed their character to **{name}**!\n\n**Id: {time}**",
            color=0x8d0d0d,
            timestamp=datetime.datetime.now())
          embed.set_footer(
            text="Aasta by Clara Noele",
            icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
          await autolog.send(embed=embed)
      elif autochoice == "Ask":
        view4 = await buttonset3(did,name,inter,autolog,author,autochoice,guilds)
        await inter.followup.send(f"So you asked me to ask you if you wanted to change your guild.\nSo... Would you like me to change your guild roles?",view=view4,delete_after=20)
      else:
        pass
  async def button_callback2(interaction):
    view2.stop()
    embed = disnake.Embed(
      title=f"**Change Canceled**",
      description=f"Alright <@!{did}>! \nYour character change was **canceled**.\n\nIf you change your mind feel free to use this command again!",
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
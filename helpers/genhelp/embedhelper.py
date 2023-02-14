import os
import disnake
from typing import Optional
from datetime import datetime

async def embedbuilder(title: str=None,desc: str=None, image=None, thumbnail=None, author: list=None, fieldlist: list=None):
  embed = disnake.Embed(
    title=title,
    description=desc,
    color=0x8d0d0d,
    timestamp=datetime.now())
  embed.set_footer(
    text="Aasta by Clara Noele",
    icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
  if image != None:
    if type(image) == str:
      embed.set_image(
        url=image
      )
    elif type(image) != str:
      embed.set_image(
        file=image
      )
    else:
      pass
  x=1
  if thumbnail != None:
    if type(thumbnail) == str:
      embed.set_thumbnail(
        url=thumbnail
      )
    elif type(thumbnail) != str:
      embed.set_thumbnail(
        file=thumbnail
      )
    else:
      pass
  x=2
  if author != None:
    embed.set_author(
      name = author[0],
      url = author[1])
  x=3
  if fieldlist != None:
    for field in range(len(fieldlist)):
      embed.add_field(
        name = fieldlist[field][0],
        value = fieldlist[field][1],
        inline = fieldlist[field][2]
      )
  x=0
  return embed
import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime



class helpers():
  async def registercheck(did):
    libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
    cellst = libsheet.findall(did,in_column=45)
    charlist = []
    guildv = []
    if cellst == [] or None:
      return '638'
    for each in cellst:
      rowvalue = each.row
      retired = libsheet.cell(rowvalue,43).value
      if retired == 'FALSE':
        empty = libsheet.cell(rowvalue,49).value
        if empty == None:
          name = libsheet.cell(rowvalue,2).value
          guild = libsheet.cell(rowvalue,6).value
          guildv.append(guild)
          charlist.append(name)
        else:
          continue
      else:
        continue
    if charlist == []:
      return ("890","890")
    else:
      return (charlist, guildv)
  async def register(name,link):
    master = client.open('Master Favor Log  V2.5').get_worksheet(1)
    namecell = master.find(name,in_column=2)
    rownum = namecell.row
    master.update_cell(rownum,49,link)
    return "Done"
    


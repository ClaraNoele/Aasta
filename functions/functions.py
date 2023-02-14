import os
import disnake
from disnake import AllowedMentions
from disnake.ext import commands
from enum import Enum
import functions.important.client
from functions.important.client import client
import gspread
import d20
import asyncio



async def sheetlocale(did):
  libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
  cellst = libsheet.findall(did,in_column=45)
  if cellst == [] or None:
    Error638 = '638'
    return '638'
  for each in cellst:
    rowvalue = each.row
    val = libsheet.cell(rowvalue,42).value
    if val == 'TRUE':
      shtlink = libsheet.cell(rowvalue,49).value
      if shtlink == None:
        shtlink = '640'
        continue
      else:
        break
      break
    elif val == 'FALSE':
      shtlink = '639'
      continue
  return shtlink
#Searches for the active character and returns the sheet link

async def figureitout2(listoflists):
  i = 0
  for list in listoflists:
    if list[0] == 'Initiative':
      num = list[1]
      Initiative = num.replace('+','')
      continue
    if list[0] == 'Mental Acuity':
      num = list[1]
      MA = num.replace('+','')
      continue
    if list[0] == 'Push Through':
      num = list[1]
      PT = num.replace('+','')
      continue
    if list[0] == 'Quick Reflexes':
      num = list[1]
      QR = num.replace('+','')
      continue 
    if list[0] == 'Athletics (Body)':
      num = list[1]
      Athl = num.replace('+','')
      continue 
    if list[0] == 'Endurance (Body)':
      num = list[1]
      Endu = num.replace('+','')
      continue 
    if list[0] == 'Agility (Dex)':
      num = list[1]
      Agil = num.replace('+','')
      continue 
    if list[0] == 'Stealth (Dex)':
      num = list[1]
      Stea = num.replace('+','')
      continue 
    if list[0] == 'History (Mind)':
      num = list[1]
      Hist = num.replace('+','')
      continue 
    if list[0] == 'People (Mind)':
      num = list[1]
      Peop = num.replace('+','')
      continue 
    if list[0] == 'Tinkerer (Mind)':
      num = list[1]
      Tink = num.replace('+','')
      continue 
    if list[0] == 'Academics (Mind)':
      num = list[1]
      Acad = num.replace('+','')
      continue 
    if list[0] == 'Alchemy (Mind)':
      num = list[1]
      Alch = num.replace('+','')
      continue 
    if list[0] == 'Mysticism (Mind)':
      num = list[1]
      Myst = num.replace('+','')
      continue 
    if list[0] == 'Fieldcraft (Spirit)':
      num = list[1]
      Fiel = num.replace('+','')
      continue 
    if list[0] == 'Spirituality (Spirit)':
      num = list[1]
      Spir = num.replace('+','')
      continue 
    if list[0] == 'Animal Handling (Spirit)':
      num = list[1]
      Anim = num.replace('+','')
      continue 
    if list[0] == 'Non-magic Healing (Spirit)':
      num = list[1]
      NMH = num.replace('+','')
      continue 
    if list[0] == 'Riding (Spirit)':
      num = list[1]
      Ridi = num.replace('+','')
      continue 
    if list[0] == 'Performance (Cha)':
      num = list[1]
      Perf = num.replace('+','')
      continue 
    if list[0] == 'Persuasion (Cha)':
      num = list[1]
      Pers = num.replace('+','')
      continue 
    if list[0] == 'Intimidation (Cha)':
      num = list[1]
      Inti = num.replace('+','')
      continue 
    if list[0] == 'Deception (Cha)':
      num = list[1]
      Dece = num.replace('+','')
      continue 
    if list[0] == 'Observation (Perc)':
      num = list[1]
      Obse = num.replace('+','')
      continue
    if list[0] == 'Light Blades (Dex)':
      num = list[1]
      LB = num.replace('+','')
      continue 
    if list[0] == 'Heavy Blades (Body)':
      num = list[1]
      HB = num.replace('+','')
      continue 
    if list[0] == 'Polearms (Body, Dex)':
      num = list[1]
      Pole = num.replace('+','')
      continue 
    if list[0] == 'Unarmed (Body, Dex)':
      num = list[1]
      Unar = num.replace('+','')
      continue 
    if list[0] == 'Bows (Perc)':
      num = list[1]
      Bows = num.replace('+','')
      continue 
    if list[0] == 'Shields (Body)':
      num = list[1]
      Shie = num.replace('+','')
      continue 
    if list[0] == 'Bludgeons (Body)':
      num = list[1]
      Blud = num.replace('+','')
      continue 
    if list[0] == 'Firearms (Perc)':
      num = list[1]
      Firea = num.replace('+','')
      continue 
    if list[0] == 'Fire (Mind)':
      num = list[1]
      Fire = num.replace('+','')
      continue 
    if list[0] == 'Water (Mind)':
      num = list[1]
      Water = num.replace('+','')
      continue 
    if list[0] == 'Earth (Mind)':
      num = list[1]
      Earth = num.replace('+','')
      continue 
    if list[0] == 'Dark (Mind, Spirit)':
      num = list[1]
      Dark = num.replace('+','')
      continue 
    if list[0] == 'Light (Mind, Spirit)':
      num = list[1]
      Light = num.replace('+','')
      continue 
    if list[0] == 'Wind (Mind, Sprit)' or 'Wind (Mind, Spirit)':
      num = list[1]
      Wind = num.replace('+','')
      continue 
    
  return Initiative,MA,PT,QR,Athl,Endu,Agil,Stea,Hist,Peop,Tink,Acad,Alch,Myst,Fiel,Spir,Anim,NMH,Ridi,Perf,Pers,Inti,Dece,Obse,LB,HB,Pole,Unar,Bows,Shie,Blud,Firea,Fire,Water,Earth,Dark,Light,Wind
    
async def guild(did):
  libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
  cellst = libsheet.findall(did)
  if cellst == [] or None:
    Error638 = '638'
    return '638'
  for each in cellst:
    rowvalue = each.row
    val = libsheet.cell(rowvalue,42).value
    if val == 'TRUE':
      guildf = libsheet.cell(rowvalue,6).value
      break
    elif val == 'FALSE':
      guildf = '639'
      continue
  return guildf
  
#Fancy text functions to be added
  
  




import functions.functions
import os
from functions.functions import sheetlocale, figureitout2
from functions.important.client import client
import gspread
import asyncio

plcholder = os.environ['test_id']


class Stat_List:
  def __init__(self):
    return
  async def all(self,did):
    shtlink = await sheetlocale(did)
    if shtlink == '638':
      Error638 = '638'
      return Error638
    elif shtlink == '639':
      Error639 = '639'
      return Error639
    elif shtlink == '640':
      Error640 = '640'
      return Error640
    else:
      self.shtlink = shtlink
      pass
    sheet = client.open_by_url(shtlink).sheet1
    main = sheet.get('D3:D25')
    skco = sheet.get('F27:G64')
    info = sheet.get('F3:L11')
    ivalues = info[0][1],info[0][6],info[2][1],info[2][6],info[6][1],info[6][2],info[7][1],info[7][2],info[8][1],info[8][2]
    mvalues = main[1][0],main[5][0],main[9][0],main[13][0],main[17][0],main[21][0]
    values = await figureitout2(skco)
    final = mvalues + values + ivalues
    return final
    
  async def atr(self,stat,did,shtlink):
    self.did = did
    stats = ','.join(stat)
    if shtlink == 'None':
      self.shtlink = await sheetlocale(self.did)
      pass
    elif shtlink == '638':
      Error638 = '638'
      return Error638
    elif shtlink == '639':
      Error639 = '639'
      return Error639
    elif shtlink == '640':
      Error640 = '640'
      return Error640
    else:
      self.shtlink = shtlink
      pass
    self.sheet = client.open_by_url(self.shtlink).sheet1
    default = 'Unavailable'
    return await getattr(self,'atr_' + str(stats), lambda: default)()
  
  async def atr_NameLvl(self):
    nmlvl = self.sheet.get('G3:L3')
    nmlvlval = nmlvl[0][0],nmlvl[0][5]
    return (*nmlvlval, self.shtlink)

  async def atr_Money(self):
    return self.sheet.cell(5,12).value

  async def atr_Race(self):
    return self.sheet.cell(5,7).value

  async def atr_HP(self):
    return self.sheet.cell(9,8).value

  async def atr_CHP(self):
    return self.sheet.cell(9,7).value

  async def atr_Mana(self):
    return self.sheet.cell(11,8).value

  async def atr_CMana(self):
    return self.sheet.cell(11,7).value

  async def atr_Body(self):
    return self.sheet.cell(4,4).value

  async def atr_Dexterity(self):
    return self.sheet.cell(8,4).value

  async def atr_Perception(self):
    return self.sheet.cell(12,4).value

  async def atr_Mind(self):
    return self.sheet.cell(16,4).value

  async def atr_Spirit(self):
    return self.sheet.cell(20,4).value

  async def atr_Charisma(self):
    return self.sheet.cell(24,2).value

  async def atr_Initiative(self):
    return self.sheet.cell(27,7).value

  async def atr_Mental_Acuity(self):
    return self.sheet.cell(28,7).value

  async def atr_Push_Through(self):
    return self.sheet.cell(29,7).value

  async def atr_Quick_Reflexes(self):
    return self.sheet.cell(30,7).value

  async def atr_Athletics(self):
    Loc = self.sheet.find("Athletics (Body)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Endurance(self):
    Loc = self.sheet.find("Endurance (Body)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Agility(self):
    Loc = self.sheet.find("Agility (Dex)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Stealth(self):
    Loc = self.sheet.find("Stealth (Dex)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_History(self):
    Loc = self.sheet.find("History (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_People(self):
    Loc = self.sheet.find("People (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Tinkerer(self):
    Loc = self.sheet.find("Tinkerer (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Academics(self):
    Loc = self.sheet.find("Academics (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Alchemy(self):
    Loc = self.sheet.find("Alchemy (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Mysticism(self):
    Loc = self.sheet.find("Mysticism (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Fieldcraft(self):
    Loc = self.sheet.find("Fieldcraft (Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Spirituality(self):
    Loc = self.sheet.find("Spirituality (Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Animal_Handling(self):
    Loc = self.sheet.find("Animal Handling (Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Non_Magical_Healing(self):
    Loc = self.sheet.find("Non-magic Healing (Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Riding(self):
    Loc = self.sheet.find("Riding (Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Performance(self):
    Loc = self.sheet.find("Performance (Cha)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Persuasion(self):
    Loc = self.sheet.find("Persuasion (Cha)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Intimidation(self):
    Loc = self.sheet.find("Intimidation (Cha)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Deception(self):
    Loc = self.sheet.find("Deception (Cha)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Observation(self):
    Loc = self.sheet.find("Observation (Perc)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Light_Blades(self):
    Loc = self.sheet.find("Light Blades (Dex)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Heavy_Blades(self):
    Loc = self.sheet.find("Heavy Blades (Body)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Polearms(self):
    Loc = self.sheet.find("Polearms (Body, Dex)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Unarmed(self):
    Loc = self.sheet.find("Unarmed (Body, Dex)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Bows(self):
    Loc = self.sheet.find("Bows (Perc)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Shields(self):
    Loc = self.sheet.find("Shields (Body)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Bludgeons(self):
    Loc = self.sheet.find("Bludgeons (Body)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Firearms(self):
    Loc = self.sheet.find("Firearms (Perc)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Fire(self):
    Loc = self.sheet.find("Fire (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Water(self):
    Loc = self.sheet.find("Water (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Earth(self):
    Loc = self.sheet.find("Earth (Mind)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Dark(self):
    Loc = self.sheet.find("Dark (Mind, Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Light(self):
    Loc = self.sheet.find("Light (Mind, Spirit)")
    Row = Loc.row
    return self.sheet.cell(Row,7).value

  async def atr_Wind(self):
    Loc2 = self.sheet.find("Wind (Mind, Spirit)")
    Loc = self.sheet.find("Wind (Mind, Sprit)")
    if Loc2 != None:
      Row = Loc2.row
    elif Loc != None:
      Row = Loc.row
    return self.sheet.cell(Row,7).value
    

	

#async async def statfind(id,atr):
  #self.sheet = self.sheetlocale(id)
  #Secondary Information
  #Character_Name = self.sheet.cell(3,7).value
  #Character_Level = self.sheet.cell(3,12).value
  #Character_Race = self.sheet.cell(5,7).value
  #Main stats locations
  #Body = self.sheet.cell(4,4).value
  #Dexterity = self.sheet.cell(8,4).value
  #Perception = self.sheet.cell(12,4).value
  #Mind = self.sheet.cell(16,4).value
  #Spirit = self.sheet.cell(20,4).value
  #Charisma = self.sheet.cell(24,4).value
  #Secondary stats locations
  #Initiative = self.sheet.cell(27,7).value
  #Mental_Acuity = self.sheet.cell(28,7).value
  #Push_Through = self.sheet.cell(29,7).value
  #Quick_Reflexes = self.sheet.cell(30,7).value
  #Athletics = self.sheet.cell(31,7).value
  #Endurance = self.sheet.cell(32,7).value
  #Agility = self.sheet.cell(33,7).value
  #Stealth = self.sheet.cell(34,7).value
  #History = self.sheet.cell(35,7).value
  #People = self.sheet.cell(36,7).value
  #Tinkerer = self.sheet.cell(37,7).value
  #Academics = self.sheet.cell(38,7).value
  #Alchemy = self.sheet.cell(39,7).value
  #Mysticism = self.sheet.cell(40,7).value
  #Fieldcraft = self.sheet.cell(41,7).value
  #Spirituality = self.sheet.cell(42,7).value
  #Animal_Handling = self.sheet.cell(43,7).value
  #Non_Magic_Healing = self.sheet.cell(44,7).value 
  #Riding = self.sheet.cell(45,7).value
  #Performance = self.sheet.cell(46,7).value
  #Persuasion = self.sheet.cell(47,7).value
  #Intimidation = self.sheet.cell(48,7).value
  #Deception = self.sheet.cell(49,7).value
  #Light_Blades = self.sheet.cell(50,7).value
  #Heavy_Blades = self.sheet.cell(51,7).value
  #Polearms = self.sheet.cell(52,7).value
  #Unarmed = self.sheet.cell(53,7).value
  #Bows = self.sheet.cell(54,7).value
  #Shields = self.sheet.cell(55,7).value
  #Bludgeons = self.sheet.cell(56,7).value
  #Firearms = self.sheet.cell(57,7).value
  #Fire = self.sheet.cell(58,7).value
  #Water = self.sheet.cell(59,7).value
  #Earth = self.sheet.cell(60,7).value
  #Dark = self.sheet.cell(61,7).value
  #Light = self.sheet.cell(62,7).value
  #Wind = self.sheet.cell(63,7).value
  #return atr
#print('| Body =',Body,'| Dexterity =',Dexterity,'| Perception =',Perception,'| Mind =',Mind,'| Spirit =',Spirit,'| Charisma =',Charisma,'|')

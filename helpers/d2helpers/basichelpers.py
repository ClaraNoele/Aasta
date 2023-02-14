import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime
import functions.log as log
import pytz

timezone = pytz.timezone('America/Denver')
groles = {
  'Hallowed Vanguard':565128126804393992,
  'Neverdawn Network':565128188565651458,
  'The Oathbreakers':878401513049952326,
  'Steadfast':632269085610082305,
  'Scarlet Feast':949072147345723492,
  'Order of the Morning':945550823159652414
}
grole2 = {
  'Hallowed Vanguard':561613312656408617,
  'Neverdawn Network':561613486820425738,
  'The Oathbreakers':878409277822357505,
  'Steadfast':632269420777177088,
  'Scarlet Feast':1009646010399719526,
  'Order of the Morning':945562396569772042
}
rolelist = [565128126804393992,565128188565651458,878401513049952326,632269085610082305,949072147345723492,945550823159652414]
rolelist2 = [561613312656408617,561613486820425738,878409277822357505,632269420777177088,1009646010399719526,945562396569772042]

class helpers:
  async def userd2(did):
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
        active = libsheet.cell(rowvalue,42).value
        if active == 'FALSE':
          name = libsheet.cell(rowvalue,2).value
          guild = libsheet.cell(rowvalue,6).value
          guildv.append(guild)
          charlist.append(name)
        else:
          continue
      else:
        continue
    if charlist == []:
      return ("780","780")
    else:
      return (charlist, guildv)
  async def change(did,name):
    try:
      libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
      celltt = libsheet.findall(did,in_column=45)
      for each in celltt:
        rowvalue = each.row
        active = libsheet.cell(rowvalue,42).value
        if active == 'TRUE':
          libsheet.update_cell(rowvalue,42,False)
          continue
        else:
          continue
      cellst = libsheet.find(name,in_column=2)
      rwv = cellst.row
      libsheet.update_cell(rwv,42,True)
      return "Done"
    except Exception as e:
      await log.errorlog(e,None)
      return ("Error")
  async def valid(did):
    try:
      sheet = client.open('Timesheet').sheet1
      timenow = datetime.datetime.today().replace(microsecond=0)
      epoch = datetime.datetime(1970,1,1)
      delta = (timenow-epoch)
      delsec = delta.total_seconds()
      didfinal = sheet.find(did,in_column=1)
      if didfinal == None:
        return ("valid","first")
      else:
        row = didfinal.row
        timet = sheet.cell(row,2).value
        timethen = datetime.datetime.fromtimestamp(int(timet))
        delta2 = (timethen-epoch)
        delsec2 = delta2.total_seconds()
        diff = (delsec-delsec2)
      
        if diff >= 604800:
          return ("valid","normal")
        elif diff <= 604800:
          timediff = (604800-diff)
          seconds = timediff % (12 * 4 * 7 * 24 * 3600)
          days = seconds // 86400
          seconds %= 86400
          hour = seconds // 3600
          seconds %= 3600
          minutes = seconds // 60
          seconds %= 60
      
          time = "%d day(s), %02d hour(s), %02d minute(s)," % (days, hour, minutes)
          return ("invalid",time)
    except Exception as e:
      await log.errorlog(e,None)
      return ("Error","Error")
  async def guild(name,author,servers):
    hub = servers[0]
    realms = servers[1]
    member = servers[2]
    try:
      libsheet = client.open('Master Favor Log  V2.5').get_worksheet(1)
      cellst = libsheet.find(name,in_column=2)
      row = cellst.row
      guild = libsheet.cell(row,6).value
      for role in rolelist:
        roleobj = hub.get_role(role)
        await author.remove_roles(roleobj)
      for role in rolelist2:
        roleob = realms.get_role(role)
        await member.remove_roles(roleob)
      if guild != "Guildless":
        id = groles[guild]
        roleb = hub.get_role(id)
        id2 = grole2[guild]
        roleb2 = realms.get_role(id2)
        await author.add_roles(roleb)
        await member.add_roles(roleb2)
        return "Done"
      else:
        return "Done"
    except Exception as e:
      await log.errorlog(e,None)
      return ("Error")
  async def timetrack(did,name,choice):
    try:
      sheet = client.open('Timesheet').sheet1
      didfinal = sheet.find(did,in_column=1)
      if didfinal == None:
        rownum = len(sheet.get_all_values()) + 1
      else:
        rownum = didfinal.row
      timenow = datetime.datetime.today().replace(microsecond=0)
      humantime = datetime.datetime.now(timezone).strftime('%m\%d\%Y %H:%M')
      epoch = datetime.datetime(1970,1,1)
      delta = (timenow-epoch)
      delsec = delta.total_seconds()
      sheet.update(f"A{rownum}:E{rownum}",[[did,delsec,choice,name,humantime]])
      return ("Done",delsec)
    except Exception as e:
      await log.errorlog(e,None)
      return ("Error","Error")
  async def updatetime(did,timechange):
    try:
      sheet = client.open('Timesheet').sheet1
      didfinal = sheet.find(did,in_column=1)
      if didfinal == None:
        return ("Failure")
      else:
        rownum = didfinal.row
      if timechange == 'today':
        time = datetime.datetime.today().replace(microsecond=0)
      else:
        time = datetime.datetime.strptime(f"{timechange} 00:00",'%m/%d/%Y %H:%M')
      list = sheet.row_values(rownum)
      epoch = datetime.datetime(1970,1,1)
      delta = (time-epoch)
      delsec = delta.total_seconds()
      list[1] = delsec
      list[4] = timechange
      sheet.update(f"A{rownum}:E{rownum}",[list])
      return ("Done")
    except Exception as e:
      await log.errorlog(e,None)
      return ("Error")
      
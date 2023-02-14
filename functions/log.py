import logging
import datetime, pytz
import os

files = []

time = datetime.datetime.now(pytz.timezone('America/Denver')).strftime('%m\%d\%Y %H:%M')

logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
consoleFormatter = logging.Formatter("[%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(f"databases/logs/log-{time}.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(consoleFormatter)
rootLogger.addHandler(consoleHandler)

def filemanage():
  for file in os.listdir(r'/home/runner/Aasta/databases/logs'):
    if file.endswith(".log"):
      filepath = os.path.join(r'/home/runner/Aasta/databases/logs', file)
      files.append(filepath)
    else:
      continue
  if len(files) > 12:
    length = int(len(files)) - 13
    if length == 0:
      path = files[0]
      os.remove(path)
    else:
      for i in range(0,length):
        path = files[i]
        os.remove(path)
  else:
    pass

async def errorlog(error,args):
  file = open(f"databases/logs/log-{time}.log","a")
  errortime = datetime.datetime.now(pytz.timezone('America/Denver')).strftime('%m\%d\%Y %H:%M')
  print(f"An Error Occured at {errortime}: \n{error}\n{args}")
  file.write(f"An Error Occured at {errortime}: \n{error}\n{args}\n")
  file.close()
async def printing(statement):
  file = open(f"databases/logs/log-{time}.log","a")
  errortime = datetime.datetime.now(pytz.timezone('America/Denver')).strftime('%m\%d\%Y %H:%M')
  print(statement)
  file.write(f"Printed a statement at {errortime}: {statement}\n")
  file.close()
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Aasta is runnning!"

def run():
  app.run(host="0.0.0.0", port=6666)

def keep_alive():
  server = Thread(target=run)
  server.start()

class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if self.a > 9:
      self.a = 0
    return x

class KillNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    if self.a > 9:
      self.a = 0
    return x

myclass = MyNumbers()
myiter = iter(myclass)
myclass2 = KillNumbers()
killiter = iter(myclass2)

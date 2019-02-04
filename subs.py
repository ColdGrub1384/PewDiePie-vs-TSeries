

# sub to pewdiepie
from sys import argv
import urllib.request
import json
from console import clear
from time import sleep
import ssl

context = ssl._create_unverified_context()

def main():
  pewdiepie = "pewdiepie"
  key = "AIzaSyDOi4pJwTjAQw4xQ3G0CAH_zpht6-ajVkQ"

  data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+pewdiepie+"&key="+key, context=context).read()
  subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

  data2 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+"tseries"+"&key="+key, context=context).read()
  subs2 = json.loads(data2)["items"][0]["statistics"]["subscriberCount"]

  clear()

  if int(subs) < int(subs2):
    print("YouTube is dead")

  print("PewDiePie" + " has " + "{:,d}".format(int(subs)) + " subscribers!")
  print("T-Series" + " has " + "{:,d}".format(int(subs2)) + " subscribers!")

if "__main__" == __name__:
  if "T-Gay" in argv:
    print("Subscribe to PewDiePie.")
    print("Unsubscribe from T-Series")
  
  while True:
    main()
    sleep(0.1)

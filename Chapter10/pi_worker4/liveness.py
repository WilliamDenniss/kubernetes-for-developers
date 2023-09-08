import os
import time

def update_liveness():

  timestamp = int(time.time())  
  with open("logs/lastrun.date", "w") as myfile:
    myfile.write(f"{timestamp}")

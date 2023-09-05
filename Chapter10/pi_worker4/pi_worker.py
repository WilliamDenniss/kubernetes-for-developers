import os
import signal
import redis
from pi import *
from liveness import *

redis_host = os.environ.get('REDIS_HOST')
assert redis_host != None
r = redis.Redis(host=redis_host,
                port='6379',
                decode_responses=True)
running = True

def signal_handler(signum, frame):
    print("got signal")
    running = False

signal.signal(signal.SIGTERM, signal_handler)

print("starting")
while running:
  update_liveness()
  task = r.blpop('queue:task', 5)
  if task != None:
    iterations = int(task[1])
    print("got task: " + str(iterations))
    pi = leibniz_pi(iterations)
    print (pi)
  else:
    if os.getenv('COMPLETE_WHEN_EMPTY', '0') != '0':
      print ("no more work")
      running = False

exit(0)

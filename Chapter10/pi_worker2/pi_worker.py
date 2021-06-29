import os
import signal
import redis
from pi import *

redis_host = os.environ.get('REDIS_HOST')
assert redis_host != None
r = redis.Redis(host=redis_host, port= '6379', decode_responses=True)

running = True

def signal_handler(signum, frame):
    print("got signal")
    running = False

signal.signal(signal.SIGTERM, signal_handler)

print("starting")
while running:
  job = r.blpop('queue:job', 5)
  if job != None:
    iterations = int(job[1])
    print("got job: " + str(iterations))
    pi = leibniz_pi(iterations)
    print (pi)

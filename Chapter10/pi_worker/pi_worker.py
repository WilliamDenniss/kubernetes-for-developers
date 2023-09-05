import os
import redis
from pi import *

redis_host = os.environ.get('REDIS_HOST')
assert redis_host != None
r = redis.Redis(host=redis_host,
                port='6379',
                decode_responses=True)

print("starting")
while True:
  task = r.blpop('queue:task')
  iterations = int(task[1])
  print("got task: " + str(iterations))
  pi = leibniz_pi(iterations)
  print (pi)

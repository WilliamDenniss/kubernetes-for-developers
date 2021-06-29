import os
import redis
from pi import *

redis_host = os.environ.get('REDIS_HOST')
assert redis_host != None
r = redis.Redis(host=redis_host, port='6379', decode_responses=True)

print("starting")
while True:
  job = r.blpop('queue:job')
  iterations = int(job[1])
  print("got job: " + str(iterations))
  pi = leibniz_pi(iterations)
  print (pi)

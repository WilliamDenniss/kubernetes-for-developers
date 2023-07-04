import os
import redis
import random

redis_host = os.environ.get('REDIS_HOST')
assert redis_host != None
r = redis.Redis(host=redis_host,
                port='6379',
                decode_responses=True)

random.seed()
for i in range(0, 10):
  rand = random.randint(10,100)
  iterations = rand * 100000
  r.rpush('queue:task', iterations)
  print("added task: " + str(iterations))

print("queue depth", str(r.llen('queue:task')))
print ("done")

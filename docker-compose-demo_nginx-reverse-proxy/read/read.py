#! /user/bin/env python 

from flask import Flask
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route("/")
def read():
  timestamp = r.get('timestamp')

  if timestamp:
    return timestamp.decode("UTF-8")
  return None 
  
if __name__ == "__main__":
  app.run(host='0.0.0.0')
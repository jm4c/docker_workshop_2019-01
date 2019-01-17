#! /user/bin/env python

from flask import Flask
import redis
import datetime

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route("/")
def write():
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (r.set('timestamp', dt)):
        return str('Wrote ' + str(dt) + ' to redis.')
    return str('Failed to write to redis.')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
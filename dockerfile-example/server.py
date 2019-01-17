#! /user/bin/env python 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def read():
  return "This is a Dockerfile Demo" 
  
if __name__ == "__main__":
  app.run(host='0.0.0.0')
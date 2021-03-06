import os
import signal
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from api import generator

app = Flask(__name__)
api = Api(app)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default


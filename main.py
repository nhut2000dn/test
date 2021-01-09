from predict import response
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "<h1>Welcome to CodingX</h1>"

if __name__ == '__main__':
     app.run()

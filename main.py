from predict import response
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

# class Employees(Resource):
#     def get(self, text):
#         return response(text)

@app.route('/')
def index():
    return "<h1>Welcome to CodingX</h1>"

# api.add_resource(Employees, '/send/<text>') 

if __name__ == '__main__':
     app.run()

#!/usr/bin/env python
# _*_ coding: utf8 _*_

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {"Hello":"world"}

api.add_resource(Hello, '/hello')

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask
from flask import request
from flask_restful import Api, Resource
from datetime import datetime
from enum import Enum
import uuid

app = Flask(__name__)
api = Api(app)



class ProvenirHardPolicy(Resource):

    def post(self):
        # Reading data from the payload(should come as json)
        return "HP"


class ProvenirCreditPolicy(Resource):
    def post(self):
        from test1 import printTime
        return printTime()


api.add_resource(ProvenirHardPolicy, '/hp')
api.add_resource(ProvenirCreditPolicy, '/cp')

if __name__ == '__main__':
    app.run(port='5001')

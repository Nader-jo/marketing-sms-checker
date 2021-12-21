#!/usr/bin/env python
"""main.py: this is an api that checks your marketing sms."""
from flask import Flask
from flask_restful import Api, Resource, reqparse

from checker_logic import checker_logic

APP = Flask(__name__)
API = Api(APP)

ARGS = reqparse.RequestParser()
ARGS.add_argument("sms", type=str, help="sms message is required", required=True)

class Data(Resource):
    """data"""
    cmnt = ""
    def get(self):
        """get"""
        self.cmnt = "cmnt"
        json_data = ARGS.parse_args()
        if len(json_data["sms"]) == 0:
            return {"error": "sms is empty"}
        return checker_logic(json_data["sms"])

API.add_resource(Data, "/sms-checker")

if __name__ == "__main__":
    APP.run(debug=True)

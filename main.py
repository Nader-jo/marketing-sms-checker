from flask import Flask
from flask_restful import Api, Resource, reqparse

from checker_logic import checker_logic

app = Flask(__name__)
api = Api(app)

args = reqparse.RequestParser()
args.add_argument("sms", type=str, help="sms message is required", required=True)

class data(Resource):
    def get(self):
        json_data = args.parse_args()
        if len(json_data["sms"]) == 0:
            return {"error": "sms is empty"}
        return checker_logic(json_data["sms"])

api.add_resource(data, "/sms-checker/")

if __name__ == "__main__":
    app.run(debug=True)

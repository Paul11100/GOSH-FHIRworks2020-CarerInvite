from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Patients(Resource):
    def get(self):
        result = {"hello" : "world", "bye": "bruh"}
        return jsonify(result)

api.add_resource(Patients, '/patients')

if __name__ == '__main__':
     app.run(port='5002')


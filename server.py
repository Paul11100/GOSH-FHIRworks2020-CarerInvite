from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from main import Main

app = Flask(__name__)
api = Api(app)

class Patients(Resource):
    def get(self):
        main = Main()
        limit = int(request.args.get("limit"))
        print(limit)
        result = main.print_patients_in_range(limit, 55, 65, "Paul", "UCL-FHIR-Hack", "appdownload.com")
        # result = {"hello" : "world", "bye": "bruh"}
        return jsonify(result)

api.add_resource(Patients, '/patients') #Route 1

if __name__ == '__main__':
     app.run(port='5002')


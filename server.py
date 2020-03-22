from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from main import Main

app = Flask(__name__)
api = Api(app)

class Patients(Resource):
    def get(self):
        main = Main()
        limit = int(request.args.get("limit"))
        lower = int(request.args.get("lower"))
        upper = int(request.args.get("upper"))
        sender_name = request.args.get("name")
        sender_ref = request.args.get("ref")
        app_url = request.args.get("url")
        result = main.print_patients_in_range(limit, lower, upper, sender_name, sender_ref, app_url)
        return jsonify(result)

api.add_resource(Patients, '/patients') #Route 1

if __name__ == '__main__':
     app.run(port='5002')

# Sample Request: http://127.0.0.1:5002/patients?limit=5&lower=55&upper=65&name=paul&ref=UCL-FHIR-Hack&url=appdownload.com
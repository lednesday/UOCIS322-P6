# Streaming Service

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from db_methods import Db
import json

app = Flask(__name__)
api = Api(app)

# make a JSON element to return
db = Db()


class ListAll(Resource):
    def get(self, dtype="json"):
        data_list = list(db.find_content(
            projection={"open_time": 1, "close_time": 1, "_id": 0}))
        num_lines = request.args.get('top', -1, type=int)
        if num_lines < 0 or num_lines > len(data_list):
            num_lines = len(data_list)
        data_list = data_list[:num_lines]
        if dtype == "json":
            return jsonify(data_list)
        elif dtype == "csv":
            csv_string = ", ".join(list(data_list[0].keys())) + '\n'
            for datum in data_list:
                csv_string += ", ".join(list(datum.values())) + '\n'
            return csv_string
        else:
            return "something went wrong with the API"


class ListOpenOnly(Resource):
    def get(self, dtype="json"):
        data_list = list(db.find_content(
            projection={"open_time": 1, "_id": 0}))
        num_lines = request.args.get('top', -1, type=int)
        if num_lines < 0 or num_lines > len(data_list):
            num_lines = len(data_list)
        data_list = data_list[:num_lines]
        if dtype == "json":
            return jsonify(data_list)
        elif dtype == "csv":
            csv_string = ", ".join(list(data_list[0].keys())) + '\n'
            for datum in data_list:
                csv_string += ", ".join(list(datum.values())) + '\n'
            return csv_string
        else:
            return "something went wrong with the API"


class ListCloseOnly(Resource):
    def get(self, dtype="json"):
        data_list = list(db.find_content(
            projection={"close_time": 1, "_id": 0}))
        num_lines = request.args.get('top', -1, type=int)
        if num_lines < 0 or num_lines > len(data_list):
            num_lines = len(data_list)
        data_list = data_list[:num_lines]
        if dtype == "json":
            return jsonify(data_list)
        elif dtype == "csv":
            csv_string = ", ".join(list(data_list[0].keys())) + '\n'
            for datum in data_list:
                csv_string += ", ".join(list(datum.values())) + '\n'
            return csv_string
        else:
            return "something went wrong with the API"


# Create routes
# Another way, without decorators
api.add_resource(ListAll, '/listAll', '/listAll/<dtype>')
api.add_resource(ListOpenOnly, '/listOpenOnly', '/listOpenOnly/<dtype>')
api.add_resource(ListCloseOnly, '/listCloseOnly', '/listCloseOnly/<dtype>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Streaming Service

from flask import Flask, jsonify
from flask_restful import Resource, Api
from db_methods import Db
import json

app = Flask(__name__)
api = Api(app)

# make a JSON element to return
db = Db()


class ListAll(Resource):
    def get(self, dtype="json"):
        if dtype == "json":
            return jsonify(list(db.find_content({"open_time": 1, "close_time": 1, "_id": 0})))
        elif dtype == "csv":
            data_list = db.find_content(
                list({"open_time": 1, "close_time": 1, "_id": 0}))
            csv_string = str(data_list[0].keys()) + '\n'
            for datum in data_list:
                csv_string += str(time_pair.values()) + '\n'
            prinf("csv_string: ", csv_string)
            return csv_string
        else:
            return "something went wrong with the API"


class ListOpenOnly(Resource):
    def get(self, dtype="json"):
        if dtype == "json":
            return jsonify(list(db.find_content({"open_time": 1, "_id": 0})))
        elif dtype == "csv":
            data_list = db.find_content(
                list({"open_time": 1, "_id": 0}))
            csv_string = str(data_list[0].keys()) + '\n'
            for datum in data_list:
                csv_string += str(time_pair.values()) + '\n'
            prinf("csv_string: ", csv_string)
            return csv_string
        else:
            return "something went wrong with the API"


class ListCloseOnly(Resource):
    def get(self, dtype="json"):
        if dtype == "json":
            return jsonify(list(db.find_content({"close_time": 1, "_id": 0})))
        elif dtype == "csv":
            data_list = db.find_content(
                list({"close_time": 1, "_id": 0}))
            csv_string = str(data_list[0].keys()) + '\n'
            for datum in data_list:
                csv_string += str(time_pair.values()) + '\n'
            prinf("csv_string: ", csv_string)
            return csv_string
        else:
            return "something went wrong with the API"


# Create routes
# Another way, without decorators
api.add_resource(ListAll, '/listAll', '/listAll/<dtype>')
api.add_resource(ListOpenOnly, '/listOpenOnly', '/listOpenOnly/<dtype>')
api.add_resource(ListCloseOnly, '/listCloseOnly', '/listClose/Only/<dtype>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

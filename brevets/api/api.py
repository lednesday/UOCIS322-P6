# Streaming Service

from flask import Flask
from flask_restful import Resource, Api
from db_methods import Db
import json

app = Flask(__name__)
api = Api(app)

# make a JSON element to return
db = Db()

""" ----- JSON ----- """


class ListAll(Resource):
    def get(self):
        return jsonify(db.find_content({open_time: 1, close_time: 1, _id: 0}))


class ListOpenOnly(Resource):
    def get(self):
        return jsonify(db.find_content({open_time: 1, _id: 0}))


class ListCloseOnly(Resource):
    def get(self):
        return jsonify(db.find_content({close_time: 1, _id: 0}))


""" ----- CSV ----- """


class ListAllCSV(Resource):
    def get(self):
        json_data = db.find_content(
            jsonify({open_time: 1, close_time: 1, _id: 0}))
        json_parsed = json.loads(json_data)
        csv_string = ""
        header = 0
        for (key, value) in json_parsed.items():
            if header == 0:
                csv_string += json_parsed

        with open('/tmp/AllTimes.csv', 'w', newline='') as fp:
            csvwriter = csv.writer(fp)
            count = 0
            for time_pair in time_pairs:
                if count == 0:
                    header = time_pair.keys()
                    csvwriter.writerow(header)
                    count += 1
                csvwriter.writerow(time_pair.values())
        return csv_string


class ListOpenOnlyCSV(Resource):
    def get(self):
        json_data = db.find_content(jsonify({open_time: 1, _id: 0}))
        json_parsed = json.loads(json_data)


class ListCloseOnlyCSV(Resource):
    def get(self):
        json_data = db.find_content(jsonify({close_time: 1, _id: 0}))
        json_parsed = json.loads(json_data)


# Create routes
# Another way, without decorators
api.add_resource(ListAll, '/listAll')
api.add_resource(ListOpenOnly, '/listOpenOnly')
api.add_resource(ListCloseOnly, '/listCloseOnly')
api.add_resource(ListAll, '/listAll/json')
api.add_resource(ListOpenOnly, '/listOpenOnly/json')
api.add_resource(ListCloseOnly, '/listCloseOnly/json')

api.add_resource(ListAllCSV, '/listAll/csv')
api.add_resource(ListOpenOnlyCSV, '/listOpenOnly/csv')
api.add_resource(ListCloseOnlyCSV, '/listCloseOnly/csv')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

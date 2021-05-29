# Streaming Service

from flask import Flask
from flask_restful import Resource, Api
from db_methods import Db

app = Flask(__name__)
api = Api(app)

# make a JSON element to return
db = Db()


class ListAll(Resource):
    def get(self):
        return db.find_content()


class ListOpenOnly(Resource):
    def get(self):
        return db.find_content({open_time: 1, _id: 0})


class ListCloseOnly(Resource):
    def get(self):
        return db.find_content({close_time: 1, _id: 0})


# Create routes
# Another way, without decorators
api.add_resource(ListAll, '/listAll')
api.add_resource(ListOpenOnly, '/listOpenOnly')
api.add_resource(ListCloseOnly, '/listCloseOnly')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask_restful import Resource
from repository.data import Data


class List(Resource):
    def get(self):
        return Data.get_list(), 200

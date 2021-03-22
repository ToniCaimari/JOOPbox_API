from flask_restful import Resource
from repository.data import Data


class Failed(Resource):
    def get(self):
        return Data.get_fail(), 200

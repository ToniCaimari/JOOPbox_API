from flask_restful import Resource
from repository.data import Data
import json


class Start(Resource):
    def get(self):
        return Data.datos

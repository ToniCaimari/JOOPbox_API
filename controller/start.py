from flask_restful import Resource
from repository.data import Data
import json

# devuelve todos los datos sin ningún criterio añadido


class Start(Resource):
    def get(self):
        return Data.datos, 200

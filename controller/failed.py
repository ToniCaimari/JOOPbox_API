from flask_restful import Resource
from repository.data import Data

# devuelve la lista de datos que no pasaron la validación


class Failed(Resource):
    def get(self):
        return Data.get_fail(), 200

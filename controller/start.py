from flask_restful import Resource


class Start(Resource):
    def get(self):
        return {'Aqui': 'Empieza'}

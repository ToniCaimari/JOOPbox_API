from flask import Flask
from flask_restful import Resource, Api
from controller.start import Start

app = Flask(__name__)
api = Api(app)

api.add_resource(Start, '/')
api.add_resource(List, '/list')
api.add_resource(Fail, '/fail')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api
from controller.start import Start
from controller.failed import Failed
from controller.list import List


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Start, '/')
    api.add_resource(List, '/list')
    api.add_resource(Failed, '/failed')
    return app
    if __name__ == '__main__':
        app = create_app()
        app.run(debug=True)

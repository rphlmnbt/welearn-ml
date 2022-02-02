from flask import Flask
from flask_restful import Api
from controllers.testController import TestController
from controllers.mlController import MLController

app = Flask(__name__)

api = Api(app)
api.add_resource(TestController, '/test')
api.add_resource(MLController, '/ml')

if __name__ == "__main__":
    # start up api
    app.run(port=8080, debug=True)
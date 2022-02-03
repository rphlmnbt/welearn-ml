from flask import Flask
from flask_restful import Api
from controllers.testController import TestController
from controllers.mlController import MLController
from controllers.userController import UserController

app = Flask(__name__)

api = Api(app)
api.add_resource(TestController, '/test')
api.add_resource(MLController, '/ml')
api.add_resource(UserController, '/user')

if __name__ == "__main__":
    # start up api
    app.run(port=8080, debug=True)
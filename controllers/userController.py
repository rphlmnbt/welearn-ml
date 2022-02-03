from flask_restful import Resource, reqparse, request
from flask import json
from services.userService import UserService


class UserController(Resource):
    def post(self):
        user = UserService()
        json = request.json
        stats_arr = json["stats"]
        user_id = str(json["userID"])
        user.create(user_id, stats_arr)
        return 200

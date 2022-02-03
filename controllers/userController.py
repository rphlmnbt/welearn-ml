from flask_restful import request
from __main__ import app
from services.userService import UserService


@app.route('/user', methods=['POST'])
def post():
    user = UserService()
    json = request.json
    stats_arr = json["stats"]
    user_id = str(json["userID"])
    msg = user.create(user_id, stats_arr)
    return {"response" : msg }

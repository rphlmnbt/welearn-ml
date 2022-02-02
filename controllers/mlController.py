from flask_restful import Resource, reqparse, request
from flask import json
from services.mlService import MLService


class MLController(Resource):
    def post(self):
        ml = MLService()
        json = request.json

        stats_arr = json["stats"]

        proba = ml.predict(stats_arr)
        proba_true = proba[0][1]
        return {'probability': proba_true}, 200  # return data with 200 OK


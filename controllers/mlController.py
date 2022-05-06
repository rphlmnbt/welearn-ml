import json

from flask_restful import request
from __main__ import app
import numpy as np
from services.mlService import MLService


@app.route('/ml', methods=['POST'])
def predict():
    ml = MLService()
    json = request.json
    stats_arr = json["stats"]
    user_id = str(json["userID"])
    proba = ml.predict(stats_arr, user_id)
    proba_true = proba[0][1]
    return {'probability': proba_true}, 200  # return data with 200 OK


@app.route('/ml/add', methods=['POST'])
def add():
    ml = MLService()
    json = request.json
    stats_arr = json["stats"]
    user_id = json["userID"]
    out = json["out"]
    msg = ml.add(stats_arr, user_id, out)
    return {'response': msg}, 200


@app.route('/ml/batch', methods=['POST'])
def predictbatch():
    ml = MLService()
    data = request.json
    uuid_user = data["uuid_user"]
    studyPartners = data["studyPartners"]
    size = len(studyPartners)
    ratedStudyPartners = [0 for i in range(size)]
    i = 0
    for studyPartner in studyPartners:
        stats_arr = studyPartner["stats"]
        user_id = str(studyPartner["uuid_user"])
        proba = ml.predict(stats_arr, uuid_user)
        proba_true = proba[0][1]
        print(user_id)
        print(stats_arr)
        print(proba_true)
        ratedStudyPartner = {
            "uuid_user": user_id,
            "stats":  stats_arr,
            "probability": proba_true
        }
        ratedStudyPartners[i] = ratedStudyPartner
        i += 1
    response = json.dumps(ratedStudyPartners)
    return {"batch" : ratedStudyPartners}, 200

@app.route('/ml/batch/group', methods=['POST'])
def predictbatchgroup():
    ml = MLService()
    data = request.json
    uuid_users = data["uuid_users"]
    studyPartners = data["studyPartners"]
    size = len(studyPartners)
    ratedStudyPartners = [0 for i in range(size)]
    i = 0
    for studyPartner in studyPartners:
        stats_arr = studyPartner["stats"]
        user_id = str(studyPartner["uuid_user"])
        proba = ml.group_predict(stats_arr, uuid_users)
        proba_true = proba[0][1]
        print(user_id)
        print(stats_arr)
        print(proba_true)
        ratedStudyPartner = {
            "uuid_user": user_id,
            "stats":  stats_arr,
            "probability": proba_true
        }
        ratedStudyPartners[i] = ratedStudyPartner
        i += 1
    response = json.dumps(ratedStudyPartners)
    return {"batch" : ratedStudyPartners}, 200

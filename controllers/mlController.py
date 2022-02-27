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
    studyPartners = request.json
    size = len(studyPartners)
    # ratedStudyPartners = np.empty(size, dtype=object)
    ratedStudyPartners = []
    ratedStudyPartners = [0 for i in range(size)]
    i = 0
    for studyPartner in studyPartners:
        stats_arr = studyPartner["stats"]
        user_id = str(studyPartner["uuid_user"])
        proba = ml.predict(stats_arr, user_id)
        proba_true = proba[0][1]
        ratedStudyPartner = {
            "uuid_user": user_id,
            "stats":  stats_arr,
            "probability": proba_true
        }
        ratedStudyPartners[i] = ratedStudyPartner
        i += 1
    response = json.dumps(ratedStudyPartners)
    # stats_arr = json["stats"]
    # user_id = json["userID"]
    # out = json["out"]
    # msg = ml.add(stats_arr, user_id, out)
    return {"batch" : ratedStudyPartners}, 200

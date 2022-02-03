from flask_restful import request
from __main__ import app
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


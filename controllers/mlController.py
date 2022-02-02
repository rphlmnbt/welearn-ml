from flask_restful import Resource, reqparse
from services.mlService import mlService


class MLController(Resource):
    def post(self):
        ml = mlService()
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('stats', required=True)  # add args

        args = parser.parse_args()  # parse arguments to dictionary
        stats_str = args['stats']
        stats_arr = stats_str.split(',')
        for i in range(0, len(stats_arr)):
            stats_arr[i] = int(stats_arr[i])
        proba = ml.predict(stats_arr)
        proba_true = proba[0][1]
        return {'probability':proba_true}, 200  # return data with 200 OK


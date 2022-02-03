import pandas as pd
import os
import csv
from sklearn.ensemble import RandomForestClassifier


class MLService:
    def predict(self, stats, user_id):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../datasets/user-'+user_id+'.csv')
        user_data = pd.read_csv(filename, sep=',')
        x = user_data.drop(columns=['out'])
        print(x)
        y = user_data['out']
        print(y)
        model = RandomForestClassifier()
        model.fit(x, y)
        print(model.predict([stats]))
        predictions_proba = model.predict_proba([stats])
        return predictions_proba

    def add(self, stats_arr, user_id, out):
        q1 = stats_arr[0]
        q2 = stats_arr[1]
        q3 = stats_arr[2]
        q4 = stats_arr[3]
        q5 = stats_arr[4]
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../datasets/user-' + user_id + '.csv')
        with open(filename, 'a', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([q1, q2, q3, q4, q5, out])
        success_msg = "Data Added!"
        return success_msg
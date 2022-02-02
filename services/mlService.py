import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier


class MLService:
    def predict(self, stats, user_id):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '../datasets/user-'+user_id+'.csv')
        user_data = pd.read_csv(filename)
        x = user_data.drop(columns=['out'])
        y = user_data['out']
        model = RandomForestClassifier()
        model.fit(x, y)
        predictions_proba = model.predict_proba([stats])
        return predictions_proba

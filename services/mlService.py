import pandas as pd
import os
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

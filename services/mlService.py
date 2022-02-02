import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class mlService:
    def predict(self, input):
        user_data = pd.read_csv("../datasets/user.csv")
        x = user_data.drop(columns=['out'])
        y = user_data['out']
        model = RandomForestClassifier()
        model.fit(x, y)
        predictions_proba = model.predict_proba(input)
        predictions = model.predict(input)
        print(predictions)
        print(predictions_proba)
        return predictions_proba

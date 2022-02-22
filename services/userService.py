import csv
import os


class UserService:
    def create(self, user_id, stats_arr):
        dir = os.path.dirname(__file__)
        q1 = stats_arr[0]
        q2 = stats_arr[1]
        q3 = stats_arr[2]
        q4 = stats_arr[3]
        q5 = stats_arr[4]
        q6 = stats_arr[5]
        q7 = stats_arr[6]
        filename = os.path.join(dir, '../datasets/user-' + user_id + '.csv')
        with open(filename, 'w', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["q1","q2","q3","q4","q5","q6","q7","out"])
            writer.writerow([q1,q2,q3,q4,q5,q6,q7,"true"])
            writer.writerow(["0","0","0","0","0","0","0","false"])
        success_msg = "Dataset Created!"
        return success_msg

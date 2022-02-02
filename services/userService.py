import csv


class UserService:
    def create(self, user_id):
        with open('user-'+user_id+'.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["q1","q2","q3","q4","q5","out"])
        success_msg = "Dataset Created!"
        return success_msg

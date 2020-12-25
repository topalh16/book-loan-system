class User:
    def __init__(self, user_row):
        self.user_id = user_row[0]
        self.department = user_row[1]
        self.full_name = user_row[2]
        self.email = user_row[3]
        self.birth_date = user_row[4]
        self.role = user_row[5]
        self.password = user_row[6]
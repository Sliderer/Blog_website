class UserLogin:
    def __init__(self):
        self.email = ''
        self.name = ''
        self.id = 0
        self.password = ''

    def init_for_registration(self, name, password, email):
        self.email = email
        self.password = password
        self.name = name
        return self

    def init_from_tuple(self, data: tuple):
        self.id = data[0]
        self.name = data[1]
        self.password = data[2]
        self.email = data[3]
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

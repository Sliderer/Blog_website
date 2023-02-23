class UserLogin:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._id = 1

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)

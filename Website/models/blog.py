class Blog:
    def __init__(self):
        self.id = 0
        self.user_id = 0
        self.title = ''
        self.text = ''

    def init_from_tuple(self, data: tuple):
        self.id = data[0]
        self.user_id = data[1]
        self.title = data[2]
        self.text = data[3]
        return self

    def init_form_creation(self, title: str, text: str):
        self.title = title
        self.text = text
        return self
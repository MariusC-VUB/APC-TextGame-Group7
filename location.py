# Location Class
class Location:
    def __init__(self, name, description):
        self.name = name
        self.position = None
        self.description = description
        self.defeater = None

    def set_position(self, position):
        self.position = position

    def set_defeater(self, defeater):
        self.defeater = defeater

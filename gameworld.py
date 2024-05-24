class GameWorld:
    def __init__(self):
        self.locations = {}
        self.players = []

    def add_location(self, location):
        self.locations[location.get_position()] = location

    def add_player(self, player):
        self.players.append(player)

    def get_location_description(self, position):
        location = self.locations.get(position)
        if location:
            return location.description
        return "Unknown Location"

    def is_valid_position(self, position):
        return position in self.locations
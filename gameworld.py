# GameWorld Class
class GameWorld:
    def __init__(self):
        self.locations = {}
        self.players = []
        self.npcs = []
        self.defeaters = []

    def add_location(self, location):
        self.locations[location.name] = location

    def add_player(self, player):
        self.players.append(player)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def add_defeater(self, defeater):
        self.defeaters.append(defeater)

    def get_location_description(self, position):
        for location in self.locations.values():
            if location.position == position:
                return location.description
        return "Unknown Location"

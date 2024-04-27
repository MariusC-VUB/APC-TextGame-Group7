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

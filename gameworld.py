# GameWorld Class
class GameWorld:
    def __init__(self):
        self.locations = {}
        self.players = []
        self.npcs = []
        self.defeaters = []
        self.food = []
        self.weapons = []
        self.treasures = []
        self.boat = []

    def add_location(self, location):
        self.locations[location.name] = location

    def add_player(self, player):
        self.players.append(player)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def add_defeater(self, defeater):
        self.defeaters.append(defeater)

    def add_food(self, Food):
        self.food.append(Food)

    def add_weapon(self, Weapon):
        self.weapons.append(Weapon)

    def add_treasures(self, Treasure):
        self.treasures.append(Treasure)

    def add_boats(self, Boat):
        self.boat.append(Boat)

    def get_location_description(self, position):
        for location in self.locations.values():
            if location.position == position:
                return location.description
        return "Unknown Location"

# Location Class
class Location:
    def __init__(self, x_coordinate, y_coordinate):
        self.defeater = None
        self.food = []
        self.weapons = []
        self.boats = []
        self.treasures = []
        self.correct_defensive_action = None

    def set_defeater(self, defeater):
        self.defeater = defeater

    def add_food(self, food):
        self.food.append(food)

    def add_weapons(self, weapons):
        self.weapons.append(weapons)

    def add_treasures(self, treasure):
        self.treasures.append(treasure)

    def add_boat(self, boat):
        self.boats.append(boat)

    def get_boats(self):
        return self.boats

    def get_food(self):
        return self.food

    def get_weapons(self):
        return self.weapons

    def get_treasures(self):
        return self.treasures

    def get_correct_defensive_action(self):
        return self.correct_defensive_action

    # Set the correct defensive action against the currently attacking enemy.
    def set_correct_defensive_action(self, action):
        self.correct_defensive_action = action


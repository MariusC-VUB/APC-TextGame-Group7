from Item import Food, Weapon, Treasure, Boat
from defeater import Defeater

class Location:
    def __init__(self, x_coordinate, y_coordinate):
        self.position = (x_coordinate, y_coordinate)
        self.defeater = None
        self.food_list = []
        self.weapon_list = []
        self.boats = []
        self.treasures = []
        #self.correct_defensive_action = None

    def set_defeater(self, defeater):
        self.defeater = defeater

    def add_food(self, food):
        self.food_list.append(food)

    def add_weapon(self, weapon):
        self.weapon_list.append(weapon)

    def add_treasure(self, treasure):
        self.treasures.append(treasure)

    def add_boat(self, boat):
        self.boats.append(boat)

    def set_correct_defensive_action(self, action):
        self.correct_defensive_action = action

    def get_position(self):
        return self.position

class StartingPoint(Location):
    def __init__(self):
        super().__init__(0, 0)
        self.description = "Welcome. You are in the middle of the forest."

class GreenForest(Location):
    def __init__(self):
        super().__init__(1, 0)
        self.description = ("You have entered into the lush vegetation and vibrant flora.\n"
                            "This place is full of vicious snakes and terrifying enemies.\n"
                            "You have to be very careful but there are few weapons "
                            "that can help you to cope with this situation.\nYou must eat food to get points.\n"
                            "Look out! The tiger is looking at you with furious eyes.")
        self.add_weapon(Weapon("Gun", "A sniper for headshot", 100))
        self.add_weapon(Weapon("Stick", "A long wooden rod", 10))
        self.add_food(Food("Apple", "A red apple", 25))
        self.set_defeater(Defeater("Snake", 30, 10))
        self.set_defeater(Defeater("Tiger", 100, 50))
        self.add_treasure(Treasure("Coins", "One thousand silver coins", 200))
        #self.set_correct_defensive_action("use gun")

class DinoNest(Location):
    def __init__(self):
        super().__init__(-1, 0)
        self.description = "A prehistoric sanctuary."
        self.add_weapon(Weapon("Dragon Glass", "A Dragon Glass", 100))
        self.add_food(Food("Honey", "A honey", 100))
        self.set_defeater(Defeater("Dragon", 100, 50))
        #self.set_correct_defensive_action("use sword")

class DarkCave(Location):
    def __init__(self):
        super().__init__(0, -1)
        self.description = ("Welcome to the heart of the ancient forest, you are in a dark cave "
                            "where shadows come to life and the air seems to breathe with malevolence. "
                            "A monster with a long spear is heading towards you.")
        self.add_weapon(Weapon("Sword", "A katana samurai sword with a dragon handle", 50))
        self.add_food(Food("Meat", "A juicy grilled beef meat", 50))
        self.set_defeater(Defeater("Monster", 100, 50))
        #self.set_correct_defensive_action("use sword")

class RipleRiver(Location):
    def __init__(self):
        super().__init__(0, 1)
        self.description = ("Here is a serene and crystal-clear stream located in the south of the forest. "
                            "There is a beautiful island in the river.")
        self.add_treasure(Treasure("Diamond", "A pouch of diamonds", 1000))
        self.add_boat(Boat("Speed Boat"))

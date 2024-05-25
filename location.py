from Item import Food, Weapon, Treasure
from defeater import Defeater


class Location:
    def __init__(self, x_coordinate, y_coordinate):
        self.position = (x_coordinate, y_coordinate)
        self.defeater = None
        self.food_list = []
        self.weapon_list = []
        self.treasures = []
        self.add_weapon = lambda weapon: self.weapon_list.append(weapon)
        self.add_food = lambda food: self.food_list.append(food)
        self.add_treasure = lambda treasure: self.treasures.append(treasure)

    def set_defeater(self, defeater):
        self.defeater = defeater

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
        self.add_weapon(Weapon("gun", "A sniper for headshot", 100))
        self.add_weapon(Weapon("stick", "A long wooden rod", 10))
        self.add_food(Food("apple", "A red apple", 25))
        self.set_defeater(Defeater("tiger", 100, 50))
        self.add_treasure(Treasure("coins", "One thousand silver coins", 200))


class DinoNest(Location):
    def __init__(self):
        super().__init__(-1, 0)
        self.description = "A prehistoric sanctuary."
        self.add_weapon(Weapon("dragon glass", "A Dragon Glass", 100))
        self.add_food(Food("honey", "A honey", 50))
        self.set_defeater(Defeater("Dragon", 100, 100))


class DarkCave(Location):
    def __init__(self):
        super().__init__(0, -1)
        self.description = ("Welcome to the heart of the ancient forest, you are in a dark cave "
                            "where shadows come to life and the air seems to breathe with malevolence. "
                            "A monster with a long spear is heading towards you.")
        self.add_weapon(Weapon("sword", "A katana samurai sword with a dragon handle", 50))
        self.add_food(Food("meat", "A juicy grilled beef meat", 50))
        self.set_defeater(Defeater("Monster", 100, 200))


class RippleRiver(Location):
    def __init__(self):
        super().__init__(0, 1)
        self.description = ("Here is a serene and crystal-clear stream located in the south of the forest. "
                            "You are swimming in the depth of the river. Beware of crocodiles and ")
        self.add_treasure(Treasure("diamond", "A pouch of diamonds", 1000))
        self.set_defeater(Defeater("crocodile", 100, 80))

from location import Location
from Item import Food, Weapon, Treasure
from defeater import Defeater
class DarkCave(Location):
    def __init__(self, x_coordinate, y_coordinate):
        """
        Constructor
        """
        super().__init__(x_coordinate, y_coordinate)
        # Set the Location Description of the room
        self.description = " Well come to the heart of ancient forest,you are in dark cave " \
                           "where shadows come to life and air seems to breathe with malevolence." \
                           "Monster with a long spear is heading towards you..........."

        # Initialize the weapons which are in the cave.
        self.sword = Weapon("Sword", "A katana samurai sword with dragon handle", 50)

        # Initialize a meat piece
        self.meat = Food("Meat", "A juicy meat beef grilled in the fire", 50)

        # Initialize the defeaters
        self.monster = Defeater("Monster", 100, 50)

        self.add_weapons(self.sword)
        self.set_defeater(self.monster)
        self.add_food(self.meat)
        self.set_defeater(self.monster)
        self.set_correct_defensive_action("use sword")

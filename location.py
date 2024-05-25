from Item import Food, Weapon, Treasure, Boat
from defeater import Defeater

# Location Class
class Location:
    def __init__(self, x_coordinate, y_coordinate):
        self.defeater = None
        self.food_list = []
        self.weapon_list = []
        self.boats = []
        self.treasures = []
        self.correct_defensive_action = None
        self.add_weapons = lambda weapon: self.weapon_list.append(weapon)
        self.add_food = lambda food: self.food_list.append(food)
        self.add_treasures = lambda treasure : self.treasures.append(treasure)
        self.add_boat = lambda boat: self.boats.append(boat)

    # Method to set the defeater for the location
    def set_defeater(self, defeater):
        self.defeater = defeater

    def get_boats(self):
        return self.boats

    def get_treasures(self):
        return self.treasures

    def get_correct_defensive_action(self):
        return self.correct_defensive_action

    def get_food(self):
        return self.food_list

    # Set the correct defensive action against the currently attacking enemy.
    def set_correct_defensive_action(self, action):
        self.correct_defensive_action = action

class StartingPoint(Location):
    def __init__(self):
        super().__init__(0, 0)
        self.description = "Well come. You are in the middle of the forest"


class RipleRiver(Location):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(0, 1)
        # Set the Location Description
        self.description = " Here is a serene and crystal-clear stream located in the south of forest." \
                           " There is a beautiful island in the river."

        # Initialize the treasure and boat
        treasure = Treasure("Diamond", "A pouch of diamonds", 1000)
        boat = Boat("Speed Boat")
        self.add_treasures(treasure)
        self.add_boat(boat)


class GreenForest(Location):
    """
    This class describes one of the location within our game, containing information such as the description of the forest,
    food,weapon and enemies which are contained within the forest. This class is a child of the Location superclass.
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(1, 0)
        # Set the Location Description of the room
        self.description = "You have entered into the Lush vegetation and vibrant flora.\n" \
                               "This place is full of vicious snakes and terrifying enemies \n " \
                               "You have to be very careful but there are few weapons " \
                               "that can help you to cope with this situation.\nYou must eat food to get points.\n" \
                               " Look out! The tiger is looking at you with furious eyes"

        # Initialize the Tools which are in the forest.
        self.gun = Weapon("Gun","A sniper for headshot", 100)
        self.stick = Weapon("Stick", "A long wooden rod",10)

        # Initialize the food
        self.apple = Food("Apple", "A red apple", 25)

        # Initialize the defeaters
        self.snake = Defeater("Snake", 30, 10)
        self.tiger = Defeater("Tiger", 100, 50)
        self.treasure = Treasure("Coins", "One thousand silver coins", 200)

        self.add_weapons(self.gun)
        self.add_weapons(self.stick)
        self.set_defeater(self.snake)
        self.set_defeater(self.tiger)
        self.add_food(self.apple)
        self.set_defeater(self.tiger)
        self.set_correct_defensive_action("use gun")


class DinoNest(Location):
    """
    This class describes one of the location within our game, containing information such as the description of the forest,
    food,weapon and enemies which are contained within the forest. This class is a child of the Location superclass.
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__(-1, 0)
        # Set the Location Description of the room
        self.description = " A prehistoric sanctuary."

        # Initialize the weapons which are in the cave.
        self.dragon_glass= Weapon("Dragon Glass", "A Dragon Glass", 100)

        # Initialize a meat piece
        self.honey = Food("Honey", "A honey", 100)

        # Initialize the defeaters
        self.dragon = Defeater("Dragon", 100, 50)

        self.add_weapons(self.dragon_glass)
        self.set_defeater(self.dragon)
        self.add_food(self.honey)
        self.set_defeater(self.dragon)
        self.set_correct_defensive_action("use dragon glass")


class DarkCave(Location):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(0, -1)
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

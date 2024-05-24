from location import Location
from Item import Food, Weapon, Treasure
from defeater import Defeater
class GreenForest(Location):
    """
    This class describes one of the location within our game, containing information such as the description of the forest,
    food,weapon and enemies which are contained within the forest. This class is a child of the Location superclass.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Constructor
        """
        super().__init__(x_coordinate, y_coordinate)
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

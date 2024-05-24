from location import Location
from Item import Food, Weapon
from defeater import Defeater
class DinoNest(Location):
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
        self.set_correct_defensive_action("use sword")

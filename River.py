from location import Location
from Item import Treasure, Boat

class RipleRiver(Location):
    def __init__(self, x_coordinate, y_coordinate):
        """
        Constructor
        """
        super().__init__(x_coordinate, y_coordinate)
        # Set the Location Description
        self.description = " Here is a serene and crystal-clear stream located in the south of forest." \
                           " There is a beautiful island in the river."

        # Initialize the treasure and boat
        treasure = Treasure("Diamond", "A pouch of diamonds", 1000)
        boat = Boat("Speed Boat")
        self.add_treasures(self.treasures)
        self.add_boat(boat)


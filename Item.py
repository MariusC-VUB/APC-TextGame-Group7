class Item:
    def __init__(self, name, description, strength):
        self.name = name
        self.description = description
        self.strength = strength


class Food(Item):
    def __init__(self, name, description, strength):
        super().__init__(name, description, strength)


class Weapon(Item):
    def __init__(self, name, description, strength):
        super().__init__(name, description, strength)


class Treasure:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

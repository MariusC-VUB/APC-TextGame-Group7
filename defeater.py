class Defeater:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, player):
        player.hp -= self.strength
        if player.hp <= 0:
            player.hp = 0
            return f"The {self.name} hits you for {self.strength} damage. You have been defeated."
        return f"The {self.name} hits you for {self.strength} damage. You have {player.hp} HP left."

class Defeater:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, player):
        if player.extra_strength > 0:
            player.extra_strength -= self.strength
            return f"The {self.name} hits you for {self.strength} damage. You have {player.extra_strength} extra strength left."
        else:
            self.hp -= self.strength
            if self.hp <= 0:
                self.hp = 0
                return f"The {self.name} hits you for {self.strength} damage. You have been defeated."
            return f"The {self.name} hits you for {self.strength} damage. You have {self.hp} HP left."

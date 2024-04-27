import random
from tkinter import messagebox


# Player Class
class Player:
    def __init__(self, name, hp, agility, position):
        self.name = name
        self.hp = hp
        self.agility = agility
        self.position = position
        self.inventory = []

    def move(self, direction):
        directions = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }

        if direction in directions:
            dx, dy = directions[direction]
            self.position = (self.position[0] + dx, self.position[1] + dy)
            messagebox.showinfo("Move", f"You move {direction}.")
        else:
            messagebox.showinfo("Invalid", "Invalid direction.")

    def use_item(self, item):
        if item == "magical_potion" and "magical_potion" in self.inventory:
            self.hp += 20
            self.inventory.remove("magical_potion")
            messagebox.showinfo("Use Item", "You feel refreshed!")
        else:
            messagebox.showinfo("Use Item", "You don't have that item.")

    def attack(self, defeater):
        if self.position == defeater.position:
            damage = random.randint(10, 20)
            defeater.hp -= damage
            messagebox.showinfo("Attack", f"You attack the {defeater.name} and deal {damage} damage.")

            if defeater.hp <= 0:
                messagebox.showinfo("Victory", f"You defeated the {defeater.name}!")
                self.position = (0, 0)
                self.inventory.append(defeater.weapon.name)
        else:
            messagebox.showinfo("Attack", "There's nothing to attack here.")

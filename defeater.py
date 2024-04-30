import random
from tkinter import messagebox


# Defeater Class
class Defeater:
    def __init__(self, name, hp, weapon, position):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.position = position
        self.alive = True

    def attack(self, player):
        damage = random.randint(5, 15)
        player.hp -= damage
        messagebox.showinfo("Attack", f"The {self.name} attacks you and deals {damage} damage.")

        if player.hp <= 0:
            messagebox.showinfo("Game Over", "You have been defeated.")
            exit()

    def isAlive(self):
        if self.hp <= 0:
            self.alive = False
        else:
            self.alive = True


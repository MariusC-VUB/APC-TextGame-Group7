import random
from tkinter import messagebox


# Defeater Class
class Defeater:
    def __init__(self, name, hp, weapon, position):
        """
        Initialize the Defeater with a name, hit points, weapon, and position.
        """
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.position = position
        self.alive = True

    def attack(self, player):
        """
        Attack the player, dealing random damage between 5 and 15.
        If the player's hp drops to 0 or below, the game ends with a defeat message.
        """
        damage = random.randint(5, 15)
        player.hp -= damage
        messagebox.showinfo("Attack", f"The {self.name} attacks you and deals {damage} damage.")

        if player.hp <= 0:
            messagebox.showinfo("Game Over", "You have been defeated.")
            exit()

    def isAlive(self):
        """
        Check if the defeater is still alive based on its hp.
        Update the alive status accordingly.
        """
        if self.hp <= 0:
            self.alive = False
        else:
            self.alive = True


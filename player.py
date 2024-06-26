import random
from tkinter import messagebox
from defeater import Defeater

# Player Class
class Player:
    def __init__(self, name, hp, agility, position):
        self.name = name
        self.hp = hp
        self.agility = agility
        self.position = position
        self.inventory = []
        self.score = 0
        self.extra_strength = 0

    def move(self, direction):
        directions = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }

        # Determine allowed direction
        allowed_directions = self.get_allowed_directions()

        if direction in directions and direction in allowed_directions:
            dx, dy = directions[direction]
            self.position = (self.position[0] + dx, self.position[1] + dy)
            messagebox.showinfo("Move", f"You move {direction}.")
        else:
            messagebox.showinfo("Invalid", "Invalid direction. Try to go to the starting point.")

    def get_allowed_directions(self):
        # Current location
        x, y = self.position
        allowed_directions = []

        # If the player is in the center position, allow movement in any direction
        if x == 0 and y == 0:
            allowed_directions.extend(["north", "south", "east", "west"])
        # If the player is not in the center, allow movement only towards the center
        else:
            if x != 0:
                allowed_directions.append("west" if x > 0 else "east")
            if y != 0:
                allowed_directions.append("south" if y > 0 else "north")
        return allowed_directions

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

    def add_points(self,points):
        self.score += points

    def increase_strength(self,power):
        self.extra_strength += power

    def increase_health(self,health):
        self.hp += health

    def take_food(self,Food):
        self.inventory.append(Food.get_name())
        messagebox.showinfo(f"Take {Food.get_name}")

    def eat_food(self,Food):
        if Food.get_name() in self.inventory:
            self.add_points(Food.get_points())
            self.inventory.remove(Food.get_name())
            messagebox.showinfo(f"Eat {Food.get_name}","You feel refreshed")
        else:
            messagebox.showinfo(f"{Food.get_name()} is not available in your inventory")

    def take_weapon(self,Weapon):
        self.inventory.append(Weapon.get_name())

    def use_weapon(self, Weapon):
        if Weapon.get_name() in self.inventory:
            self.increase_strength(Weapon.get_damage())
            self.inventory.remove(Weapon.get_name())
            messagebox.showinfo(f"Use {Weapon.get_name}","You feel refreshed")
        else:
            messagebox.showinfo(f"{Weapon.get_name()} is not available in your inventory")

    def take_treasure(self, Treasure):
        if Defeater.isAlive() == False:
            Treasure.use_treasure()
            self.add_points(Treasure.get_treasure())
            messagebox.showinfo(f"{Treasure.get_description()} has been picked.... Hurah!!!!!!")
        else:
            messagebox.showinfo("First kill all the enemies around you")

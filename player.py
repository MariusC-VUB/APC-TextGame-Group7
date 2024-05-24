import random
from tkinter import messagebox
from Item import Food, Weapon, Treasure, Boat

class Player:
    def __init__(self, name, hp, agility, position, game_world):
        self.name = name
        self.hp = hp
        self.agility = agility
        self.position = position
        self.inventory = []
        self.score = 0
        self.extra_strength = 0
        self.game_world = game_world

    def move(self, direction):
        directions = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }

        if direction in directions:
            dx, dy = directions[direction]
            new_position = (self.position[0] + dx, self.position[1] + dy)
            if self.game_world.is_valid_position(new_position):
                self.position = new_position
                messagebox.showinfo("Move", f"You moved to {direction}.")
            else:
                messagebox.showinfo("Move", "You can't move in that direction!")
        else:
            messagebox.showinfo("Move", "Invalid direction!")

    def use_item(self, item_name):
        item = next((item for item in self.inventory if item.name == item_name), None)
        if item:
            self.inventory.remove(item)
            if isinstance(item, Food):
                self.hp += item.strength
                messagebox.showinfo("Use Item", f"You used {item_name} and gained {item.strength} HP.")
            elif isinstance(item, Weapon):
                self.extra_strength += item.strength
                messagebox.showinfo("Use Item", f"You used {item_name} and gained {item.strength} extra strength.")
            elif isinstance(item, Treasure):
                self.score += item.value
                messagebox.showinfo("Use Item", f"You used {item_name} and gained {item.value} points.")
            elif isinstance(item, Boat):
                messagebox.showinfo("Use Item", f"You used {item_name} to travel on water.")
        else:
            messagebox.showinfo("Use Item", f"{item_name} is not in your inventory.")

    def take_food(self, food_name):
        current_location = self.game_world.locations.get(self.position)
        if current_location:
            food = next((food for food in current_location.food_list if food.name == food_name), None)
            if food:
                self.inventory.append(food)
                current_location.food_list.remove(food)
                messagebox.showinfo("Take Food", f"You took {food_name}.")
            else:
                messagebox.showinfo("Take Food", f"{food_name} is not available here.")

    def eat_food(self, food_name):
        food = next((food for food in self.inventory if food.name == food_name), None)
        if food:
            self.inventory.remove(food)
            self.hp += food.strength
            messagebox.showinfo("Eat Food", f"You ate {food_name} and gained {food.strength} HP.")
        else:
            messagebox.showinfo("Eat Food", f"{food_name} is not in your inventory.")

    def take_weapon(self, weapon_name):
        current_location = self.game_world.locations.get(self.position)
        if current_location:
            weapon = next((weapon for weapon in current_location.weapon_list if weapon.name == weapon_name), None)
            if weapon:
                self.inventory.append(weapon)
                current_location.weapon_list.remove(weapon)
                messagebox.showinfo("Take Weapon", f"You took {weapon_name}.")
            else:
                messagebox.showinfo("Take Weapon", f"{weapon_name} is not available here.")

    def use_weapon(self, weapon_name):
        weapon = next((weapon for weapon in self.inventory if weapon.name == weapon_name), None)
        if weapon:
            self.extra_strength += weapon.strength
            messagebox.showinfo("Use Weapon", f"You used {weapon_name} and gained {weapon.strength} extra strength.")
        else:
            messagebox.showinfo("Use Weapon", f"{weapon_name} is not in your inventory.")

    def take_treasure(self, treasure_name):
        current_location = self.game_world.locations.get(self.position)
        if current_location:
            treasure = next((treasure for treasure in current_location.treasures if treasure.name == treasure_name), None)
            if treasure:
                self.inventory.append(treasure)
                current_location.treasures.remove(treasure)
                messagebox.showinfo("Take Treasure", f"You took {treasure_name}.")
            else:
                messagebox.showinfo("Take Treasure", f"{treasure_name} is not available here.")

    def attack(self, enemy):
        player_damage = self.agility + self.extra_strength + random.randint(0, 10)
        enemy.hp -= player_damage
        if enemy.hp <= 0:
            messagebox.showinfo("Attack", f"You defeated the {enemy.name}!")
        else:
            messagebox.showinfo("Attack", f"You attacked the {enemy.name} for {player_damage} damage. {enemy.hp} HP remaining.")

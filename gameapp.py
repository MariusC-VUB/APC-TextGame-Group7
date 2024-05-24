import tkinter as tk
from tkinter import messagebox, simpledialog
from gameworld import GameWorld
from location import StartingPoint, DarkCave, DinoNest, GreenForest,RipleRiver
from player import Player

# Main Game Logic
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.location_list = []

        self.title("Mystical Forest Adventure")

        self.game_world = GameWorld()

        # Initialize locations
        self.location_list.append(StartingPoint)
        self.location_list.append(GreenForest)
        self.location_list.append(DinoNest)
        self.location_list.append(DarkCave)
        self.location_list.append(RipleRiver)

        # Initialize player
        player_name = simpledialog.askstring("Input", "Enter your name:")
        # Set the initial position of the player to match an existing location
        initial_position = (0, 0)  # Adjust the initial position to match an existing location
        self.player = Player(player_name, 100, 10, initial_position)
        self.game_world.add_player(self.player)


        # Create GUI elements
        self.label = tk.Label(self, text=self.game_world.get_location_description(self.player.position))
        self.label.pack(pady=20)

        self.move_button = tk.Button(self, text="Move", command=self.move_dialog)
        self.move_button.pack(pady=20)

        self.use_item_button = tk.Button(self, text="Use Item", command=self.use_item_dialog)
        self.use_item_button.pack(pady=20)

        self.attack_button = tk.Button(self, text="Attack", command=self.attack_dialog)
        self.attack_button.pack(pady=20)

        self.take_food_button = tk.Button(self, text = "Take food", command = self.take_food_dialog)
        self.take_food_button.pack(pady=20)

        self.eat_food_button = tk.Button(self, text = "Eat Food", command = self.eat_food_dialog)
        self.eat_food_button.pack(pady=20)

        self.pick_weapon_button =tk.Button(self, text = "Pick weapon", command = self.take_weapon_dialog)
        self.take_food_button.pack(pady=20)

        self.use_weapon_button = tk.Button(self, text= "Use Weapon", command= self.use_weapon_dialog)
        self.use_weapon_button.pack(pady=20)

        self.pick_treasure_button = tk.Button(self, text= "Pick Treasure", command= self.take_treasure_dialog)
        self.pick_treasure_button.pack(pady=20)

    def move_dialog(self):
        direction = simpledialog.askstring("Input", "Which direction? (north/south/east/west)")
        self.player.move(direction)
        self.label.config(text=self.game_world.get_location_description(self.player.position))

    def use_item_dialog(self):
        item = simpledialog.askstring("Input", "Which item?")
        self.player.use_item(item)

    def take_food_dialog(self):
        food = simpledialog.askstring("Input","Which food?")
        self.player.take_food(food)

    def eat_food_dialog(self):
        eat_food = simpledialog.askstring("Input","Which food?")
        self.player.eat_food(eat_food)

    def take_weapon_dialog(self):
        weapon = simpledialog.askstring("Input","Which weapon")
        self.player.take_food(weapon)

    def use_weapon_dialog(self):
        take_weapon = simpledialog.askstring("Input","Which weapon")
        self.player.use_weapon(take_weapon)

    def take_treasure_dialog(self):
        treasure = simpledialog.askstring("Input","Treasure")
        self.player.take_treasure(treasure)

    def attack_dialog(self):
        current_location = self.game_world.locations[self.player.position]
        if current_location.defeater:
            enemy = current_location.defeater
            self.player.attack(enemy)
            self.label.config(text=self.game_world.locations[self.player.position].description)
        else:
            messagebox.showinfo("Attack", "There's nothing to attack here.")


import tkinter as tk
from tkinter import messagebox, simpledialog
from defeater import Defeater
from gameworld import GameWorld
from location import Location
from player import Player

# Main Game Logic
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mystical Forest Adventure")

        self.game_world = GameWorld()

        # Initialize locations
        green_forest = Location("Green Forest", "Lush vegetation and vibrant flora.")
        dark_cave = Location("Dark Cave", "A mysterious and shadowy underworld.")
        dino_nest = Location("Dino Nest", "A prehistoric sanctuary.")
        ripple_river = Location("Ripple River", "A serene and crystal-clear stream.")

        self.game_world.add_location(green_forest)
        self.game_world.add_location(dark_cave)
        self.game_world.add_location(dino_nest)
        self.game_world.add_location(ripple_river)

        # Initialize weapons
        dinosaur = "Dinosaur"
        magical_potion = "Magical Potion"

        # Initialize defeaters
        dragon = Defeater("Dragon", 50, dinosaur, (1, 1))
        monster = Defeater("Monster", 30, None, (-1, -1))
        fairy = Defeater("Fairy", 10, None, (2, 2))
        enchanted_guardian = Defeater("Enchanted Guardian", 40, None, (-2, -2))

        self.game_world.add_defeater(dragon)
        self.game_world.add_defeater(monster)
        self.game_world.add_defeater(fairy)
        self.game_world.add_defeater(enchanted_guardian)

        # Initialize player
        player_name = simpledialog.askstring("Input", "Enter your name:")
        # Set the initial position of the player to match an existing location
        initial_position = (0, 0)  # Adjust the initial position to match an existing location
        self.player = Player(player_name, 100, 10, initial_position)
        self.game_world.add_player(self.player)

        # # Initialize player
        # player_name = simpledialog.askstring("Input", "Enter your name:")
        # # Set the initial position of the player to match an existing location
        # initial_position = (0, 0)  # Adjust the initial position to match an existing location
        # self.player = Player(player_name, 100, 10, initial_position)
        # self.game_world.add_player(self.player)

        # Create GUI elements
        self.label = tk.Label(self, text=self.game_world.locations[self.player.position].description)
        self.label.pack(pady=20)

        self.move_button = tk.Button(self, text="Move", command=self.move_dialog)
        self.move_button.pack(pady=20)

        self.use_item_button = tk.Button(self, text="Use Item", command=self.use_item_dialog)
        self.use_item_button.pack(pady=20)

        self.attack_button = tk.Button(self, text="Attack", command=self.attack_dialog)
        self.attack_button.pack(pady=20)

    def move_dialog(self):
        direction = simpledialog.askstring("Input", "Which direction? (north/south/east/west)")
        self.player.move(direction)
        self.label.config(text=self.game_world.locations[self.player.position].description)

    def use_item_dialog(self):
        item = simpledialog.askstring("Input", "Which item?")
        self.player.use_item(item)

    def attack_dialog(self):
        current_location = self.game_world.locations[self.player.position]
        if current_location.defeater:
            enemy = current_location.defeater
            self.player.attack(enemy)
            self.label.config(text=self.game_world.locations[self.player.position].description)
        else:
            messagebox.showinfo("Attack", "There's nothing to attack here.")


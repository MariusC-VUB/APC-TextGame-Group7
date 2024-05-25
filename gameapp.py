import tkinter as tk
from tkinter import messagebox, simpledialog
from gameworld import GameWorld
from location import StartingPoint, DarkCave, DinoNest, GreenForest, RippleRiver
from player import Player

class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mystical Forest Adventure")
        self.game_world = GameWorld()

        # Initialize locations
        self.game_world.add_location(StartingPoint())
        self.game_world.add_location(GreenForest())
        self.game_world.add_location(DinoNest())
        self.game_world.add_location(DarkCave())
        self.game_world.add_location(RippleRiver())

        # Initialize player
        player_name = simpledialog.askstring("Input", "Enter your name:")
        initial_position = (0, 0)
        self.player = Player(player_name, 100, 10, initial_position, self.game_world)
        self.game_world.add_player(self.player)

        # Create GUI elements
        self.label = tk.Label(self, text=self.game_world.get_location_description(self.player.position))
        self.label.pack(pady=20)

        self.move_button = tk.Button(self, text="Move", command=self.move_dialog)
        self.move_button.pack(pady=20)

        self.use_item_button = tk.Button(self, text="Use Treasure", command=self.use_treasure_dialog)
        self.use_item_button.pack(pady=20)

        self.attack_button = tk.Button(self, text="Attack", command=self.attack_dialog)
        self.attack_button.pack(pady=20)

        self.take_food_button = tk.Button(self, text="Take Food", command=self.take_food_dialog)
        self.take_food_button.pack(pady=20)

        self.eat_food_button = tk.Button(self, text="Eat Food", command=self.eat_food_dialog)
        self.eat_food_button.pack(pady=20)

        self.pick_weapon_button = tk.Button(self, text="Pick Weapon", command=self.take_weapon_dialog)
        self.pick_weapon_button.pack(pady=20)

        self.use_weapon_button = tk.Button(self, text="Use Weapon", command=self.use_weapon_dialog)
        self.use_weapon_button.pack(pady=20)

        self.pick_treasure_button = tk.Button(self, text="Pick Treasure", command=self.take_treasure_dialog)
        self.pick_treasure_button.pack(pady=20)

        self.exit_button = tk.Button(self, text="Health and Score", command=self.check_attributes)
        self.exit_button.pack(pady=20)

        self.exit_button = tk.Button(self, text= "Exit", command= self.exit_dialog)
        self.exit_button.pack(pady=20)

    def move_dialog(self):
        direction = simpledialog.askstring("Input", "Which direction? (north/south/east/west)")
        self.player.move(direction.lower())
        self.label.config(text=self.game_world.get_location_description(self.player.position))

    def use_treasure_dialog(self):
        treasure = simpledialog.askstring("Input", "Which item?")
        self.player.use_treasure(treasure.lower())

    def take_food_dialog(self):
        food = simpledialog.askstring("Input", "Which food?")
        self.player.take_food(food.lower())

    def eat_food_dialog(self):
        eat_food = simpledialog.askstring("Input", "Which food?")
        self.player.eat_food(eat_food.lower())

    def take_weapon_dialog(self):
        weapon = simpledialog.askstring("Input", "Which weapon?")
        self.player.take_weapon(weapon.lower())

    def use_weapon_dialog(self):
        weapon = simpledialog.askstring("Input", "Which weapon?")
        self.player.use_weapon(weapon.lower())

    def take_treasure_dialog(self):
        treasure = simpledialog.askstring("Input", "Which treasure?")
        self.player.take_treasure(treasure.lower())

    def attack_dialog(self):
        if self.player.hp > 0:
            current_location = self.game_world.locations.get(self.player.position)
            if current_location and current_location.defeater:
                enemy = current_location.defeater
                self.player.attack(enemy)
                if enemy.hp > 0:
                    result = enemy.attack(self.player)
                    messagebox.showinfo("Attack Result", result)
                self.label.config(text=self.game_world.get_location_description(self.player.position))
            else:
                messagebox.showinfo("Attack", "There's nothing to attack here.")

        else:
            messagebox.showinfo("Game Over", f"You scored {self.player.score}")
            messagebox.showerror("Game Over")
            self.quit()

    def exit_dialog(self):
        self.quit()

    def check_attributes(self):
        messagebox.showinfo("Health and Score",f"Your score is {self.player.score}, health is {self.player.hp}"
                                               f" and strength is {self.player.extra_strength}")

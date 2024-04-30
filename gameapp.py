import tkinter as tk
from tkinter import messagebox, simpledialog
from defeater import Defeater
from gameworld import GameWorld
from location import Location
from player import Player
from Item import Food, Weapon, Boat,Treasure

# Main Game Logic
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mystical Forest Adventure")

        self.game_world = GameWorld()

        # Initialize locations
        initial_location = Location("Starting Point", "Beginning of the adventure.")
        initial_location.set_position((0, 0))
        green_forest = Location("Green Forest", "Lush vegetation and vibrant flora.")
        green_forest.set_position((1, 0))
        dark_cave = Location("Dark Cave", "A mysterious and shadowy underworld.")
        dark_cave.set_position((-1, 0))
        dino_nest = Location("Dino Nest", "A prehistoric sanctuary.")
        dino_nest.set_position((0, 1))
        ripple_river = Location("Ripple River", "A serene and crystal-clear stream.")
        ripple_river.set_position((0, -1))

        self.game_world.add_location(initial_location)
        self.game_world.add_location(green_forest)
        self.game_world.add_location(dark_cave)
        self.game_world.add_location(dino_nest)
        self.game_world.add_location(ripple_river)

        # Initialize weapons
        dinosaur = "Dinosaur"
        magical_potion = "Magical Potion"
        sword = Weapon("Sword","A katana samurai sword with dragon handle",50)
        gun = Weapon("Shotgun","Purdey Sidelock Shotgun",50)
        stick = Weapon("Stick","A thin wooden stick",10)

        # Initialize defeaters
        dragon = Defeater("Dragon", 50, dinosaur, (1, 1))
        monster = Defeater("Monster", 30, None, (-1, -1))
        fairy = Defeater("Fairy", 10, None, (2, 2))
        enchanted_guardian = Defeater("Enchanted Guardian", 40, None, (-2, -2))

        #Initialize foods
        apple = Food("Apple","A big red apple",20)
        pizza = Food ("Pizza", "A loaded cheese pizza with chicken cubes",100)

        #Initialize treasure
        diamonds = Treasure("Diamonds","A pouch of diamonds",1000)
        coins = Treasure("Coins","A bag of silver coins",200)

        #Initialize the boat
        boat = Boat("A white speedboat")

        #Initialize
        self.game_world.add_defeater(dragon)
        self.game_world.add_defeater(monster)
        self.game_world.add_defeater(fairy)
        self.game_world.add_defeater(enchanted_guardian)

        #Add the food
        self.game_world.add_food(apple)
        self.game_world.add_food(pizza)

        #Add the weapons
        self.game_world.add_weapon(stick)
        self.game_world.add_weapon(gun)
        self.game_world.add_weapon(sword)

        #Add the boat
        self.game_world.add_boats(boat)

        #Add the treasures
        self.game_world.add_treasures(coins)
        self.game_world.add_treasures(diamonds)

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


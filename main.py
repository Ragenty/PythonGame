import random as rand
import time as tm
import json

# Function to save variables to JSON
def save_variables_to_json(file_path, **kwargs):
    try:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}
    
    existing_data.update(kwargs)
    
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

# Variables
# Stats
health = 0
strength = 0
mana = 0
agility = 0
luck = 0

# Asks user for basic information
# Asks user for their user name
while True:
    try:
        user_name = input("What is your name?  ")
        if user_name.isalpha():
            print("Hello ", user_name,".")
            break
        else:
            raise TypeError
    except TypeError:
        print("Please enter letters only.")

# Asks user what class they choose
while True:
    try:
        player_class = input("What class do you want to be? Your following options are, Warrior, Mage, Archer, and Healer.")
        if player_class.isalpha() and player_class.lower() in ['warrior', 'mage', 'archer', 'healer']:
            print("You chose ",player_class)
            break
        else:
            raise TypeError
    except TypeError:
        print("Please enter a valid option from the given choices.")

# Class Stats
if player_class == "warrior":
    health = 150
    strength = 20
    mana = 5
    agility = 15
    luck = 10
elif player_class == "mage":
    health = 80
    strength = 8
    mana = 25
    agility = 10
    luck = 10
elif player_class == "archer":
    health = 100
    strength = 10
    mana = 5
    agility = 20
    luck = 15
elif player_class == "healer":
    health = 150
    strength = 5
    mana = 25
    agility = 10
    luck = 15

# Save stats to JSON file
save_variables_to_json("save.json", health=health, strength=strength, mana=mana, agility=agility, luck=luck)

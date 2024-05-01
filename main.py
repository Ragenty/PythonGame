import random as rand
import time as tm
import json

# Functions
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

def rest(time, day):
    global year
    if time >= 24:
        day += 1
        time %= 24  # Reset time to be within 24 hours
    if day >= 365:
        day %= 365  # Reset day to be within 365 days
        # Assuming year is a global variable
        year += 1
    return time, day


# Lists / Dictionaries
starting_towns = [
    "Amberglade",
    "Aspenwood",
    "Bramblewood",
    "Birchwood",
    "Briarwood",
    "Briarthorn",
    "Cedarcrest",
    "Dewdrop Valley",
    "Duskwood",
    "Ember Hollow",
    "Emberwood",
    "Fernhaven",
    "Frostvale",
    "Frostfall",
    "Frostwood",
    "Goldenleaf",
    "Hazelwood",
    "Honeydew",
    "Lavender Hill",
    "Maplewood",
    "Merkwood",
    "Mistwood",
    "Misty Hollow",
    "Moonlit Hollow",
    "Moonshadow",
    "Mossy Hollow",
    "Nightshade",
    "Oakwood",
    "Pinecrest",
    "Riverbend",
    "Sablewood",
    "Shadowbrook",
    "Shadewind",
    "Shimmering Vale",
    "Silverbrook",
    "Silverglade",
    "Starlight Hollow",
    "Sunburst Meadow",
    "Sunflower Grove",
    "Sunlit Grove",
    "Sylvan Glen",
    "Thistlewood",
    "Thornvale",
    "Thornwood",
    "Twilight Vale",
    "Whispering Oaks",
    "Whispering Pines",
    "Whisperwind",
    "Willowbend",
    "Willowmere"]
starting_town_coordinates = {
    "Amberglade": (14, 29),
    "Aspenwood": (14, 76),
    "Bramblewood": (54, 22),
    "Birchwood": (21, 43),
    "Briarwood": (58, 56),
    "Briarthorn": (37, 11),
    "Cedarcrest": (62, 78),
    "Dewdrop Valley": (23, 77),
    "Duskwood": (70, 57),
    "Ember Hollow": (65, 15),
    "Emberwood": (42, 88),
    "Fernhaven": (12, 15),
    "Frostvale": (26, 99),
    "Frostfall": (55, 44),
    "Frostwood": (45, 32),
    "Goldenleaf": (87, 44),
    "Hazelwood": (92, 88),
    "Honeydew": (82, 68),
    "Lavender Hill": (83, 25),
    "Maplewood": (31, 87),
    "Merkwood": (77, 86),
    "Mistwood": (26, 63),
    "Misty Hollow": (97, 28),
    "Moonlit Hollow": (28, 19),
    "Moonshadow": (92, 11),
    "Mossy Hollow": (94, 89),
    "Nightshade": (57, 69),
    "Oakwood": (29, 47),
    "Pinecrest": (41, 49),
    "Riverbend": (52, 91),
    "Sablewood": (77, 55),
    "Shadowbrook": (63, 82),
    "Shadewind": (12, 91),
    "Shimmering Vale": (99, 76),
    "Silverbrook": (95, 15),
    "Silverglade": (60, 35),
    "Starlight Hollow": (53, 10),
    "Sunburst Meadow": (75, 99),
    "Sunflower Grove": (18, 99),
    "Sunlit Grove": (91, 95),
    "Sylvan Glen": (82, 40),
    "Thistlewood": (30, 32),
    "Thornvale": (88, 60),
    "Thornwood": (97, 79),
    "Twilight Vale": (41, 81),
    "Whispering Oaks": (32, 64),
    "Whispering Pines": (13, 55),
    "Whisperwind": (81, 12),
    "Willowbend": (24, 18),
    "Willowmere": (59, 70)
}


# Variables
time = 12 # Time is in 24 hour format
day = 35 # 365 days in a year
year = 873
# Stats
health = 0
strength = 0
mana = 0
agility = 0
luck = 0
level = 1
exp = 0
# Position
starting_town=rand.choice(starting_towns)
xcor = 0
ycor = 0


# Asks user for basic information
# Asks user for their user name
while True:
    try:
        user_name = input("What is your name?  ")
        if user_name.replace(' ', '').isalpha():
            user_name = ' '.join(word.capitalize() for word in user_name.split())
            print("Hello", user_name,".")
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
save_variables_to_json("save.json", user_name=user_name, player_class=player_class, health=health, strength=strength, mana=mana, agility=agility, luck=luck, xcor=xcor, ycor=ycor, time=time, year=year, day=day, level=level, exp=exp)

#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place: (forest or cave) ")

if place == "forest":
    action = input("climb a tree or cross a river: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else:
    print("You found a hidden treasure!")

#Task 2: Setting the Scene Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: (forest or cave) ")

if place == "forest":
    action = input("climb a tree or cross a river: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark: ")
    if action == "light a torch":
        print("You found some diamonds!")
    elif action == "proceed in the dark":
        print("You walked into a family of bears! run!!")

#Task 3: Default Path If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

place = input("Choose a place: (forest or cave) ")

if place == "forest":
    action = input("climb a tree or cross a river: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark: ")
    if action == "light a torch":
        print("You found some diamonds!")
    elif action == "proceed in the dark":
        print("You walked into a family of bears! run!!")
else:
    pass
    print("Choose again!")
#Note for Mr. Jeffer's. This code aims to create a rudimentary text-based adventure game that utilizes coding concepts that we have only learned in class while still aiming to create a fun and enjoyable game for the user. 

#Mr. Jeffers, there is also no ambiguity. I spent 5 hours checking and writing this code with specific comments etc
import random  # Allows our code to randomly select from list or other groups later on

inventory = {  # User can acquire items, resources, and weapons throughout the game
    "food": 0, 
    "water": 0,
    "glock": False,  # Because you either have it or you don't
    "ammo": 0,
    "medkit": 0,

    "flare": False,  # Same as glock"
}

alive = True  # Goal is to stay alive and survive the jungle. This thus determines a win or loss
escaped = False

def pause():  # Allows the user to read before continuing on 
    input("\n[Press the Enter or Return key to continue] ")  # /n just creates that new line #This helps it feel more like a adventure game rather than a story

def choice(prompt, options):  # This prompts the user for a response until they give a valid option
    print()
    print(prompt)
    for key, text in options.items():  # Calls on that dictionary 
        print(f"{key}) {text}")  # F allows us to call on those variables
    while True: 
        ans = input("> ").strip().lower()  # Lowercases and removes spaces from the user input 
        if ans in options:
            return ans  # ans means answer
        print("Pick one of the options above.")  # Prompt user again if they dont give valid option

def show_inventory():  # Just so the user knows what they have 
    print("\nINVENTORY")
    print(f"Food rations: {inventory['food']}")
    print(f"Water bottles: {inventory['water']}")
    print(f"Medkits: {inventory['medkit']}")
    if inventory["glock"]:
        print(f"Glock: YES ({inventory['ammo']} rounds left)")
    else:
        print("Glock: NO")  # If they have a glock it shows them how much ammo they have otherwise it only needs to say no 
    

def start_scene():  # Now that all of the prerequisite stuff is made we can start the game. Everything here is not mostly a repetition of the same concepts repeated until the game is finished. Therefore, comments will be limited. 
    print("You're roused suddenly to loud sounds, yelling, and uncontrollable movement.")
    print("You realize that you’re on a small plane diving straight down over a dense jungle. ")
    pause()  # Lets them read before choosing to continue 
    print("The impact is a blur. It’s loud and dark.")
    pause()
    print("You soon open your eyes and everything is silent.")
    print("You’re strapped down to your seat in the middle of the jungle.")
    pause()  # Makes that inventory now visible
    after_crash()

def search_bags():  # Just like fortnite type stuff
    print("\n You decide to crawl through the wrecked plane searching loose luggage and overhead cabins.")
    loot_rolls = [
        ("food", random.randint(1, 3)),  # Changes the amount of provisions they have 
        ("water", random.randint(1, 3)),
        ("medkit", random.randint(0, 1)),
    ]
    found_glock = random.random() < 0.9  # 90% chance they find a glock

    for item, amount in loot_rolls:
        if amount > 0:
            inventory[item] += amount  # tells the user what they found and adds it to their inventory
            print(f"You found {amount} x {item}.")

    if found_glock and not inventory["glock"]:
        inventory["glock"] = True  # Either have it or dont 
        ammo = random.randint(4, 10)  # Random number of bullets
        inventory["ammo"] += ammo
        print(f"You are shocked to have found a Glock and {ammo} rounds of ammo.")
    else:
        print("You continue to rummage through some bags but nothing else turns up.")  # USES THOSE IF ELSE STATEMENTS YOU REQUIRED FROM US

    pause() 

def search_cockpit():  # If the user decides to search the cockpit
    print("\n You climb toward the cockpit of the plane dodging dead bodies and bags.")
    print("The pilots are dead. You try not to look too closely.")
    print("Most of the tools are broken. Nothing of use appears.")
    flare_chance = random.random()
    if flare_chance < 0.5:  # 50% chance you find a flare
        print("You managed to find an emergency kit with a single flare gun in it.")
        inventory["flare"] = True  # now user has a flare gun 
    else:
        print("All the emergency gear is missing and gone. Nothing of real use is left.")
    pause()

def eat_and_drink():  # Allows the user to use that food and water 
    print("\nYou’re overwrought. You sit for a moment to understand how you will move forward.")
    if inventory["food"] > 0:  # So that they can only eat if they found food
        print("You eat some food.")
        inventory["food"] -= 1  # So food diminishes once eaten
    else:
        print("You got nothing to eat.")
    if inventory["water"] > 0:
        print("You drink some water.")
        inventory["water"] -= 1  # Same concept as food
    else:
        print("You got nothing to drink.")
    pause()

def after_crash():
    while True: 
        show_inventory()  # Shows the user what they have
        options = {
            "1": "Search bags in the wreckage.",
            "2": "Check the cockpit.",
            "3": "Eat/drink and gather yourself.",
            "4": "Leave the wreck and head into the jungle."
        }  # Lets the user decide what they want to do. Eventually they will have to leave and head into jungle
        c = choice("What do you do?", options)

        if c == "1":
            search_bags()
        elif c == "2":
            search_cockpit()
        elif c == "3":  # All this is pretty self explanatory and use baisc else if conditions
            eat_and_drink()
        elif c == "4":
            jungle_hub()
            break

def jungle_hub():
    print("\nYou decide to step away from the wreck into a vast, interminable jungle.")
    print("The jungle surrounding you hums and you think you hear some sort of engine sounds. You figure it’s just from the plane right?")
    pause()

    while alive and not escaped:
        show_inventory()  # Lets them again choose how they want to proceed
        options = {
            "1": "Follow the sound of running water (river)",
            "2": "Climb toward higher ground (ridge)",
            "3": "Follow a faint trail through the jungle",
            "4": "Go back to the wreck",
        }
        c = choice("Which direction do you choose?", options)

        if c == "1":
            river_scene()
        elif c == "2":
            ridge_scene()  # Allows them to input what they want to do 
        elif c == "3":
            trail_scene()
        elif c == "4":
            print("\nYou head back to the wreck to regroup.")
            pause()
            after_crash()
            # after_crash eventually returns to jungle_hub again. Repeated cycle 

        if not alive or escaped:
            break  # Pretty simple. If your dead we cant continue 

def river_scene():
    global alive, escaped
    print("\nYou continue through the jungle until you reach what appears to be a muddy riverbank.")
    print("The water is rapid, brown, and dirty. You assume you’re somewhere in the Amazon. Likely South America.")
    event = random.choice(["snake", "cartel", "quiet"])
    pause()  # will encounter a random event

    if event == "snake":
        print("As you’re walking a colorful snake lunges at you from the bushes.")
        if inventory["glock"] and inventory["ammo"] > 0:
            options = {
                "1": "Try to avoid it",  # if they have a glock with ammo they can use it 
                "2": "Use the Glock",
            }
            c = choice("What shall you do?", options)
            if c == "1":  # if they choose to avoid it obv
                if random.random() < 0.6:  # 60% chance they can avoid it
                    print("You stumble away, apparently safe.")
                else:
                    print("You suddenly slip, the snake bites your ankle, and it burns.")
                    print("Without antivenom, you don’t last long in the jungle.")
                    alive = False  # simply dies and game ends
            else:
                inventory["ammo"] -= 1
                print("You fire a shot. It’s loud. The snake stops moving, apparently dead.")
                print("The gunshot is loud and echoes the forest. If someone else is around they definitely heard it.")
        else:
            print("You jump back instinctively with your heart pounding.")
            if random.random() < 0.5:  # 50% chance 
                print("The snake misses and disappears back into the jungle.")
            else:
                print("Suddenly, it sinks its fangs deep into your ankle.")
                print("You try to get away but somthing isnt right.")
                alive = False
        pause()

    elif event == "cartel":  # another event user can encounter
        cartel_encounter(location="river")
    else:
        print("It's very quiet and you, thirsty, decide to refill your water bottle from the river.")
        inventory["water"] += 1  # simple logic
        pause()

def ridge_scene():  # another contingent event
    global alive, escaped
    print("\n You carefully hike up to higher ground to understand where you are.")
    print("At the top of the mountain, you can see more jungle, and smoke in the distance.")
    pause()
    options = {  # lets the user choose what they do 
        "1": "Head toward the smoke",
        "2": "Fire a flare if you have one",
        "3": "Go back down",
    }
    c = choice("What do you do?", options)  # so what happens for each option they could choose

    if c == "1": 
        cartel_encounter(location="camp")
    elif c == "2":
        if inventory.get("flare", False):
            print("\nNight falls. You shoot the flare into the air.")
            print("It shoots up into the air lighting up the night sky...")
            pause()
            print("After awhile you hear what sounds like a helicopter or drone.")
            print("Helps arrived! You’re spotted and saved.")
            escaped = True
        else:
            print("\nYou search your pockets.No flare to call for help.")
        pause()
    elif c == "3":
        print("\nYou decide it’s safer to go below the near tree line.")
        pause()

def trail_scene():
    global alive, escaped
    print("\nYou find what appears to be some sort of primitive trail. Broken branches, footprints, and cigarette butts.")
    print("Someone clearly uses this path. Could be good. Could be bad.")
    pause()
    options = {
        "1": "Follow the trail.",
        "2": "Mark the spot and turn back hoping help shall soon arrive.",
    }
    c = choice("What do you do?", options)  # gives them a choice ONCE AGAIN

    if c == "1":
        cartel_encounter(location="trail")
    else:
        print("\nYou mark the spot with a stick and head back.")
        pause()

def cartel_encounter(location):  # basic cartel encounter that gives that engages the user
   
    global alive, escaped
    print("\nAfter some walking in the jungle you hear voices and people talking.")
    if location == "camp":  # if there at the camp
        print("You spot a rough camp with armed men, fentanyl, and a few trucks. In the Amazon maybe? Definitely cartel.")
    elif location == "river":
        print("On the other side of the riverbank you see what appears to be men unloading somthing from a boat.")
    else:
        print("On the trail appears some men simply talking and smoking.")

    pause()

    options = {
        "1": "Hide and wait",  # MORE CHOICES!!!
        "2": "Try to sneak around",
    }
    if inventory["glock"] and inventory["ammo"] > 0:  # checks for ammo again
        options["3"] = "Keep your distance but keep the Glock ready."  # AT THE PRECIPICE OF SOME ACTION #if they choose the 3rd option

    c = choice("What do you do?", options)

    if c == "1":
        print("\nYou duck behind the thick bushes and be sure not to move an inch.")
        if random.random() < 0.7:
            print("They pass by, not noticing you.")
            print("you hear them mention somthing about a airstrip nearby.")
            print("You realize if you can find this airstrip, you might have a chance of actually escaping.")
            pause()
            airstrip_scene()
        else:
            print("One of them hears noise in the bushes.")
            print("They yank you out at gunpoint, theres no second chance for you.")
            alive = False
            pause()

    elif c == "2":
        print("\n You try twisting around them cautious of every step and second move.")
        if random.random() < 0.5:  #
            print("You managed to escape that sticky situation understanding the gravity of your predicament.")
            pause()
        else:
            print("You stepped on a branch, they turn heads then gunfire erupts.")
            if inventory["glock"] and inventory["ammo"] > 0:
                print("You run as fast as you can as gunfire erupts and crackles at the trees around you")
                print("You blind fire over your shoulder and somehow, again, you manage to slip away.")
                inventory["ammo"] -= 1
                if inventory["ammo"] < 0:
                    inventory["ammo"] = 0
                pause()
            else:
                print("Without a weapon, you dont get far.")
                alive = False
                pause()

    else:  # Glock ready
        print("\nYou try hiding and staying low with your gun hoping you had a rifle.")
        print("They talk about moving something to the airstrip before sun down.")
        print("You carefully follow them at a distance, careful to avoid making any noise.")
        pause()
        airstrip_scene()

def airstrip_scene():
    global alive, escaped
    print("\nAfter some time following them you finally reach an airstrip surrounded by the jungle.")
    print("There is a small prop plane with a few trucks surrounded by some men dressed in all black.")
    pause()
    options = {
        "1": "Sneak to the plane once the sun goes down and its dark.",
        "2": "Take the truck and dip.",
    }
    if inventory["glock"] and inventory["ammo"] > 0:  # Only if you have the ammo
        options["3"] = "You shoot a few rounds and run toward the plane."

    c = choice("What are you gonna do?", options)

    if c == "1":
        print("\nYou lay low until night falls.")
        print("The guards relax and fall asleep under the darkness of night.")
        if random.random() < 0.7:  # 70 percent chance
            print("You slip into the cockpit turn the ignition key and takeoff.")
            print("It is rough but you takeoff into the night sky.")
            escaped = True
        else:
            print("A guard is awakened from your noise and sees you sneaking into the plane")
            print("Shouts and gunfire erupts ending your escape before it even started.")
            alive = False
        pause()

    elif c == "2":
        print("\nYou sneak toward a random truck with your heart pounding.")
        if random.random() < 0.5:  # 50 percent
            print("The keys are already in the ignition. You start the truck and floor it down the dirt road.")
            print("Bullets hit the truck. However, you manage to keep going and find a small town.")
            print("You found help Mr. Jeffer's, you escaped!")
            escaped = True
        else:
            print("As you climb into the truck they spot you.")
            print("You freeze, but they don’t.")
            alive = False
        pause()

    else:  # distraction with Glock
        print("\n You fire some shots in the trees away from the plane.")
        inventory["ammo"] -= 3  # shoots 3 bullets
        if inventory["ammo"] < 0:  # straightforward
            inventory["ammo"] = 0  # diminishes ammo reserves
        print("The guards run toward the shots.")
        print("You sprint out of a bush and dive into the plane.")
        if random.random() < 0.6:
            print("Though your hands are shaking, you manage to start the engine and take off.")
            print("The top of the trees scrape the plane and you barely manage to take off.")
            print("You did it. You’re out.")
            escaped = True
        else:
            print("The engine doesn’t start. Cheap plane ig.")
            print("You’re still trying to start it when they drag you out of the cockpit.")
            alive = False
        pause()

def ending():
    print("\nGAME OVER")  # Displays a text once the game is over if applicable 
    if escaped and alive:
        print("You survived the crash Mr. Jeffers!!!!!, the jungle, and the cartel. You made it out!")
    elif not alive and escaped:
        # Shouldn't really happen but just in case
        print("You escaped, but not for long. The jungle always takes its payment Mr. Jeffers.")
    elif not alive:
        print("This is where your story ends. You didnt make it out. I’m sorry Mr. Jeffers")
    else:
        print("You’re still out there in the jungle, fighting to survive…")
    

def main():
    print("JEFFER'S JUNGLE CRASH: A TEXT-BASED ADVENTURE!")
    pause()
    start_scene()  # Shows this text at certain times
    ending()

name = "main"  # allows the code to run with the name "name"
if name == "main":
    main()
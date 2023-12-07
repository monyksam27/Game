import time
from colorama import init, Fore

init(autoreset=True)

class InvalidInputError(Exception):
    pass

class InvalidChoiceError(InvalidInputError):
    pass

def print_slow(text, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.05)
    print()

def introduction():
    Name_of_astronaut = str(input(Fore.LIGHTBLACK_EX + "What is your name, Brave astronaut? (Write your name): "))
    print_slow(
        f"Welcome, astronaut {Name_of_astronaut}! You are stationed on the research outpost Perseus, orbiting Nexus-9.",
        Fore.GREEN
    )
    print_slow(
        "Your mission is to investigate anomalies and manifestations around Nexus-9.",
        Fore.CYAN
    )
    print_slow(
        "Be cautious, as the planet seems to respond to thoughts and memories.",
        Fore.YELLOW
    )
    time.sleep(2)
    print_slow("\nYou wake up in your quarters. It's eerily silent.", Fore.MAGENTA)

def explore_station():
    print(Fore.BLUE + "\nYou decide to explore the research outpost.")  
    print(
        "As you walk down the corridor, you notice a flickering light in the control room.",
        Fore.WHITE
    )
    time.sleep(2)
    print(Fore.BLUE + "\nWhat do you want to do?")
    print("1. Investigate the flickering light.")
    print("2. Go to the observation deck.")

    observation_deck_choice = choice("\nEnter your choice (1/2): ")

    if observation_deck_choice == "1":
        investigate_light()
    elif observation_deck_choice == "2":
        explore_observation_deck()
    else:
        print("Invalid input. Try again.")

def investigate_light():
    print(Fore.BLUE + "\nYou cautiously approach the control room.")
    print("Inside, you see holographic projections swirling around.")
    time.sleep(2)
    print(Fore.BLUE + "\nTwo doors appear in front of you.")
    print("1. Approach the holographic projections.")
    print("2. Check the computer logs.")

    light_option = choice("\nEnter your choice (1/2): ")

    if light_option == "1":
        confrontation()
    elif light_option == "2":
        investigate_computer()
    else:
        print("Invalid input. Try again.")

def investigate_computer():
    print("\nYou access the computer logs and find recordings from the crew.")
    print("The recordings reveal that the crew members were behaving strangely.")
    print("They spoke of seeing visions and hearing mysterious sounds.")
    print("Determined to find the truth, you decide to investigate further.")
    # Continue the game based on the chosen path
    # You can add more story prompts or outcomes here based on player's choices

def explore_observation_deck():
    print(
        "\nYou reach the observation deck and notice two points of interest:"
    )
    print("1. Check the computer.")
    print("2. Check the door at the end of the room.")

    observation_deck_option = choice("\nEnter your choice (1/2): ")

    if observation_deck_option == "1":
        investigate_computer()
    elif observation_deck_option == "2":
        check_door()
    else:
        print("Invalid input. Try again.")

def check_door():
    print("\nYou walk towards the door at the end of the room.")
    print("As you approach, you hear a familiar sound.")
    print("It's a distress signal, possibly from a fellow astronaut.")
    print("What will you do?")
    print("1. Investigate the source of the distress signal.")
    print("2. Return to the observation deck.")

    door_option = choice("\nEnter your choice (1/2): ")

    if door_option == "1":
        print("\nYou decide to investigate the source of the distress signal.")
        # Continue the game based on the chosen path
        # You can add more story prompts or outcomes here based on player's choices
    elif door_option == "2":
        print("\nYou choose to return to the observation deck.")
        # Continue the game based on the chosen path
        # You can add more story prompts or outcomes here based on player's choices
    else:
        print("Invalid input. Try again.")

def confrontation():
    print(Fore.RED + "\nYou feel a sudden surge of memories flooding your mind.")
    print("Strange illusions begin to form around you.")
    time.sleep(2)
    print(Fore.RED + "\nWhat will you do?")
    print("1. Try to confront the illusions.")
    print("2. Attempt to ground yourself and focus on reality.")

    puzzle_text = (
        "As you try to confront the illusions, you question the reality of your memories. "
        "What if everything you remember is a fabrication? "
        "Are you sure you can trust your own thoughts?"
    )
    print_slow(puzzle_text, Fore.WHITE)

    puzzle_choice = choice("\nEnter your choice (1/2): ")

    if puzzle_choice == "1":
        print("\nYou choose to confront the illusions head-on.")
        for _ in range(3):
            print_slow("You find yourself trapped in a time loop of your own imagination...", Fore.YELLOW)
            time.sleep(2)
        print_slow("\nBreaking free from the illusions, you are left disoriented but determined to continue.", Fore.WHITE)
        # Continue the game based on the chosen path
        # You can add more story prompts or outcomes here based on player's choices

    elif puzzle_choice == "2":
        print("\nYou decide to ground yourself and focus on reality.")
        # Continue the game based on the chosen path
        # You can add more story prompts or outcomes here based on player's choices
    else:
        print("Invalid input. Try again.")

def valid_value(prompt):
    while True:
        try:
            value = str(input(prompt)).lower()
            if value not in ['yes', 'no']:
                raise InvalidInputError("Please enter 'yes' or 'no'.")
            return value
        except InvalidInputError as e:
            print(e)

def choice(prompt):
    while True:
        try:
            value = str(input(prompt)).lower()
            if value not in ['1', '2']:
                raise InvalidChoiceError("Please enter '1' or '2'.")
            return value
        except InvalidChoiceError as e:
            print(e)

def main_game():
    introduction()
    explore_station_choice = valid_value("\nDo you want to explore the station? (yes/no): ").lower()
    
    if explore_station_choice == "yes":
        explore_station()
    elif explore_station_choice == "no":
        print("\nYou decide to stay in your quarters.")
    else:
        print("Invalid input. Try again.")

if __name__ == "__main__":
    main_game()
# Import necessary libraries
import time  # Provides time-related functions
from colorama import init, Fore  # Colorama for colored console output

# Initialize colorama for automatic color reset in console
init(autoreset=True)

# Define custom exceptions for invalid input
class InvalidInputError(Exception):
    pass

class InvalidChoiceError(InvalidInputError):
    pass

# Function to print text slowly with optional color
def print_slow(text, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.05)
    print()

# Function to introduce the player to the game
def introduction():
    # Get the astronaut's name as input
    name_of_astronaut = str(input(Fore.LIGHTBLACK_EX + "What is your name, Brave astronaut? (Write your name): "))
    # Display welcome message and mission information
    print_slow(f"Welcome, astronaut {name_of_astronaut}! You are stationed on the research outpost Perseus, orbiting Nexus-9.", Fore.GREEN)
    print_slow("Your mission is to investigate anomalies and manifestations around Nexus-9.", Fore.CYAN)
    print_slow("Be cautious, as the planet seems to respond to thoughts and memories.", Fore.YELLOW)
    time.sleep(2)
    print_slow("\nYou wake up in your quarters. It's eerily silent.", Fore.MAGENTA)

# Function for the player to explore the research outpost
def explore_station():
    print_slow("\nYou decide to explore the research outpost.", Fore.BLUE)
    print_slow("As you walk down the corridor, you notice a flickering light in the control room.", Fore.BLUE)
    time.sleep(2)
    print_slow("\nWhat do you want to do?", Fore.GREEN)
    print("1. Investigate the flickering light.")
    print("2. Go to the observation deck.")

    # Get the player's choice for exploration
    observation_deck_choice = choice("\nEnter your choice (1/2): ")

    # Branch the story based on the player's choice
    if observation_deck_choice == "1":
        investigate_light()
    elif observation_deck_choice == "2":
        explore_observation_deck()
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Function for the player to investigate a flickering light
def investigate_light():
    print_slow("\nYou cautiously approach the control room.", Fore.BLUE)
    print_slow("Inside, you see holographic projections swirling around.", Fore.BLUE)
    time.sleep(2)
    print_slow("\nTwo doors appear in front of you.", Fore.GREEN)
    print("1. Approach the holographic projections.")
    print("2. Check the computer logs.")

    # Get the player's choice for further investigation
    light_option = choice("\nEnter your choice (1/2): ")

    # Branch the story based on the player's choice
    if light_option == "1":
        confrontation()
    elif light_option == "2":
        investigate_computer()
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Function for the player to investigate computer logs
def investigate_computer():
    print_slow("\nYou access the computer logs and find recordings from the crew."
    "The recordings reveal that the crew members were behaving strangely."
    "They spoke of seeing visions and hearing mysterious sounds."
    "Determined to find the truth, you decide to investigate further.", Fore.BLUE)
    # Continue the game based on the chosen path
 

# Function for the player to explore the observation deck
def explore_observation_deck():
    print_slow("\nYou reach the observation deck and notice two points of interest:", Fore.BLUE)
    print("1. Check the computer.")
    print("2. Check the door at the end of the room.")

    # Get the player's choice for observation deck exploration
    observation_deck_option = choice("\nEnter your choice (1/2): ")

    # Branch the story based on the player's choice
    if observation_deck_option == "1":
        investigate_computer()
    elif observation_deck_option == "2":
        check_door()
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Function for the player to check a door in the observation deck
def check_door():
    print_slow("\nYou walk towards the door at the end of the room."
        "As you approach, you hear a familiar sound."
        "It's a distress signal, possibly from a fellow astronaut.", Fore.BLUE)
    print_slow("\n What will you do?", Fore.GREEN)
    print("1. Return to the observation deck.")
    print("2. Follow the sound.")
    print("3. Ignore it.")

    # Get the player's choice for the door action
    door_option = choice_2("\nEnter your choice (1/2/3): ")

    # Branch the story based on the player's choice
    if door_option == "1":
        print("\nYou choose to return to the observation deck.")
        # Continue the game based on the chosen path
      
    elif door_option == "2":
        print("\nYou decide to follow the sound.")
        follow_sound()
    elif door_option == "3":
        print("\nYou choose to ignore the distress signal.")
        # Continue the game based on the chosen path
       
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Function for the player to follow a distress signal
def follow_sound():
    print_slow("\nYou follow the sound, and as you turn a corner, you find yourself in a surreal scene.", Fore.CYAN )
    print_slow("Your late mother appears before you, singing a familiar lullaby and calling your name.", Fore.CYAN )
    time.sleep(2)
    print_slow("\nWhat will you do?", Fore.GREEN)
    print("1. Follow your mother.")
    print("2. Fight the illusion.")

    # Get the player's choice for following the sound
    follow_sound_option = choice("\nEnter your choice (1/2): ")

    # Branch the story based on the player's choice
    if follow_sound_option == "1":
        print(Fore.CYAN + "\nYou choose to follow your mother.")
        # Continue the game based on the chosen path
   
    elif follow_sound_option == "2":
        print(Fore.CYAN + "\nYou choose to fight the illusion.")
        # Continue the game based on the chosen path
   
    else:
        print(Fore.RED + "Invalid input. Try again.")
        
    time.sleep(2)
    print_slow("\nYou experience visions and gain an understanding of your own self."
                      "Unfortunately, now you are trapped in the planet's influence.", Fore.RED)

# Function for the player to confront illusions
def confrontation():
    print_slow("\nYou feel a sudden surge of memories flooding your mind.", Fore.RED)
    print_slow("Strange illusions begin to form around you.", Fore.RED)
    time.sleep(2)
    print_slow("\nWhat will you do?", Fore.GREEN)
    print("1. Try to confront the illusions.")
    print("2. Attempt to ground yourself and focus on reality.")

    puzzle_text = (
        "As you try to confront the illusions, you question the reality of your memories. "
        "What if everything you remember is a fabrication? "
        "Are you sure you can trust your own thoughts?"
    )
    print_slow(puzzle_text, Fore.RED)

    # Get the player's choice for confronting illusions
    puzzle_choice = choice("\nEnter your choice (1/2): ")

    # Branch the story based on the player's choice
    if puzzle_choice == "1":
        for _ in range(3):
            print_slow("You find yourself trapped in a time loop of your own imagination...", Fore.YELLOW)
    elif puzzle_choice == "2":
        print("\nYou decide to ground yourself and focus on reality.")
        # Continue the game based on the chosen path
        
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Function to validate yes/no input
def valid_value(prompt):
    while True:
        try:
            value = str(input(prompt)).lower()
            if value not in ['yes', 'no']:
                raise InvalidInputError("Please enter 'yes' or 'no'.")
            return value
        except InvalidInputError as e:
            print(e)

# Function to validate choices with options '1' or '2'
def choice(prompt):
    while True:
        try:
            value = str(input(prompt)).lower()
            if value not in ['1', '2']:
                raise InvalidChoiceError("Please enter '1' or '2'")
            return value
        except InvalidChoiceError as e:
            print(e)

# Function to validate choices with options '1', '2', or '3'
def choice_2(prompt):
    while True:
        try:
            value = str(input(prompt)).lower()
            if value not in ['1', '2', '3']:
                raise InvalidChoiceError("Please enter '1', '2', '3' ")
            return value
        except InvalidChoiceError as e:
            print(e)

# Main function to start the game
def main_game():
    introduction()
    # Get the player's choice to explore the station or stay in quarters
    explore_station_choice = valid_value("\nDo you want to explore the station? (yes/no): ").lower()
    
    # Branch the story based on the player's choice
    if explore_station_choice == "yes":
        explore_station()
    elif explore_station_choice == "no":
        print("\nYou decide to stay in your quarters.")
    else:
        print(Fore.RED + "Invalid input. Try again.")

# Execute the main game function when the script is run
if __name__ == "__main__":
    main_game()

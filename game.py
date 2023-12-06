import time

def introduction():
    #test
    
    #prompt user to write a name
    print("Welcome, astronaut NAME! You are stationed on the research outpost Perseus, orbiting Nexus-9.")
    print("Your mission is to investigate anomalies and manifestations around Nexus-9.")
    print("Be cautious, as the planet seems to respond to thoughts and memories.")
    time.sleep(2)
    print("\nYou wake up in your quarters. It's eerily silent.")

def explore_station():
    print("\nYou decide to explore the research outpost.")
    print("As you walk down the corridor, you notice a flickering light in the control room.")
    time.sleep(2)
    print("\nWhat do you want to do?")
    print("1. Investigate the flickering light.")
    print("2. Go to the observation deck.")

def investigate_light():
    print("\nYou cautiously approach the control room.")
    print("Inside, you see holographic projections swirling around.")
    time.sleep(2)
    print("\nTwo doors appear in front of you.")
    print("1. Approach the holographic projections.")
    print("2. Check the computer logs.")

def confrontation():
    print("\nYou feel a sudden surge of memories flooding your mind.")
    print("Strange illusions begin to form around you.")
    time.sleep(2)
    print("\nWhat will you do?")
    print("1. Try to confront the illusions.")
    print("2. Attempt to ground yourself and focus on reality.")

def main_game():
    introduction()

    # 1 choice
    explore_station_choice = input("\nDo you want to explore the station? (yes/no): ").lower()
    if explore_station_choice == "yes":
        explore_station()
        station_option = input("\nEnter your choice (1/2): ")
        
# Second choice //the first option
        if station_option == "1":
            investigate_light()
            light_option = input("\nEnter your choice (1/2): ")
            
            # Final choice based on previous options
            if light_option == "1":
                confrontation()
                # Continue game based on the final choice
                # Add more story prompts or outcomes here based on player's choices
            elif light_option == "2":
                print("\nYou access the computer logs and find some intriguing data.")
                # Continue game based on the chosen path
        elif station_option == "2":
            print("\nYou reach the observation deck and witness breathtaking cosmic phenomena.")
            # Continue game based on the chosen path
    else:
        print("\nYou decide to stay in your quarters.")
        # Continue game based on the chosen path

if __name__ == "__main__":
    main_game()

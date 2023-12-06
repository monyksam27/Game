import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def get_user_name():
    name = input("Enter your astronaut name: ")
    return name

def introduction(name):
    print_slow(f"Welcome, astronaut {name}! You are stationed on the research outpost Perseus, orbiting Nexus-9.")
    print_slow("Your mission is to investigate anomalies and manifestations around Nexus-9.")
    print_slow("Be cautious, as the planet seems to respond to thoughts and memories.")
    print_slow("You wake up in your quarters. It's eerily silent.")

# Get user name
user_name = get_user_name()

# Call the introduction function with the user's name
introduction(user_name)

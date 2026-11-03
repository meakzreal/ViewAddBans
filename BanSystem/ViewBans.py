import os
import time

red2 = "\033[31m"
green2 = "\033[32m"
yellow2 = "\033[33m"
blue2 = "\033[34m"
purple2 = "\033[35m"
reset2 = "\033[0m"

def clear_command():
    os.system('cls' if os.name == 'nt' else 'clear')

def in_testing_phase_three():
    print(f"{yellow2}testing{reset2}")
    time.sleep(1)
    return True

def show_ban_lists():
    global file_contents
    with open("banlogs.txt", "r") as file:
        file_contents = file.read()
        print(file_contents)
        input("Press Enter to return to the main menu...")
        return True
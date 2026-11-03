## ==========================================
## Project: Ban Notes
## Author: Meakz
## Purpose: Record and Research Ban information.
## ------------------------------------------
## Version: 1.0
## Created: 03/11/2026
## ==========================================

# Imports
import os
import time
import AddBans
import ViewBans


# Terminal Colours
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
reset = "\033[0m"


# Terminal Functions
def clear_command():
    os.system('cls' if os.name == 'nt' else 'clear')


# Testing Functions
def in_testing_phase():
    print(f"{yellow}testing{reset}")
    time.sleep(1)
    return True


# Main Menu
def start_up_screen():
    global choice_of_screen
    clear_command()

    while True:
        print(f"{purple}=========================================={reset}")
        print(f"{blue}1. Add a Player Ban{reset}")
        print(f"{blue}2. View Player Bans{reset}")
        print(f"{red}3. Exit{reset}")
        print(f"{purple}=========================================={reset}")

        choice_of_screen = input(f"{green}Enter your choice (1-3): {reset}")

        if choice_of_screen == '1':
            AddBans.start_up_screen_bans()
            start_up_screen()

        elif choice_of_screen == '2':
            clear_command()
            ViewBans.show_ban_lists()
            start_up_screen()

        elif choice_of_screen == '3':
            print(f"{red}Exiting the program...{reset}")
            time.sleep(1)
            clear_command()
            exit()

        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)
            clear_command()
            start_up_screen()


# Run Program
start_up_screen()

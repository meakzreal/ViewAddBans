# Imports
import os
import time


# Terminal Colours
red1 = "\033[31m"
green1 = "\033[32m"
yellow1 = "\033[33m"
blue1 = "\033[34m"
purple1 = "\033[35m"
reset1 = "\033[0m"


# Global Variables
name_input = ""
any_notes = ""


# Terminal Functions
def clear_command():
    os.system('cls' if os.name == 'nt' else 'clear')


# Testing Functions
def in_testing_phase_two():
    print(f"{yellow1}testing{reset1}")
    time.sleep(1)
    return True


# Ban Recording Functions
def ask_for_ban():
    global name_input,any_notes
    name_input = input("Player Name: ").strip()
    steam_id_input = input("Steam ID or SPECIAL ID: ").strip()
    any_notes = input("Notes About Player: ").strip()

    with open("banlogs.txt", "a") as file:
        file.write(
            f"\n========== BAN RECORD ==========\n"
            f"Name: {name_input}\n"
            f"Steam ID: {steam_id_input}\n"
            f"Notes: {any_notes}\n"
            f"=====================================\n"
        )
        print("Player Ban Added!")
        return True


# Start Up Functions
def start_up_screen_bans():
    clear_command()
    print(f"{purple1}=========================================={reset1}")
    print(f"{blue1}Loading Player Bans!{reset1}")
    time.sleep(1)
    print(f"{blue1}Player Bans Loaded!{reset1}")
    time.sleep(1)
    clear_command()
    ask_for_ban()

import curses
import json
# Define races and classes with descriptions

with open("spells.json", "r") as file:
    SPELLS = json.load(file)

with open("equipment.json", "r") as file:
    EQUIPMENTS = json.load(file)
RACES = {
    "Human": "Humans are versatile and adaptable known for their ambition and creativity.",

    "Elf": "Elves are graceful and long-lived, with keen senses and a natural affinity for magic.",
    "Dwarf": "Dwarves are sturdy and resilient, known for their craftsmanship and love for the earth.",
    "Halfling": "Halflings are small and nimble, with a natural talent for stealth and a love for comfort.",
    "Dragonborn": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
    "Gnome": "Gnomes are curious and inventive, with a knack for illusions and a strong connection to the earth.",
    "Tiefling": "Tieflings have infernal heritage, granting them unusual abilities and a distinctive appearance.",
}

RACES_TRAIT = {
    "Human": {"Human Variant Trait": "Humans are versatile and adaptable, known for their ambition and creativity.", },
    "Elf": {"High Elf": "Elves are graceful and long-lived, with keen senses and a natural affinity for magic.", },
    "Dwarf": {"Hill Dwarf": "Dwarves are sturdy and resilient, known for their craftsmanship and love for the earth.", },
    "Halfling": {"Lightfoot Halfling": "Halflings are small and nimble, with a natural talent for stealth and a love for comfort.", },
    "Dragonborn": {"DRACONIC ANCESTRY (BLACK)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Blue)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Brass)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Bronze)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Copper)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Gold)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Green)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Red)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (Silver)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon.",
                   "DRACONIC ANCESTRY (White)": "Dragonborn are proud and noble, with draconic ancestry that grants them a breath weapon."},
    "Gnome": {"Rock Gnome": "Gnomes are curious and inventive, with a knack for illusions and a strong connection to the earth.", },
}


CLASSES = {
    "Fighter": "Fighters are skilled warriors who excel in physical combat, using their training and strength.",
    "Wizard": "Wizards are spellcasters who harness arcane power through study and practice.",
    "Rogue": "Rogues are agile and cunning, adept at sneaking, stealing, and exploiting weaknesses.",
    "Cleric": "Clerics are divine spellcasters who serve a higher power and can heal and protect their allies.",
    "Ranger": "Rangers are skilled hunters and trackers, with a deep bond to nature and animal companions.",
    "Paladin": "Paladins are holy warriors who uphold justice and righteousness through divine magic and combat skills.",
    "Bard": "Bards are versatile performers who use their artistic talents to cast spells and inspire their allies.",
}
SEXS = [
    "Male",
    "Female"
]
ABILTY_SCORES = [
    "Standard Array ",
    "Manual/Rolled",
    "Point buy"
]

STARTING_EQUIPMENT = [
    "Equipment",
    "Gold"
]

PROFICIENCIES = [
    "Animal Handling",
    "Athletics",
    "Intimidation",
    "Nature",
    "Perception",
    "Survival",
]

ALIGNEMENT = [
    "Chaotic Evil",
    "Chaotic Good",
    "Chaotic Neutral",
    "Lawful Evil",
    "Lawful Good",
    "Lawful Neutral",
    "Neutral",
    "Neutral Evil",
    "Neutral good",
]


def display_menu(stdscr, choices, title, descriptions):
    current_row = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title)

        # Display the options
        for idx, choice in enumerate(choices):
            if idx == current_row:
                safe_addstr(stdscr, idx + 1, 0,
                            f"> {choice}", True)
            else:
                safe_addstr(stdscr, idx + 1, 0, f"  {choice}", False)

        # Display the description of the selected choice
        if len(descriptions) != 0:
            stdscr.addstr(len(choices) + 2, 0,
                          descriptions[choices[current_row]])

        curses.curs_set(0)
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            # to make sure we dont go out of range
            current_row = (current_row + 1) % len(choices)
        elif key == curses.KEY_UP:
            current_row = (current_row - 1) % len(choices)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return choices[current_row]
        elif key == 27:  # ESC key
            return None


def get_user_input(stdscr, prompt, choices=None):

    if choices:
        return display_menu(stdscr, choices, prompt, descriptions={})
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, prompt)
        curses.echo()
        user_input = stdscr.getstr(1, 0).decode("utf-8").strip()
        curses.noecho()
        return user_input


def safe_addstr(stdscr, y, x, text, inverse: bool):
    max_y, max_x = stdscr.getmaxyx()
    if y < max_y and x < max_x:
        stdscr.addstr(y, x, text[:max_x - x],
                      curses.A_REVERSE if inverse else curses.A_NORMAL)
    else:
        # If y or x is out of bounds, handle the situation
        pass


def search(stdscr, items):
    query = ''
    current_row = 0
    stuff = []
    while True:
        stdscr.clear()

        # Display the current query
        stdscr.addstr(0, 0, f"Search: {query}")

        # Filter and display search results
        filtered_items = [
            item for item in items if query.lower() in item.lower()]
        for idx, choice in enumerate(filtered_items):
            if idx == current_row:
                safe_addstr(stdscr, idx + 1, 0,
                            f"> {choice}", True)
            else:
                safe_addstr(stdscr, idx + 1, 0, f"  {choice}", False)

        stdscr.refresh()

        key = stdscr.getch()

        # Handle different types of input
        if key in (curses.KEY_ENTER, 10, 13):
            stuff.append(filtered_items[current_row])
            choise = display_menu(stdscr, ["Yes", "No"], "Add another ?:", {})
            if choise == "Yes":
                continue
            else:
                return stuff
            # break   Exit on Enter key
            # Handle backspace (127 for most terminals, 8 for some)
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if len(query) > 0:
                # Remove the last character from the query
                query = query[:-1]
        elif key == 27:  # Handle ESC key
            return stuff
        elif 32 <= key <= 126:  # Printable characters
            query += chr(key)
        elif key == curses.KEY_DOWN:
            # to make sure we dont go out of range
            current_row = (current_row + 1) % len(filtered_items)
        elif key == curses.KEY_UP:
            current_row = (current_row - 1) % len(filtered_items)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return filtered_items[current_row]

    # stdscr.clear()
    # stdscr.addstr(0, 0, "Goodbye!")
    # stdscr.refresh()
    # stdscr.getch()


def main(stdscr):

    curses.curs_set(1)
    char_info = []
    # Get character details
    name = get_user_input(stdscr, "Enter your character's Name: ")
    char_info.append(name)
    level = get_user_input(stdscr, "Enter your character's Level: ")

    char_info.append(level)
    # Select Sex
    char_info.append(display_menu(
        stdscr, SEXS, "Select your character's Sex:", {}
    ))

    # Select class and race with descriptions
    char_info.append(display_menu(
        stdscr, list(CLASSES.keys()), "Select your character's Class:", CLASSES
    ))
    char_info.append(display_menu(
        stdscr, list(RACES.keys()), "Select your character's Race:", RACES
    ))
    char_info.append(display_menu(
        stdscr, list(RACES_TRAIT[char_info[4]].keys()
                     ), "Select your character's Race Trait:",
        RACES_TRAIT[char_info[4]]
    ))
    char_info.append(display_menu(
        stdscr, list(ABILTY_SCORES,
                     ), "Select your character's Abiltyscores:",
        {}
    ))
    char_info.append(display_menu(
        stdscr, list(STARTING_EQUIPMENT,
                     ), "Select your character's Starting equipment:",
        {}
    ))
    char_info.append(display_menu(
        stdscr, PROFICIENCIES,
        "Select your )character's Proficiencies:",
        {}
    ))

    char_info.append(display_menu(
        stdscr, ALIGNEMENT,
        "Select your )character's Alignment:",
        {}
    ))

    curses.curs_set(1)

    char_info.append(get_user_input(
        stdscr, "Enter your character's Background: ")
    )
    # Ability Scores
    char_info.append(get_user_input(
        stdscr, "Enter Strength (Ability Score): "))
    char_info.append(get_user_input(
        stdscr, "Enter Dexterity (Ability Score): "))
    char_info.append(get_user_input(
        stdscr, "Enter Constitution (Ability Score): "))
    char_info.append(get_user_input(
        stdscr, "Enter Intelligence (Ability Score): "))
    char_info.append(get_user_input(stdscr, "Enter Wisdom (Ability Score): "))
    char_info.append(get_user_input(
        stdscr, "Enter Charisma (Ability Score): "))

    spells_names = [spell['name'] for spell in SPELLS]

    spells_name = search(stdscr, spells_names)
    char_info.append(spells_name)

    stdscr.clear()
    stdscr.addstr("    Character Info:\n")
    for info in char_info:
        stdscr.addstr(f" {info}\n")

    stdscr.refresh()
    stdscr.getch()

    stdscr.clear()
    stdscr.addstr("  EQUIPMENTS:\n")
    for equipment in EQUIPMENTS:
        stdscr.addstr(f" {equipment}\n")

    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)

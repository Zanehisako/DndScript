import curses

# Define races and classes with descriptions
RACES = {
    "Human": "Humans are versatile and adaptable, known for their ambition and creativity.",
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


def display_menu(stdscr, choices, title, descriptions):
    current_row = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title)

        # Display the options
        for idx, choice in enumerate(choices):
            if idx == current_row:
                stdscr.addstr(idx + 1, 0, f"> {choice}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 1, 0, f"  {choice}")

        # Display the description of the selected choice
        if len(descriptions) != 0:
            stdscr.addstr(len(choices) + 2, 0,
                          descriptions[choices[current_row]])

        curses.curs_set(0)
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
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


def main(stdscr):

    curses.curs_set(1)
    stdscr.clear()

    # Get character details
    name = get_user_input(stdscr, "Enter your character's Name: ")
    level = get_user_input(stdscr, "Enter your character's Level: ")

    # Select Sex
    char_sex = display_menu(
        stdscr, SEXS, "Select your character's Sex:", {}
    )

    # Select class and race with descriptions
    char_class = display_menu(
        stdscr, list(CLASSES.keys()), "Select your character's Class:", CLASSES
    )
    race = display_menu(
        stdscr, list(RACES.keys()), "Select your character's Race:", RACES
    )
    races_trait = display_menu(
        stdscr, list(RACES_TRAIT[race].keys()
                     ), "Select your character's Race Trait:", RACES_TRAIT[race]

    )
    curses.curs_set(1)

    background = get_user_input(stdscr, "Enter your character's Background: ")
    alignment = get_user_input(stdscr, "Enter your character's Alignment: ")

    # Ability Scores
    strength = get_user_input(stdscr, "Enter Strength (Ability Score): ")
    dexterity = get_user_input(stdscr, "Enter Dexterity (Ability Score): ")
    constitution = get_user_input(
        stdscr, "Enter Constitution (Ability Score): ")
    intelligence = get_user_input(
        stdscr, "Enter Intelligence (Ability Score): ")
    wisdom = get_user_input(stdscr, "Enter Wisdom (Ability Score): ")
    charisma = get_user_input(stdscr, "Enter Charisma (Ability Score): ")

    # Create PDF
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)

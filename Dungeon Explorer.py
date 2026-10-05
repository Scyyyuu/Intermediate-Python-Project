"""
Dungeon Escape (text adventure) - starter file
Run with: python dungeon_escape.py

Fill in every TODO. Read the HINT lines only if you get stuck.
Goal of the game: find the key in the dungeon, then unlock the exit door.
"""

import json

SAVE_FILE = "savegame.json"

# The world is a dictionary: room name -> info about that room.
# "exits" maps a direction to the room you reach by going that way.
# TODO (Milestone 3): add at least 3 more rooms of your own, with items and exits.
WORLD = {
    "Cell": {
        "description": "A damp stone cell. A rusty door leads north.",
        "exits": {"north": "Hallway"},
        "items": ["torch"],
    },
    "Hallway": {
        "description": "A long, dark hallway. Doors lead south and east.",
        "exits": {"south": "Cell", "east": "Armory"},
        "items": [],
    },
    "Armory": {
        "description": "Old weapons rust on the walls. A chest sits in the corner.",
        "exits": {"west": "Hallway"},
        "items": ["key"],
    },
}


# ---------- Milestone 1: the player ----------
class Player:
    def __init__(self, start_room="Cell"):
        # TODO: store the current room name and an inventory list (starts empty)
        pass

    def pick_up(self, item):
        """TODO: add the item to the inventory."""
        pass

    def has(self, item):
        """TODO: return True if the item is in the inventory."""
        pass


# ---------- Milestone 2: the game engine ----------
class Game:
    def __init__(self):
        self.player = Player()
        self.world = WORLD  # HINT: later you may want a copy so a new game resets the world
        self.running = True

    def look(self):
        """Print the current room's description, its items, and its exits.
        HINT: self.world[self.player.room] gives you the room dictionary.
        """
        pass

    def move(self, direction):
        """Move the player if there is an exit that way, otherwise print a message.
        TODO: what should happen if the exit leads to a locked door?
        HINT: dict.get(direction) returns None if the key doesn't exist.
        """
        pass

    def take(self, item):
        """Move an item from the room's items list into the player's inventory.
        TODO: handle an item that isn't in the room.
        """
        pass

    def show_inventory(self):
        pass

    def check_win(self):
        """TODO: decide when the player wins.
        HINT: maybe a new room called "Exit" that you can only enter with the key.
        """
        pass

    # ---------- Milestone 4: save and load ----------
    def save(self):
        """Write the player's room, inventory, and the world's items to SAVE_FILE.
        HINT: you must save the world's items too, or picked-up items would reappear.
        """
        pass

    def load(self):
        """Read SAVE_FILE and restore the state. Handle a missing file."""
        pass


# ---------- Milestone 2: reading commands ----------
def parse_command(text):
    """Split what the player typed into (verb, argument).
    Example: "take key" -> ("take", "key"), "look" -> ("look", "")
    HINT: text.strip().lower().split(maxsplit=1)
    """
    pass


def main():
    game = Game()
    print("=== Dungeon Escape ===")
    print("Commands: look, go <direction>, take <item>, inventory, save, load, quit")
    game.look()

    while game.running:
        text = input("\n> ")
        verb, arg = parse_command(text)
        # TODO: call the right Game method for each verb.
        # TODO: print a helpful message for commands you don't understand.
        # TODO: after every command, call game.check_win().
        if verb == "quit":
            game.running = False


if __name__ == "__main__":
    main()
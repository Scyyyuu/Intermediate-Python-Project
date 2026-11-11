import json

SAVE_FILE = "savegame.json"

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


class Player:
    def __init__(self, start_room="Cell"):
        pass

    def pick_up(self, item):
        pass

    def has(self, item):
        pass



class Game:
    def __init__(self):
        self.player = Player()
        self.world = WORLD  
        self.running = True

    def look(self):
        pass

    def move(self, direction):
        pass

    def take(self, item):
        pass

    def show_inventory(self):
        pass

    def check_win(self):
        pass


    def save(self):
        pass

    def load(self):
        pass



def parse_command(text):
    pass


def main():
    game = Game()
    print("=== Dungeon Escape ===")
    print("Commands: look, go <direction>, take <item>, inventory, save, load, quit")
    game.look()

    while game.running:
        text = input("\n> ")
        verb, arg = parse_command(text)
        if verb == "quit":
            game.running = False


if __name__ == "__main__":
    main()

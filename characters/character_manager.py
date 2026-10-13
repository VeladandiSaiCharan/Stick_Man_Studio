class CharacterManager:

    def __init__(self):
        self.characters = {}

    # =========================
    # REGISTER CHARACTER
    # =========================

    def register(self, character):

        name = character.get_name()

        if name in self.characters:
            raise ValueError(
                f"Character '{name}' is already registered."
            )

        self.characters[name] = character

        return character

    # =========================
    # GET CHARACTER
    # =========================

    def get(self, name):

        if name not in self.characters:
            raise KeyError(
                f"Character '{name}' is not registered."
            )

        return self.characters[name]

    # =========================
    # CHECK CHARACTER
    # =========================

    def exists(self, name):

        return name in self.characters

    # =========================
    # GET ALL CHARACTERS
    # =========================

    def get_all(self):

        return list(self.characters.values())

    # =========================
    # GET CHARACTER NAMES
    # =========================

    def get_names(self):

        return list(self.characters.keys())

    # =========================
    # REMOVE CHARACTER
    # =========================

    def remove(self, name):

        if name not in self.characters:
            raise KeyError(
                f"Character '{name}' is not registered."
            )

        return self.characters.pop(name)

    # =========================
    # CHARACTER POSITION
    # =========================

    def move_to(self, name, position):

        character = self.get(name)

        character.move_to(position)

    def shift(self, name, direction):

        character = self.get(name)

        character.shift(direction)

    # =========================
    # CHARACTER ANIMATIONS
    # =========================

    def raise_hand(self, name, side="right"):

        character = self.get(name)

        return character.raise_hand(side=side)

    def point(self, name, side="right"):

        character = self.get(name)

        return character.point(side=side)

    def nod(self, name):

        character = self.get(name)

        return character.nod()
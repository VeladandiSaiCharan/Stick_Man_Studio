from manim import *

from characters.midoriya import Midoriya
from characters.bakugo import Bakugo
from characters.character_manager import CharacterManager


class CharacterIntegrationTest(Scene):

    def construct(self):

        # =========================
        # CREATE MANAGER
        # =========================

        manager = CharacterManager()

        # =========================
        # CREATE AND REGISTER
        # =========================

        midoriya = Midoriya()
        bakugo = Bakugo()

        manager.register(midoriya)
        manager.register(bakugo)

        # =========================
        # POSITION CHARACTERS
        # =========================

        manager.move_to(
            "Midoriya",
            LEFT * 2.5
        )

        manager.move_to(
            "Bakugo",
            RIGHT * 2.5
        )

        manager.get("Bakugo").scale(0.9)

        # =========================
        # DISPLAY CHARACTERS
        # =========================

        self.play(
            Create(manager.get("Midoriya").get_group()),
            Create(manager.get("Bakugo").get_group())
        )

        self.wait(1)

        # =========================
        # MIDORIYA RAISES HAND
        # =========================

        self.play(
            manager.raise_hand("Midoriya"),
            run_time=0.8
        )

        self.wait(0.5)

        # =========================
        # BAKUGO RAISES HAND
        # =========================

        self.play(
            manager.raise_hand("Bakugo"),
            run_time=0.8
        )

        self.wait(0.5)

        # =========================
        # MIDORIYA NODS
        # =========================

        self.play(
            manager.nod("Midoriya"),
            run_time=0.4
        )

        self.wait(1)

        # =========================
        # MOVE BAKUGO
        # =========================

        self.play(
            manager.get("Bakugo").group.animate.shift(LEFT * 1),
            run_time=1
        )

        self.wait(1)

        # =========================
        # VERIFICATION
        # =========================

        print("\n--- Character Integration Test ---")

        print("Registered characters:", manager.get_names())

        print(
            "Midoriya exists:",
            manager.exists("Midoriya")
        )

        print(
            "Bakugo exists:",
            manager.exists("Bakugo")
        )

        print(
            "Midoriya parts:",
            len(manager.get("Midoriya").get_parts())
        )

        print(
            "Bakugo parts:",
            len(manager.get("Bakugo").get_parts())
        )

        print("Character integration successful!")

        self.wait(2)
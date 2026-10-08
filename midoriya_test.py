from manim import *
from characters.midoriya import Midoriya


class MidoriyaTest(Scene):

    def construct(self):

        midoriya = Midoriya()

        self.play(
            Create(midoriya.get_group())
        )

        self.wait(2)

        print(
            "Character:",
            midoriya.get_name()
        )

        print(
            "Parts:",
            len(midoriya.get_parts())
        )

        self.wait(2)
from manim import *

from characters.midoriya import Midoriya
from characters.bakugo import Bakugo


class CharacterTest(Scene):

    def construct(self):

        # Create characters

        midoriya = Midoriya()
        bakugo = Bakugo()


        # Position characters

        midoriya.move_to(LEFT * 2.5)
        bakugo.move_to(RIGHT * 2.5)


        # Make Bakugo slightly smaller

        bakugo.scale(0.9)


        # Show characters

        self.play(
            Create(midoriya.get_group()),
            Create(bakugo.get_group())
        )

        self.wait(2)


        # Print information

        print("Character 1:", midoriya.get_name())
        print("Character 1 Parts:", len(midoriya.get_parts()))

        print("Character 2:", bakugo.get_name())
        print("Character 2 Parts:", len(bakugo.get_parts()))

        self.wait(2)
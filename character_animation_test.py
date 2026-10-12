from manim import *

from characters.midoriya import Midoriya
from characters.bakugo import Bakugo


class CharacterAnimationTest(Scene):

    def construct(self):

        # =========================
        # CREATE CHARACTERS
        # =========================

        midoriya = Midoriya()
        bakugo = Bakugo()

        midoriya.move_to(LEFT * 2.5)
        bakugo.move_to(RIGHT * 2.5)

        bakugo.scale(0.9)

        # =========================
        # INTRODUCE CHARACTERS
        # =========================

        self.play(
            Create(midoriya.get_group()),
            Create(bakugo.get_group())
        )

        self.wait(1)

        # =========================
        # MIDORIYA RAISES HAND
        # =========================

        self.play(
            midoriya.raise_hand(),
            run_time=0.8
        )

        self.wait(0.5)

        # =========================
        # MIDORIYA POINTS
        # =========================

        self.play(
            midoriya.point(),
            run_time=0.8
        )

        self.wait(0.5)

        # =========================
        # MIDORIYA NODS
        # =========================

        self.play(
            midoriya.nod(),
            run_time=0.4
        )

        self.wait(0.5)

        # =========================
        # BAKUGO RAISES HAND
        # =========================

        self.play(
            bakugo.raise_hand(),
            run_time=0.8
        )

        self.wait(0.5)

        # =========================
        # MOVE BAKUGO
        # =========================

        self.play(
            bakugo.group.animate.shift(LEFT * 1),
            run_time=1
        )

        self.wait(2)

        # =========================
        # VERIFICATION
        # =========================

        print("Midoriya:", midoriya.get_name())
        print("Bakugo:", bakugo.get_name())
        print("Character animation test completed.")
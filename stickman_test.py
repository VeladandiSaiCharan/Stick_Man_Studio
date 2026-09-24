from manim import *
from characters.stickman import StickMan


class StickManTest(Scene):

    def construct(self):

        stickman = StickMan()

        # Create the StickMan
        self.play(
            *[
                Create(part.object)
                for part in stickman.get_parts()
            ]
        )

        self.wait(1)

        # Raise right arm
        self.play(
            stickman.animate_raise_right_arm()
        )

        self.wait(1)

        # Lower right arm
        self.play(
            stickman.animate_lower_right_arm()
        )

        self.wait(1)

        #Points right arm 
        self.play(
            stickman.animate_point_right()
        )

        self.wait(2)
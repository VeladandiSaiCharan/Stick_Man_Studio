from manim import *
from characters.stickman import StickMan


class StickManTest(Scene):

    def construct(self):

        stickman = StickMan()

        #Puts stickman on the left
        stickman.shift(LEFT * 4)

        #Create the stickman
        self.play(
            *[
                Create(part.object)
                for part in stickman.get_parts()
            ]
        )

        self.wait(1)

        #Move stickman towards center
        self.play(
            *stickman.animate_shift(RIGHT * 4)
        )

        self.wait(2)

        self.play(
            stickman.right_arm.object.animate.rotate(
                PI / 4,
                about_point=stickman.right_arm.object.get_start()
            )
        )

        self.wait(2)
from manim import *
from characters.stickman import StickMan


class StickManTest(Scene):

    def construct(self):

        stickman = StickMan()

        for part in stickman.get_parts():
            self.play(Create(part.object))

        self.wait(1)

        #Moves the stickman to the left 
        self.play(
            *[
                part.object.animate.shift(LEFT * 2)
                for part in stickman.get_parts()
            ]
        )

        self.wait(1)

        #Moves the stickman to right
        self.play(
            *[
                part.object.animate.shift(RIGHT * 4)
                for part in stickman.get_parts()
            ]
        )

        self.wait(2)
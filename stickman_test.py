from manim import *
from characters.stickman import StickMan


class StickManTest(Scene):

    def construct(self):

        stickman = StickMan()

        for part in stickman.get_parts():
            self.play(Create(part.object))

        self.wait(2)
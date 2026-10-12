from manim import (
    ORANGE,
    Circle,
    Line,
    VGroup,
    UP,
)

from characters.character import Character


class Bakugo(Character):

    def __init__(self):
        super().__init__("Bakugo")
        self._create_character()

    def _create_character(self):

        # =========================
        # HEAD
        # =========================

        self.head = Circle(
            radius=0.45,
            color=ORANGE,
            stroke_width=4
        )

        self.head.shift(UP * 0.55)


        # =========================
        # BODY
        # =========================

        self.body = Line(
            start=(0, 0, 0),
            end=(0, -1.35, 0),
            color=ORANGE,
            stroke_width=4
        )


        # =========================
        # ARMS
        # =========================

        self.left_arm = Line(
            start=(0, -0.35, 0),
            end=(-0.75, -0.95, 0),
            color=ORANGE,
            stroke_width=4
        )

        self.right_arm = Line(
            start=(0, -0.35, 0),
            end=(0.75, -0.95, 0),
            color=ORANGE,
            stroke_width=4
        )


        # =========================
        # LEGS
        # =========================

        self.left_leg = Line(
            start=(0, -1.35, 0),
            end=(-0.65, -2.2, 0),
            color=ORANGE,
            stroke_width=4
        )

        self.right_leg = Line(
            start=(0, -1.35, 0),
            end=(0.65, -2.2, 0),
            color=ORANGE,
            stroke_width=4
        )


        # =========================
        # COMPLETE CHARACTER
        # =========================

        self.group = VGroup(
            self.head,
            self.body,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg
        )


    # =========================
    # CHARACTER PARTS
    # =========================

    def get_parts(self):

        return [
            self.head,
            self.body,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg
        ]
from manim import (
    BLUE,
    BLACK,
    WHITE,
    Circle,
    Line,
    VGroup,
    UP,
    RIGHT,
)

from characters.character import Character


class Midoriya(Character):

    def __init__(self):
        super().__init__("Midoriya")
        self._create_character()

    def _create_character(self):

        # =========================
        # HEAD
        # =========================

        self.head = Circle(
            radius=0.5,
            color=BLUE,
            stroke_width=4
        )

        self.head.shift(UP * 0.6)


        # =========================
        # BODY
        # =========================

        self.body = Line(
            start=(0, 0, 0),
            end=(0, -1.5, 0),
            color=BLUE,
            stroke_width=4
        )


        # =========================
        # ARMS
        # =========================

        self.left_arm = Line(
            start=(0, -0.4, 0),
            end=(-0.8, -1.0, 0),
            color=BLUE,
            stroke_width=4
        )

        self.right_arm = Line(
            start=(0, -0.4, 0),
            end=(0.8, -1.0, 0),
            color=BLUE,
            stroke_width=4
        )


        # =========================
        # LEGS
        # =========================

        self.left_leg = Line(
            start=(0, -1.5, 0),
            end=(-0.7, -2.4, 0),
            color=BLUE,
            stroke_width=4
        )

        self.right_leg = Line(
            start=(0, -1.5, 0),
            end=(0.7, -2.4, 0),
            color=BLUE,
            stroke_width=4
        )


        # =========================
        # SPECTACLES
        # =========================

        self.left_glass = Circle(
            radius=0.16,
            color=BLACK,
            fill_color = WHITE,
            fill_opacity = 1,
            stroke_width=2
        )

        self.right_glass = Circle(
            radius=0.16,
            color=BLACK,
            fill_color = WHITE,
            fill_opacity = 1,
            stroke_width=2
        )

        self.left_glass.move_to(
            self.head.get_center() + (-0.18 * RIGHT)
        )

        self.right_glass.move_to(
            self.head.get_center() + (0.18 * RIGHT)
        )


        # Glasses bridge

        self.bridge = Line(
            start=self.head.get_center() + (-0.03 * RIGHT),
            end=self.head.get_center() + (0.03 * RIGHT),
            color=BLACK,
            stroke_width=2
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
            self.right_leg,
            self.left_glass,
            self.right_glass,
            self.bridge
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
            self.right_leg,
            self.left_glass,
            self.right_glass,
            self.bridge
        ]
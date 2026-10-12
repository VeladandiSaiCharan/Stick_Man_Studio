from manim import VGroup, PI

class Character:
    def __init__(self, name):
        self.name = name
        self.group = VGroup()

        #Basic Character methods
    def get_group(self):
        return self.group

    def get_name(self):
        return self.name

    def get_parts(self):
        return list(self.group)

    def move_to(self, position):
        self.group.move_to(position)

    def shift(self, direction):
        self.group.shift(direction)

    def scale(self, factor):
        self.group.scale(factor)

    #Character Animations

    def raise_hand(self, side="right", angle=PI / 3):

        if side == "right":
            arm = self.right_arm
        elif side == "left":
            arm = self.left_arm
        else:
            raise ValueError(
                "side must be 'left' or 'right'."
            )

        return arm.animate.rotate(
            angle,
            about_point=arm.get_start()
        )

    def point(self, side="right", angle=-PI / 4):

        if side == "right":
            arm = self.right_arm
        elif side == "left":
            arm = self.left_arm
        else:
            raise ValueError(
                "side must be 'left' or 'right'."
            )

        return arm.animate.rotate(
            angle,
            about_point=arm.get_start()
        )

    def nod(self, distance=0.12):

        return self.head.animate.shift(
            (0, -distance, 0)
        )
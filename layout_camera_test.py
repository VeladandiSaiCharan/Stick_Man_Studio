from manim import *
from renderer import primitives
from renderer.layout import Layout


class LayoutCameraTest(MovingCameraScene):

    def construct(self):

        # --------------------------------
        # YouTube 16:9 format
        # --------------------------------

        youtube_format = Layout.get_format("youtube")

        print("Video Format:", youtube_format["name"])
        print("Aspect Ratio:", youtube_format["aspect_ratio"])

        circle = primitives.Circle(radius=0.7)
        rectangle = primitives.Rectangle(
            width=2,
            height=1
        )
        text = primitives.Text("StickMan Studio")

        # Position objects
        Layout.place(
            circle,
            Layout.left()
        )

        Layout.place(
            rectangle,
            Layout.right()
        )

        Layout.place(
            text,
            Layout.top()
        )

        # Create objects
        self.play(Create(circle.object))
        self.play(Create(rectangle.object))
        self.play(Write(text.object))

        self.wait(1)

        # --------------------------------
        # Camera movement
        # --------------------------------

        camera = self.camera.frame

        self.play(
            camera.animate.shift(RIGHT * 2)
        )

        self.wait(1)

        # --------------------------------
        # Camera zoom
        # --------------------------------

        self.play(
            camera.animate.scale(0.6)
        )

        self.wait(2)

        # --------------------------------
        # Remove objects
        # --------------------------------

        self.play(
            FadeOut(circle.object),
            FadeOut(rectangle.object),
            FadeOut(text.object)
        )

        self.wait(1)

        # --------------------------------
        # Test 9:16 format
        # --------------------------------

        short_format = Layout.get_format("short")

        print("Video Format:", short_format["name"])
        print("Aspect Ratio:", short_format["aspect_ratio"])

        short_text = primitives.Text(
            "9:16 Short"
        )

        self.play(
            Write(short_text.object)
        )

        self.wait(2)

        self.play(
            FadeOut(short_text.object)
        )

        self.wait(1)
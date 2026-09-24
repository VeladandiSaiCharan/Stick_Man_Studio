from manim import *
from scenes.scene import Scene as StudioScene
from characters.stickman import StickMan
from renderer import primitives


class SceneCompositionTest(Scene):

    def construct(self):

        # Create StickMan Studio scene
        studio_scene = StudioScene("Introduction")

        # Create StickMan
        stickman = StickMan()

        # Create title
        title = primitives.Text("StickMan Studio")

        # Create circle
        circle = primitives.Circle(radius=0.6)

        # Add objects to Studio scene
        studio_scene.add_object(stickman)
        studio_scene.add_object(title)
        studio_scene.add_object(circle)

        # Position objects
        title.object.shift(UP * 2.5)
        circle.object.shift(RIGHT * 3)

        # Display StickMan
        self.play(
            *[
                Create(part.object)
                for part in stickman.get_parts()
            ]
        )

        # Display title
        self.play(
            Write(title.object)
        )

        # Display circle
        self.play(
            Create(circle.object)
        )

        self.wait(2)

        # Move StickMan and circle together
        self.play(
            *stickman.animate_shift(LEFT * 2),
            circle.object.animate.shift(LEFT * 2)
        )

        self.wait(2)
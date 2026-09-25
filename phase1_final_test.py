from manim import *
from scenes.scene import Scene as StudioScene
from characters.stickman import StickMan
from renderer import primitives
from renderer import animations
from renderer.layout import Layout
from renderer.camera import CameraController

class Phase1FinalTest(MovingCameraScene):

    def construct(self):

        #1. Create Scene
        studio_scene = StudioScene("Phase 1 Final Scene")

        #2. Define Characters and objects in Scene
        stickman = StickMan()

        title = primitives.Text("StickMan Studio")
        circle = primitives.Circle(radius=0.6)
        rectangle = primitives.Rectangle(
            width=2.5,
            height=1.2
        )

        #3. Add above objects to Studio Scene

        studio_scene.add_object(stickman)
        studio_scene.add_object(title)
        studio_scene.add_object(circle)
        studio_scene.add_object(rectangle)

        #4. Use Layout system to arrange objects in the scene

        Layout.place(title, Layout.top())
        Layout.place(circle, Layout.right())
        Layout.place(rectangle, Layout.bottom_left())

        stickman.shift(LEFT * 4)

        #5. Display Scene Information

        print("\n========== StickMan Studio Phase 1 ==========")
        print("Scene:", studio_scene)
        print("Objects:", len(studio_scene.get_objects()))
        print("Video Format:", Layout.format_name("youtube"))
        print("Aspect Ratio:", Layout.get_format("youtube")["aspect_ratio"])
        print("=============================================\n")

        #6. Create visual elements

        self.play(
            animations.write(title)
        )

        self.play(
            animations.create(circle),
            animations.create(rectangle)
        )

        self.play(
            *[
                animations.create(part)
                for part in stickman.get_parts()
            ]
        )

        #7. Animate stickman entering the Scene

        self.play(
            *stickman.animate_shift(RIGHT * 4)
        )

        self.wait(2)

        #8. Animate actions of Stickman

        self.play(
            stickman.animate_raise_right_arm()
        )

        self.wait(0.5)

        self.play(
            stickman.animate_point_right()
        )

        self.wait(0.5)

        self.play(
            stickman.animate_head_nod()
        )

        self.wait(1)

        #9. Animate remaining scene objects

        self.play(
            animations.move(
                circle,
                LEFT * 1.5
            ),
            animations.scale(
                rectangle,
                1.2
            )
        )

        self.wait(1)

        #10. Control the camera

        camera = CameraController(self)

        camera.animate_shift(RIGHT * 1)

        self.wait(1)

        camera.animate_zoom(0.8)

        self.wait(2)

        #11. Finish Scene 

        self.play(
            animations.fade_out(stickman.head),
            animations.fade_out(stickman.body),
            animations.fade_out(stickman.left_arm),
            animations.fade_out(stickman.right_arm),
            animations.fade_out(stickman.left_leg),
            animations.fade_out(stickman.right_leg),
            animations.fade_out(title),
            animations.fade_out(circle),
            animations.fade_out(rectangle)
        )

        self.wait(1)
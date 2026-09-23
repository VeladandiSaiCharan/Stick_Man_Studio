from manim import *


class CameraController:
    """Controls the camera for StickMan Studio."""

    def __init__(self, scene):
        self.scene = scene
        self.camera = scene.camera
        self.frame = self.camera.frame

    def move_to(self, position):
        self.frame.move_to(position)

    def shift(self, direction):
        self.frame.shift(direction)

    def zoom(self, factor):
        self.frame.scale(factor)

    def animate_move_to(self, position):
        self.scene.play(
            self.frame.animate.move_to(position)
        )

    def animate_shift(self, direction):
        self.scene.play(
            self.frame.animate.shift(direction)
        )

    def animate_zoom(self, factor):
        self.scene.play(
            self.frame.animate.scale(factor)
        )
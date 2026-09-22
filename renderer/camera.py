from manim import *


class CameraController:
    """Controls the Manim camera for StickMan Studio."""

    def __init__(self, scene):
        self.scene = scene
        self.camera = scene.camera

    def move_to(self, position):
        self.camera.frame.move_to(position)

    def shift(self, direction):
        self.camera.frame.shift(direction)

    def zoom(self, factor):
        self.camera.frame.scale(factor)
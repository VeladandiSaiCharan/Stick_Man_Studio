from manim import Scene as ManimScene


class Renderer(ManimScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_object(self, obj):
        self.add(obj.object)

    def remove_object(self, obj):
        self.remove(obj.object)

    def play_animation(self, animation):
        self.play(animation)
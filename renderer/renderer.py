from manim import Scene as ManimScene
from manim import Create
class Renderer(ManimScene):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)\

    def add_object(self, obj):
        self.add(obj.object)

    def remove_object(self, obj):
        self.remove(obj.object)

    def animate_create(self, obj):
        self.play(Create(obj.object))
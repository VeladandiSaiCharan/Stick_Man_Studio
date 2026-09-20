from .scene import Scene


class SceneManager:
    def __init__(self):
        self.scenes = []

    def add_scene(self, scene):
        self.scenes.append(scene)

    def get_scene(self, name):
        for scene in self.scenes:
            if scene.name == name:
                return scene

        return None

    def get_all_scenes(self):
        return self.scenes

    def __repr__(self):
        return f"SceneManager(scenes={len(self.scenes)})"
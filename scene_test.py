from scenes.scene import Scene
from scenes.scene_manager import SceneManager


manager = SceneManager()

intro = Scene("Introduction")
intro.add_action("Show title")
intro.add_action("Midoriya enters")
intro.add_action("Midoriya speaks")

problem = Scene("Problem")
problem.add_action("Show problem")
problem.add_action("Show array")

manager.add_scene(intro)
manager.add_scene(problem)


print(manager)

for scene in manager.get_all_scenes():
    print(scene)
    print("Actions:")

    for action in scene.get_actions():
        print(" -", action)
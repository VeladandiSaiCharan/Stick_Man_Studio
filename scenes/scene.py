class Scene:
    def __init__(self, name):
        self.name = name
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        return self.actions

    def __repr__(self):
        return f"Scene(name='{self.name}', actions={len(self.actions)})"
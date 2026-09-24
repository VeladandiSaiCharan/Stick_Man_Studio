class Scene:
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.objects = []

    def add_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        return self.actions

    def add_object(self, obj):
        self.objects.append(obj)\

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)

    def get_objects(self):
        return self.objects

    def __repr__(self):
        return (
            f"Scene(name='{self.name}', "
            f"objects={len(self.objects)}, "
            f"actions={len(self.actions)})"
        )
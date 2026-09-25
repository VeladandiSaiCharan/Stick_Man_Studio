from scenes.scene import Scene
from characters.stickman import StickMan
from renderer import primitives


# Create a Studio Scene
scene = Scene("Test Scene")

# Create objects
stickman = StickMan()
circle = primitives.Circle(radius=0.5)
text = primitives.Text("Test Scene")

# Add objects
scene.add_object(stickman)
scene.add_object(circle)
scene.add_object(text)

print("Scene:", scene)
print("Objects in scene:", len(scene.get_objects()))

# Remove the circle
scene.remove_object(circle)

print("After removing circle:")
print("Objects in scene:", len(scene.get_objects()))

# Print remaining objects
for obj in scene.get_objects():
    print("-", type(obj).__name__)
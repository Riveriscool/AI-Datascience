from World import World
from Cube import Cube
from Sphere import Sphere



Earth = World(9.8)

box1 = Cube((3,3,3),4,4)
box1.apply_gravity()
box2 = Cube((3,3,3),6,2)
Earth.add(box1.attributes())
Earth.add(box2.attributes)
Earth.Run(5)
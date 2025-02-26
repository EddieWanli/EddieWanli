import random
def gen_world(self):
    heightmap = []
    for y in range(20):
        heightmap.append(random.randint(1,5))
    for x in range(len(heightmap)):

import pygame
import random
def gen_world():
    locked_pos = []
    for x in range(0, 1000, 50):
        for y in range(500, 750, 50):
            offset_x = random.randint(0,20)
            offset_y = random.randint(0,20)
            x = random.randint(0, 1000)
            y = random.randint(0, 750)
            block_pos = (x + offset_x,y + offset_y)
            locked_pos.append(block_pos)
    return locked_pos




import pygame
import random
def gen_world(y):
    locked_pos = []
    for x in range(-5, 1000, 45):
        block_pos = (x,y)
        locked_pos.append(block_pos)
    return locked_pos








import pygame
import random
def gen_world():
    locked_pos = []
    for x in range(0, 1000, 45):
        y=600
        block_pos = (x,y)
        locked_pos.append(block_pos)
    return locked_pos

def ground(player_y, rect):
    return player_y.collidepoint(rect)






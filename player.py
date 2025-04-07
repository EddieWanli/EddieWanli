import pygame, random

# Animation variables
current_frame = 0
last_update = pygame.time.get_ticks()

# Sprite animation function
def animate_sprite(animation_list, animation_speed):
    global current_frame, last_update
    now = pygame.time.get_ticks()


    if now - last_update > 100:
        current_frame += animation_speed
        last_update = now

    # Loop animation
    if current_frame >= len(animation_list):
        current_frame = 0

    return animation_list[int(current_frame)]




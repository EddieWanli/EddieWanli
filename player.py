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

def draw_health_bar(screen, x, y, health, max_health):
    # background
    pygame.draw.rect(screen, "red", (x, y, 200, 25))

    # health amount
    health_ratio = health / max_health
    pygame.draw.rect(screen, "green", (x, y, 200 * health_ratio, 25))

    # border
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 200, 25), 2)


def attack_hitbox(player_rect, attack_sprite):
    attack_rect = pygame.Rect(player_rect.x + 20, player_rect.y, attack_sprite.get_width(), attack_sprite.get_height())
    return attack_rect


def check_attack_collision(attack_rect, enemy_rects):
    for i, enemy_rect in enumerate(enemy_rects):
        if attack_rect.colliderect(enemy_rect):
            return i
    return -1












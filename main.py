# initialize useful modules
import sys
from button import Button
from player import *
from terrain import *

pygame.init()

# create game window
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Terraworld")

# clock controls
timer = pygame.time.Clock()

# game text
font = pygame.font.Font("assets/retro.ttf", 50)
font2 = pygame.font.Font(None, 35)
font3 = pygame.font.Font(None, 20)
title_text = font.render("TERRAWORLD", True, "black")
title_text_rect = title_text.get_rect(midbottom=(500, 100))
back_to_menu = font2.render("Esc - Main Menu", True, "black")
author = font2.render("By Eddie Wanli", True, "black")
author_pos = author.get_rect(center=(900, 725))

#tutorial
move_left_text = font3.render("A - move left", True, "black")
move_right_text = font3.render("D - move right" , True, "black")
jump_text = font3.render("W/SPACE - Jump" , True, "black")
run_text = font3.render("Shift + A/D  - Run" , True, "black")
defend_text = font3.render("RMB + A/D  - Defend", True, "black")
attack_text = font3.render("LMB - Attack" , True, "black")


#world assets
grass = pygame.image.load("assets/grass.jpg.")
dirt = pygame.image.load("assets/dirt.jpeg.")
sun = pygame.image.load("assets/sun 2.webp")
cloud = pygame.image.load("assets/cloud 2.webp")
background = pygame.image.load("assets/mario background.webp")
apple = pygame.image.load("assets/player sprites/apple.png").convert_alpha()

#transformed world assets
new_grass = pygame.transform.scale(grass, (50,50), )
new_dirt = pygame.transform.scale(dirt, (50,50), )
new_sun = pygame.transform.scale(sun, (200, 200), )
new_cloud = pygame.transform.scale(cloud, (200,200), )
new_background = pygame.transform.scale(background, (1000,750), )

#player assets
walk1 = pygame.image.load("assets/player sprites/walk 1.png")
walk2 = pygame.image.load("assets/player sprites/walk 2.png")
walk3 = pygame.image.load("assets/player sprites/walk 3.png")
walk4 = pygame.image.load("assets/player sprites/walk 4.png")
walk5 = pygame.image.load("assets/player sprites/walk 5.png")
walk6 = pygame.image.load("assets/player sprites/walk 6.png")
walk7 = pygame.image.load("assets/player sprites/walk 7.png")
walk8 = pygame.image.load("assets/player sprites/walk 8.png")

run1 = pygame.image.load("assets/player sprites/run 1.png")
run2 = pygame.image.load("assets/player sprites/run 2.png")
run3 = pygame.image.load("assets/player sprites/run 3.png")
run4 = pygame.image.load("assets/player sprites/run 4.png")
run5 = pygame.image.load("assets/player sprites/run 5.png")
run6 = pygame.image.load("assets/player sprites/run 6.png")
run7 = pygame.image.load("assets/player sprites/run 7.png")

attack1 = pygame.image.load("assets/player sprites/attack 1.png")
attack2 = pygame.image.load("assets/player sprites/attack 2.png")
attack3 = pygame.image.load("assets/player sprites/attack 3.png")
attack4 = pygame.image.load("assets/player sprites/attack 4.png")
attack5 = pygame.image.load("assets/player sprites/attack 5.png")

dead1 = pygame.image.load("assets/player sprites/dead 1.png")
dead2 = pygame.image.load("assets/player sprites/dead 2.png")
dead3 = pygame.image.load("assets/player sprites/dead 3.png")
dead4 = pygame.image.load("assets/player sprites/dead 4.png")
dead5 = pygame.image.load("assets/player sprites/dead 5.png")

defend = pygame.image.load("assets/player sprites/defend.png")

hurt1 = pygame.image.load("assets/player sprites/hurt 1.png")
hurt2 = pygame.image.load("assets/player sprites/hurt 2.png")

#enemy

enemy_idle = pygame.image.load("assets/enemy sprites/Idle.png")

#sprites
new_walk1 = pygame.transform.scale(walk1,(40,80))
new_walk2 = pygame.transform.scale(walk2,(40,80))
new_walk3 = pygame.transform.scale(walk3,(40,80))
new_walk4 = pygame.transform.scale(walk4,(40,80))
new_walk5 = pygame.transform.scale(walk5,(40,80))
new_walk6 = pygame.transform.scale(walk6,(40,80))
new_walk7 = pygame.transform.scale(walk7,(40,80))
new_walk8 = pygame.transform.scale(walk8,(40,80))
walk_list = [new_walk1, new_walk2, new_walk3, new_walk4, new_walk5, new_walk6, new_walk7, new_walk8]

new_run1 = pygame.transform.scale(run1, (40, 80))
new_run2 = pygame.transform.scale(run2, (40, 80))
new_run3 = pygame.transform.scale(run3, (40, 80))
new_run4 = pygame.transform.scale(run4, (40, 80))
new_run5 = pygame.transform.scale(run5, (40, 80))
new_run6 = pygame.transform.scale(run6, (40, 80))
new_run7 = pygame.transform.scale(run7, (40, 80))
run_list = [new_run1, new_run2, new_run3, new_run4, new_run5, new_run6, new_run7]

new_attack1 = pygame.transform.scale(attack1, (40,80))
new_attack2 = pygame.transform.scale(attack2, (40,80))
new_attack3 = pygame.transform.scale(attack3, (40,80))
new_attack4 = pygame.transform.scale(attack4, (40,80))
new_attack5 = pygame.transform.scale(attack5, (40,80))
attack_list = [new_attack1, new_attack2, new_attack3, new_attack4, new_attack5]

new_dead1 = pygame.transform.scale(dead1, (40,80))
new_dead2 = pygame.transform.scale(dead2, (40,80))
new_dead3 = pygame.transform.scale(dead3, (40,80))
new_dead4 = pygame.transform.scale(dead4, (40,80))
new_dead5 = pygame.transform.scale(dead5, (40,80))
dead_list = [new_dead1, new_dead2, new_dead3, new_dead4, new_dead5]

new_defend = pygame.transform.scale(defend, (40,80))
defend_list = [new_defend]

new_hurt = pygame.transform.scale(hurt1, (40,80))
new_hurt2 = pygame.transform.scale(hurt2, (40,80))
hurt_list = [new_hurt, new_hurt2]

new_enemy_idle = pygame.transform.scale(enemy_idle, (60,80))

#enemy
enemy_sprite = new_enemy_idle
enemy_rect = enemy_sprite.get_rect()

#player
player_idle = pygame.image.load("assets/player Idle.png").convert_alpha()
new_player_idle = pygame.transform.scale(player_idle, (40, 80))
player_sprite = new_player_idle
player_rect = player_sprite.get_rect(midbottom=(500, 500))
new_apple = pygame.transform.scale(apple, (20,20))
apple_rect = new_apple.get_rect()

#action booleans
pressed_right = False
pressed_left = False
pressed_shift = False
pressed_jump = False
pressed_attack = False
pressed_defend = False

#movement variables
on_ground = False
gravity = 0
x_velocity = 4
x_sprint_velocity = 6
y_velocity = 0

# default game state
game_state = "menu"

# buttons
new_game_button = Button("New Game",412.5,250, font2,  screen, (150,150,150))
progress_button = Button("Progress",412.5,310, font2, screen, (175,175,175))
settings_button = Button("Settings",412.5,370, font2, screen, "light grey")
exit_button = Button("Exit",412.5,450, font2, screen, (250,50,87))


# game loop
while True:
    scroll[0] += (player_rect.x - scroll[0] - 500)/10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_state == "settings" or game_state == "progress":
                        game_state = "menu"
                    elif game_state == "menu":
                        pygame.quit()
                        sys.exit()
                if game_state == "game":

                    if event.key == pygame.K_d:
                        pressed_right = True
                    elif event.key == pygame.K_a:
                        pressed_left = True
                    elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        pressed_jump = True
                    elif event.key == pygame.K_LSHIFT:
                        pressed_shift = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pressed_attack = True
            if event.button == 3:
                pressed_defend = True
                x_velocity = 0
                x_sprint_velocity = 0

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pressed_attack = False
                player_sprite = new_player_idle
            if event.button == 3:
                pressed_defend = False
                x_velocity = 4
                x_sprint_velocity = 6
                if pressed_right:
                    player_sprite = new_player_idle
                if pressed_left:
                    player_sprite = pygame.transform.flip(player_sprite, True, False)

        if event.type == pygame.KEYUP:
            if game_state == "game":
                if event.key == pygame.K_d:
                    pressed_right = False
                    player_sprite = new_player_idle
                if event.key == pygame.K_a:
                    pressed_left = False
                    player_sprite = pygame.transform.flip(new_player_idle, True, False)
                if event.key == pygame.K_LSHIFT:
                    pressed_shift = False
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    pressed_jump = False

        # button click checks
        if game_state == "menu":
            if new_game_button.check_clicked():
                game_state = "game"
            if settings_button.check_clicked():
                game_state = "settings"
            if progress_button.check_clicked():
                game_state = "progress"
            if exit_button.check_clicked():
                pygame.quit()
                sys.exit()

    # game screen rendering
    if game_state == "menu":
        screen.fill("light blue")
        screen.blit( title_text , title_text_rect)
        screen.blit(author, author_pos )
        new_game_button.draw()
        settings_button.draw()
        progress_button.draw()
        exit_button.draw()

    elif game_state == "game":
        # background
        screen.blit(new_background, (0,0))
        screen.blit(new_sun, (695,25))
        screen.blit( move_right_text, ( 870,10))
        screen.blit( move_left_text, ( 870,30))
        screen.blit( jump_text, ( 870,50))
        screen.blit(run_text, ( 870,70))
        screen.blit(defend_text, ( 870,90))
        screen.blit(attack_text, ( 870,110))

        world = draw_tiles(screen, 20)

        # player movement
        if pressed_right:
            if pressed_shift:
                player_rect.x += x_sprint_velocity
                player_sprite = animate_sprite(run_list, 1)
            else:
                player_rect.x += x_velocity
                player_sprite = animate_sprite(walk_list, 1)

        if pressed_left:
            if pressed_shift:
                player_rect.x -= x_sprint_velocity
                temp = animate_sprite(run_list, 1)
                player_sprite = pygame.transform.flip(temp, True, False)
            else:
                player_rect.x -= x_velocity
                temp = animate_sprite(walk_list, 1)
                player_sprite = pygame.transform.flip(temp, True, False)

        if pressed_jump:
            if on_ground:
                y_velocity = - 17
                on_ground = False

        if pressed_defend:
            if pressed_right:
                player_sprite = new_defend
            elif pressed_left:
                player_sprite = pygame.transform.flip(new_defend, True, False)

        if pressed_attack:
            player_sprite = animate_sprite(attack_list, 1)

        if not on_ground:
            y_velocity += 1
        player_rect.y += y_velocity

        # collisions
        rect = pygame.Rect(player_rect.x - scroll[0], player_rect.y, 35, 80)
        on_ground, hit_left, hit_right = handle_collisions(rect, world)

        for tile in world:
            if hit_right:
                pressed_right = False

            if hit_left:
                pressed_left = False

            if on_ground:
                y_velocity = 0

        if player_rect.left < 0:
            player_rect.left = 0

        screen.blit(player_sprite, rect)

    elif game_state == "settings":
        screen.fill("dark grey")
        screen.blit(back_to_menu, (0, 0))

        # add settings logic here

    elif game_state == "progress":
        screen.fill("yellow")
        screen.blit(back_to_menu, (0, 0))
        pygame.draw.rect(screen, "light grey", pygame.Rect(283, 300, 100, 50), 0,5)
        pygame.draw.rect(screen, "black", pygame.Rect(283, 300, 100, 50), 2,5)
        pygame.draw.rect(screen, "light grey", pygame.Rect(616, 300, 100, 50), 0, 5)
        pygame.draw.rect(screen, "black", pygame.Rect(616, 300, 100, 50), 2, 5)
        # add progress logic here

    pygame.display.update()
    timer.tick(60)





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
death_text = font.render("You Died", False, "black")
return_menu_text = font2.render("Esc - Quit game", False, "black")

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

dead = pygame.image.load("assets/player sprites/dead 5.png")
defend = pygame.image.load("assets/player sprites/defend.png")
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

new_dead = pygame.transform.scale(dead, (40,80))
new_defend = pygame.transform.scale(defend, (40,80))
new_enemy_idle = pygame.transform.scale(enemy_idle, (60,80))

#player
player_idle = pygame.image.load("assets/player Idle.png").convert_alpha()
new_player_idle = pygame.transform.scale(player_idle, (40, 80))
player_sprite = new_player_idle
player_rect = player_sprite.get_rect(midbottom=(500, 500))

# health
player_health = 100
max_health = 100

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

#progress
kill_count = 0
start_time = pygame.time.get_ticks()

# default game state
game_state = "menu"

# buttons
new_game_button = Button("New Game",412.5,250, font2,  screen, (150,150,150))
progress_button = Button("Progress",412.5,310, font2, screen, (175,175,175))
settings_button = Button("Settings",412.5,370, font2, screen, "light grey")
exit_button = Button("Exit",412.5,450, font2, screen, (250,50,87))

# apple
new_apple = pygame.transform.scale(apple, (20,20))
apple_positions = [(random.randint(0, 20000), 500) for _ in range(10)]

#enemy
enemy_positions = [(random.randint(0, 20000), 500) for _ in range(10)]
enemy_sprite = pygame.transform.flip(new_enemy_idle, True, False)


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
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

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

        # world generation
        world = draw_tiles(screen, 20)

        #tutorial text
        screen.blit( move_right_text, ( 870,10))
        screen.blit( move_left_text, ( 870,30))
        screen.blit( jump_text, ( 870,50))
        screen.blit(run_text, ( 870,70))
        screen.blit(defend_text, ( 870,90))
        screen.blit(attack_text, ( 870,110))

        #player health UI
        draw_health_bar(screen, 20, 20, player_health, max_health)
        health_text = font3.render(f"{player_health}/{max_health}", True, "black")
        screen.blit(health_text, ( 30,  25))

        #kill count
        kill_count_text = font2.render("Kill Count: " + str(kill_count), True, (255, 255, 255))
        screen.blit(kill_count_text, ( 30, 50))



        #time elapsed
        time_elapsed = pygame.time.get_ticks() - start_time
        seconds_elapsed = time_elapsed // 1000
        time_text = font3.render(f"Time Elapsed: {seconds_elapsed} seconds", True, (255, 255, 255))
        screen.blit(time_text, ( 30, 5))

        #apple handling
        #position
        apple_rects = []
        for pos in apple_positions:
            x, y = pos
            apple_rect = pygame.Rect(x, y, new_apple.get_width(), new_apple.get_height())
            apple_rects.append(apple_rect)
            screen.blit(new_apple, (x - scroll[0], y))

        #collision
        new_apple_positions = []
        for i, rect in enumerate(apple_rects):
            if player_rect.colliderect(rect):
                if player_health < 100:
                    player_health = min(player_health + 25, 100)  # cap at 100
            else:
                new_apple_positions.append(apple_positions[i])

        apple_positions = new_apple_positions


        #enemy handling
        #position
        enemy_rects = []
        for pos in enemy_positions:
            x, y = pos
            enemy_rect = pygame.Rect(x, y, enemy_sprite.get_width(), enemy_sprite.get_height())
            enemy_rects.append(enemy_rect)
            screen.blit(enemy_sprite, (x - scroll[0], y))

        #collision
        new_enemy_positions = []
        for i, rect in enumerate(enemy_rects):
            if player_rect.colliderect(rect):
                player_health = min(player_health - 25, 100)
            else:
                new_enemy_positions.append(enemy_positions[i])

        enemy_positions = new_enemy_positions

        #death handling
        if player_health == 0:
            screen.blit(death_text, (400,350))
            screen.blit(return_menu_text, (425,400))
            player_sprite = new_dead
            pressed_right = False
            pressed_left = False
            pressed_jump = False
            pressed_defend = False
            pressed_attack = False

        # health validation
        if player_health <= 0:
            player_health = 0

        # player movement
        if pressed_right:
            if pressed_shift:
                player_rect.x += x_sprint_velocity
                player_sprite = animate_sprite(run_list, 1)
            else:
                player_rect.x += x_velocity
                player_sprite = animate_sprite(walk_list, 1)

        #movement handling
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
            attack_rect = attack_hitbox(player_rect, new_attack1)
            hit_enemy_index = check_attack_collision(attack_rect, enemy_rects)

            if hit_enemy_index != -1:
                print("Enemy kill!")
                kill_count += 1
                del enemy_positions[hit_enemy_index]
                del enemy_rects[hit_enemy_index]

        if not on_ground:
            y_velocity += 1
        player_rect.y += y_velocity

        if player_rect.left < 0:
            player_rect.left = 0

        # collision handling
        rect = pygame.Rect(player_rect.x - scroll[0], player_rect.y, 35, 80)
        on_ground, hit_left, hit_right = handle_collisions(rect, world)

        for tile in world:
            if hit_right:
                pressed_right = False

            if hit_left:
                pressed_left = False

            if on_ground:
                y_velocity = 0


        # update player on screen
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

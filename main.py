# initialize useful modules
import sys
import pygame
from terrain import gen_tiles
from terrain import tilemap, tile_placer, scroll, chunk_gen
from button import Button
pygame.init()

# create game window
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Terraworld")

# clock controls
fps = 60
timer = pygame.time.Clock()

# game text
font = pygame.font.Font("images/retro.ttf", 50)
font2 = pygame.font.Font(None, 35)
title_text = font.render("TERRAWORLD", True, "black")
title_text_rect = title_text.get_rect(midbottom=(500, 100))
back_to_menu = font2.render("Esc - Main Menu", True, "black")
author = font2.render("By Eddie Wanli", True, "black")
author_pos = author.get_rect(center=(900, 725))

#world assets
grass = pygame.image.load("images/grass.jpg.")
dirt = pygame.image.load("images/dirt.jpeg.")
sun = pygame.image.load("images/sun 2.webp")
cloud = pygame.image.load("images/cloud 2.webp")
background = pygame.image.load("images/mario background.webp")
player_idle = pygame.image.load("images/player Idle.png")

#player assets
run1 = pygame.image.load("images/run 1.png")
run2 = pygame.image.load("images/run 2.png")
run3 = pygame.image.load("images/run 3.png")
run4 = pygame.image.load("images/run 4.png")
run5 = pygame.image.load("images/run 5.png")
run6 = pygame.image.load("images/run 6.png")
run7 = pygame.image.load("images/run 7.png")

#transformed world assets
new_grass = pygame.transform.scale(grass, (50,50), )
new_dirt = pygame.transform.scale(dirt, (50,50), )
new_sun = pygame.transform.scale(sun, (200, 200), )
new_cloud = pygame.transform.scale(cloud, (200,200), )
new_background = pygame.transform.scale(background, (1000,750), )
new_player_idle = pygame.transform.scale(player_idle, (50,80))
new_run1 = pygame.transform.scale(run1, (50,80), )
new_run2 = pygame.transform.scale(run2, (50,75), )
new_run3 = pygame.transform.scale(run3, (50,75), )
new_run4 = pygame.transform.scale(run4, (50,75), )
new_run5 = pygame.transform.scale(run5, (50,75), )
new_run6 = pygame.transform.scale(run6, (50,75), )
new_run7 = pygame.transform.scale(run7, (50,75), )
run_ani = [new_run1, new_run2, new_run3, new_run4, new_run5, new_run6, new_run7]

#movement variables
player_x = 0
player_y = 500
player_sprite = new_player_idle
player_rect = pygame.Rect(player_x, player_y, player_sprite.get_width(), player_sprite.get_height())
pressed_right = False
pressed_left = False
pressed_up = False
pressed_down = False
pressed_shift = False
pressed_jump = False

# default game state
game_state = "menu"

# buttons
new_game_button = Button("New Game",412.5,250, font2,  screen, (150,150,150))
progress_button = Button("Progress",412.5,310, font2, screen, (175,175,175))
settings_button = Button("Settings",412.5,370, font2, screen, "light grey")
exit_button = Button("Exit",412.5,450, font2, screen, (250,50,87))

map2use = tile_placer(tilemap)
chunk_test = chunk_gen(2)
mapuse = tile_placer(chunk_test)

# game loop
while True:
    scroll[0] += (player_x - scroll[0] - 500)/10

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
                    elif event.key == pygame.K_w:
                        pressed_up = True
                    elif event.key == pygame.K_s:
                        pressed_down = True
                    elif event.key == pygame.K_LSHIFT:
                        pressed_shift = True
                        player_sprite = new_run1

        if event.type == pygame.KEYUP:
            if game_state == "game":
                if event.key == pygame.K_d:
                    pressed_right = False
                if event.key == pygame.K_a:
                    pressed_left = False
                if event.key == pygame.K_w:
                    pressed_up = False
                if event.key == pygame.K_s:
                    pressed_down = False
                if event.key == pygame.K_LSHIFT:
                    pressed_shift = False
                    player_sprite = new_player_idle

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
        gen_tiles(screen, mapuse)

        # player movement
        if pressed_left:
            player_x -= 2
        if pressed_right:
            player_x += 2
        if pressed_up:
            player_y -= 2
        if pressed_down:
            player_y += 2
        if pressed_shift:
            if pressed_right:
                player_x += 3.5
            if pressed_left:
                player_x -= 3.5
        if player_x < 0:
            player_x = 0

        screen.blit(player_sprite, (player_x - scroll[0], player_y - scroll[1]))

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
    timer.tick(fps)





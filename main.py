# initialize useful modules
import sys
import pygame
from terrain import gen_world
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

#assets
grass = pygame.image.load("images/e.jpg")
sun = pygame.image.load("images/eyes.png")
cloud = pygame.image.load("images/cloud.png")
new_grass = pygame.transform.scale(grass, (50,50), )
player_idle = pygame.image.load("images/player Idle.png")
player_x = 500
player_y = 500
pressed_right = False
pressed_left = False
pressed_up = False
pressed_down = False
pressed_shift = False

# default game state
game_state = "menu"

# buttons
new_game_button = Button("New Game",412.5,250, font2,  screen, (150,150,150))
progress_button = Button("Progress",412.5,310, font2, screen, (175,175,175))
settings_button = Button("Settings",412.5,370, font2, screen, "light grey")
exit_button = Button("Exit",412.5,450, font2, screen, (250,50,87))

# game loop
while True:
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
        #background
        screen.fill("light blue")
        new_sun = pygame.transform.scale(sun, (200, 200), )
        new_cloud = pygame.transform.scale(cloud, (200,200), )
        screen.blit(new_grass, (0, 500))
        screen.blit(new_sun, (700,25))
        screen.blit(new_cloud, (60, 40))
        screen.blit(new_cloud, (200,75))
        screen.blit(new_cloud, (290, 5))
        screen.blit(new_cloud, (400, 50))

        if pressed_left:
            player_x -= 1
        if pressed_right:
            player_x += 1
        if pressed_up:
            player_y -= 1
        if pressed_down:
            player_y += 1

        screen.blit(player_idle, (player_x,player_y))

        #gen_world(screen)





        # add gameplay code here

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





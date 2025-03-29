# initialize useful modules
import sys, pygame
from button import Button
from terrain import scroll, draw_tiles
pygame.init()

# create game window
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Terraworld")

# clock controls
timer = pygame.time.Clock()

# game text
font = pygame.font.Font("assets/retro.ttf", 50)
font2 = pygame.font.Font(None, 35)
title_text = font.render("TERRAWORLD", True, "black")
title_text_rect = title_text.get_rect(midbottom=(500, 100))
back_to_menu = font2.render("Esc - Main Menu", True, "black")
author = font2.render("By Eddie Wanli", True, "black")
author_pos = author.get_rect(center=(900, 725))

#world assets
grass = pygame.image.load("assets/grass.jpg.")
dirt = pygame.image.load("assets/dirt.jpeg.")
sun = pygame.image.load("assets/sun 2.webp")
cloud = pygame.image.load("assets/cloud 2.webp")
background = pygame.image.load("assets/mario background.webp")
player_idle = pygame.image.load("assets/player Idle.png")

#player assets
run1 = pygame.image.load("assets/run 1.png")
run2 = pygame.image.load("assets/run 2.png")
run3 = pygame.image.load("assets/run 3.png")
run4 = pygame.image.load("assets/run 4.png")
run5 = pygame.image.load("assets/run 5.png")
run6 = pygame.image.load("assets/run 6.png")
run7 = pygame.image.load("assets/run 7.png")

#transformed world assets
new_grass = pygame.transform.scale(grass, (50,50), )
new_dirt = pygame.transform.scale(dirt, (50,50), )
new_sun = pygame.transform.scale(sun, (200, 200), )
new_cloud = pygame.transform.scale(cloud, (200,200), )
new_background = pygame.transform.scale(background, (1000,750), )
new_player_idle = pygame.transform.scale(player_idle, (40,80))
new_run1 = pygame.transform.scale(run1, (40,80), )
new_run2 = pygame.transform.scale(run2, (50,75), )
new_run3 = pygame.transform.scale(run3, (50,75), )
new_run4 = pygame.transform.scale(run4, (50,75), )
new_run5 = pygame.transform.scale(run5, (50,75), )
new_run6 = pygame.transform.scale(run6, (50,75), )
new_run7 = pygame.transform.scale(run7, (50,75), )
run_ani = [new_run1, new_run2, new_run3, new_run4, new_run5, new_run6, new_run7]

#movement variables
player_sprite = new_player_idle
player_rect = player_sprite.get_rect(midbottom=(500, 500))
player_rect.x = 500
player_rect.y = 500
pressed_right = False
pressed_left = False
pressed_shift = False
gravity = 0

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
                        gravity = - 17
                    elif event.key == pygame.K_LSHIFT:
                        pressed_shift = True
                        player_sprite = new_run1


        if event.type == pygame.KEYUP:
            if game_state == "game":
                if event.key == pygame.K_d:
                    pressed_right = False
                if event.key == pygame.K_a:
                    pressed_left = False
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
        world = draw_tiles(screen, 250)

        # player movement
        if pressed_right:
            player_rect.x += 2
        if pressed_left:
            player_rect.x -= 2
        if pressed_shift:
            if pressed_right:
                player_rect.x += 3.5
            if pressed_left:
                player_rect.x -= 3.5
        gravity += 1
        player_rect.y += gravity
        if player_rect.left < 500:
            player_rect.left = 500
        if player_rect.y > 520:
            player_rect.y = 520
        rect = pygame.Rect(player_rect.x - scroll[0], player_rect.y, 40, 80)
        pygame.draw.rect(screen, "red", rect, 2)

        #collisions

        for tile in world:
            pygame.draw.rect(screen, 'red', tile, 2 )
            if rect.colliderect(tile):
                if rect.bottom > tile.top:
                    rect.bottom = tile.top









        screen.blit(player_sprite, (player_rect.x - scroll[0], player_rect.y ))

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





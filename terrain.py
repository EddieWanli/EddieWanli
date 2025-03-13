import pygame
#tile size variable
tile_size = 50

#tile assets
grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (50,50))
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (50,50))

#tile map
tilemap = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1],
           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2],
           [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2]]

#tile generator
def gen_tiles(screen, tile_map):
    for i, row in enumerate(tile_map):
        for j, tile in enumerate(row):
            x = j * tile_size
            y = i * tile_size
            if tile == 1:
                screen.blit(new_grass, (x,y))
            elif tile == 2:
                screen.blit(new_dirt, (x,y))














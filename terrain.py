import pygame, random
# tile size variable
tile_size = 50

# tile assets
grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (50,50))
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (50,50))

# tile map
tilemap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#2
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#3
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#5
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#7
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#8
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#9
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#10
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#12
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],#13
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#14
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]#15

# tile placement
def tile_placer(tile_map):
    rows = len(tile_map)
    columns = len(tile_map[0])
    for i in range(rows):
        for j in range(columns):

            if i >= 11 and i < 14:
                if tile_map[i + 1][j] == 0: # checks if tile below current tile is air

                    tile_map[i][j] = 1  # places grass or dirt

                elif tile_map[i - 1][j] == 0: #checks if tile above current tile is air

                    tile_map[i][j] = random.randint(0, 1)  # could be water or dirt

                elif tile_map[i - 1][j] == 0:
                    if i >= 14:
                        tile_map[i][j] = 2
                    else:
                        tile_map[i][j] = 1
                else:
                    tile_map[i][j] = 2  # grass or dirt

            # ensures no air below grass or dirt
            if tile_map[i][j] in [1, 2]:  # if tile is grass or dirt

                if i + 1 < rows and tile_map[i + 1][j] == 0:
                    tile_map[i + 1][j] = tile_map[i][j]  # copy grass or dirt below

            if tile_map[i][j] == 0:
                if i + 1 < rows and tile_map[i + 1][j] == 2:
                    tile_map[i + 1][j] = 1

    return tile_map

# tile generator
def gen_tiles(screen, tile_map):
    for i, row in enumerate(tile_map):
        for j, tile in enumerate(row):
            x = j * tile_size
            y = i * tile_size
            if tile == 1:
                screen.blit(new_grass, (x,y))
            elif tile == 2:
                screen.blit(new_dirt, (x,y))














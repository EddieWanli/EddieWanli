import pygame, random
# tile size variable
tile_size = 50

# tile assets
grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (50,50))
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (50,50))

# tile map
tilemap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2]]

# tile placement
def tile_placer(tile_map):
    for i, row in enumerate(tile_map):
        for j in range(len(row)):
            # Assign a random tile based on the row index i
            if i > 11 and i < 14:
                if tile_map[i+1][j] == 0:
                    tile_map[i][j] = 0
                elif tilemap[i-1]:
                    tile_map[i][j] = random.randint(0, 2)
            elif i > 13:
                tile_map[i][j] = 2

            else:
                # Set tiles to 0 for rows at index 5 or less
                tile_map[i][j] = 0
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














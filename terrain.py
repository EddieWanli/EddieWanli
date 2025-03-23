import pygame, random

# constants
tile_size = 50
tiles = [1,2]
scroll = [0,0]
generated_tile_map = None

# tile assets
grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (tile_size,tile_size))
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (tile_size,tile_size))

# tile placement
def tile_placer(tile_map):
    rows = 15
    columns = 20
    for i in range(rows):
        for j in range(columns):

            if i + 1 < rows:
                if i in range(12,14):
                    if tile_map[i - 1][j] == 0:

                        tile_map[i][j] = random.randint(0, 1)

                    elif tile_map[i - 1][j] == 0:
                        if i >= 14:
                            tile_map[i][j] = 2
                        else:
                            tile_map[i][j] = 1
                    else:
                        tile_map[i][j] = 2

            # ensures no air below grass or dirt
            if tile_map[i][j] in [1, 2]:

                if i + 1 < rows and tile_map[i + 1][j] == 0:
                    tile_map[i + 1][j] = tile_map[i][j]

            if tile_map[i][j] == 0:
                if i + 1 < rows and tile_map[i + 1][j] == 2:
                    tile_map[i + 1][j] = 1

    return tile_map

# tile generator
def gen_tiles(screen, num_chunks):
    global generated_tile_map
    if generated_tile_map is None:
        tile_map_list = []

        for i in range(num_chunks):
            p = gen_tile_map()
            pp = tile_placer(p)
            tile_map_list.append(pp)
        generated_tile_map = tile_map_list

    for k in range(num_chunks):
        tile_map = generated_tile_map[k]
        for i, row in enumerate(tile_map):
            for j, tile in enumerate(row):
                x = j * tile_size
                y = i * tile_size
                if tile == 1:
                    screen.blit(new_grass, ((x + k * 20 * 50) - scroll[0], y - scroll[1]))
                elif tile == 2:
                    screen.blit(new_dirt, ((x + k * 20 * 50) - scroll[0], y - scroll[1]))


# tile map generator
def gen_tile_map():
    tile_map = []
    rows = 15
    columns = 20
    for i in range(rows):
        tile_map.append([])
        for j in range(columns):
            if i >= 14:
                tile_map[i].append(2)
            elif i == 13:
                tile_map[i].append(1)
            else:
                tile_map[i].append(0)
    return tile_map
















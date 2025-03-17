import pygame, random
# tile size variable
tile_size = 50
tiles = [1,2]
# tile assets
grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (tile_size,tile_size))
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (tile_size,tile_size))

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

scroll = [0,0]

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
def gen_tiles(screen, tile_map, num_chunks):
         for i, row in enumerate(tile_map):
            for j, tile in enumerate(row):
                x = j * tile_size
                y = i * tile_size
                for k in range(num_chunks):
                    if tile == 1:
                        screen.blit(new_grass, ((x+k*20*50) - scroll[0] ,y - scroll[1]))
                    elif tile == 2:
                        screen.blit(new_dirt, ((x+k*20*50) - scroll[0]  ,y - scroll[1]))

# tile map generator
def gen_tile_map(num):
    tile_map = []
    chunk = []
    rows = 15
    columns = 20
    for i in range(rows):
        chunk.append([])
        for j in range(columns):
            if i >= 14:
                chunk[i].append(2)
            elif i == 13:
                chunk[i].append(1)
            else:
                chunk[i].append(0)
    for i in range(num):
        tile_map.append(chunk)
    return tile_map

def chunk_gen(num):
    chunk_list = []
    chunk = gen_tile_map(num)
    for i in chunk:
        chunk_list.append(i)
    return chunk_list

p = chunk_gen(2)
print(p)













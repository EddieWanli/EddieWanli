import pygame, random

# constants
tile_size = 50
tiles = [1,2]
scroll = [0,0]
generated_tile_map = None

# tile assets
grass = pygame.image.load("assets/grass.jpg.")
new_grass = pygame.transform.scale(grass, (tile_size,tile_size))
dirt = pygame.image.load("assets/dirt.jpeg.")
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
def draw_tiles(screen, num_chunks):
    global generated_tile_map
    if generated_tile_map is None:
        chunk_list = []

        for i in range(num_chunks):
            tile_map = gen_tile_map()
            chunk = tile_placer(tile_map)
            chunk_list.append(chunk)
        generated_tile_map = chunk_list

    rect_list = []
    for k in range(num_chunks):
        tile_map = generated_tile_map[k]
        for i, row in enumerate(tile_map):
            for j, tile in enumerate(row):
                x = (j * tile_size + k * 20 * 50) - scroll[0]
                y = (i * tile_size) - scroll[1]
                if tile == 1:
                    screen.blit(new_grass, (x, y))
                    grass_rect = pygame.Rect(x, y, tile_size, tile_size)
                    rect_list.append(grass_rect)
                elif tile == 2:
                    screen.blit(new_dirt, (x ,y))
                    dirt_rect = pygame.Rect(x, y, tile_size, tile_size)
                    rect_list.append(dirt_rect)
    return rect_list


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


def handle_collisions(player_rect, world_tiles):

    detection_rect = pygame.Rect(player_rect.x, player_rect.y, player_rect.width, player_rect.height)
    detection_rect.inflate_ip(5, 5)

    on_ground = False
    hit_left = False
    hit_right = False

    colliding_tiles = []
    for tile in world_tiles:
        if detection_rect.colliderect(tile):
            colliding_tiles.append(tile)

    # vertical collisions
    for tile in colliding_tiles:
        if player_rect.bottom > tile.top and player_rect.bottom < tile.top + 20:
            if player_rect.right > tile.left + 5 and player_rect.left < tile.right - 5:
                player_rect.bottom = tile.top
                on_ground = True

    # horizontal collisions
    for tile in colliding_tiles:
        # right collision
        if player_rect.right > tile.left and player_rect.right < tile.left + 20:
            if player_rect.bottom > tile.top + 5:
                player_rect.right = tile.left
                hit_right = True

        # left collision
        elif player_rect.left < tile.right and player_rect.left > tile.right - 20:
            if player_rect.bottom > tile.top + 5:
                player_rect.left = tile.right
                hit_left = True

    return on_ground, hit_left, hit_right





















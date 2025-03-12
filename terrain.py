import pygame, random, noise
t_map=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
       [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2],]

grass = pygame.image.load("images/grass.jpg.")
new_grass = pygame.transform.scale(grass, (50,50),)
dirt = pygame.image.load("images/dirt.jpeg.")
new_dirt = pygame.transform.scale(dirt, (50,50), )
air = pygame.image.load("images/air.jpg")
new_air = pygame.transform.scale(air, (50,50), )

tile_types = {0:air,1:new_grass,2:new_dirt}

def generate_chunk(x,y):
    chunk_data = []
    for y_pos in range(10):
        for x_pos in range(10):
            target_x = x * 10 + x_pos
            target_y = y * 10 + y_pos
            tile_type = 0 # nothing
            height = int(noise.pnoise1(target_x * 0.1, repeat=9999999) * 5)
            if target_y > 8 - height:
                tile_type = 2 # dirt
            elif target_y == 8 - height:
                tile_type = 1 # grass
            elif target_y == 8 - height - 1:
                if random.randint(1,5) == 1:
                    tile_type = 3 # plant
            if tile_type != 0:
                chunk_data.append([[target_x,target_y],tile_type])
    return chunk_data














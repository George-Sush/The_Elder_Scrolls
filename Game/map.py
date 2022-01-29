from settings import *
from numba.core import types
from numba.typed import Dict
from numba import int32
import pygame

_ = False
matrix_map = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5],
[2, 2, _, _, 2, _, 2, _, 2, 2, 2, _, _, 2, 2, 2, 2, _, 2, 2, 2, 2, 2, 2, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 2, 2, 5, 5, 5, 5, 5, _, _, _, 5],
[2, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, 2, 2, 2, 2, 2, _, _, _, _, 2, 2, 2, 2, 2, _, _, _, _, _, 2, 5, _, _, _, _, _, 1, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, 2, 2, 2, _, 2, 2, _, 2, 2, 2, 2, 2, _, _, _, _, _, 2, 2, _, 2, 2, 2, 2, 5, _, _, 5, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 2, 2, 2, 2, _, 2, 2, 2, 2, _, _, _, _, _, _, 2, 2, _, _, 5, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, 2, 2, _, _, 2, _, _, _, _, _, _, _, _, 2, _, _, _, 2, 2, 2, _, _, _, _, _, _, 5, 5, _, 1, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, _, 2, 2, _, 2, 2, _, _, 2, 2, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, 5, 5, 5, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, 2, _, 2, 2, 2, 2, 2, 2, _, 2, _, _, _, _, _, _, 2, _, _, _, 2, 2, 2, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, _, 2, _, _, 2, _, _, _, _, _, _, 2, 2, _, 2, 2, _, _, _, 2, 5, _, 1, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, 2, 2, _, 2, 2, 2, 2, _, _, _, _, _, _, _, 2, 2, 2, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 2, _, 2, 2, _, _, _, 2, 2, _, 2, 2, 2, 2, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, 2, _, _, 2, _, _, _, _, _, _, _, 2, _, _, 2, _, 2, 5, _, 1, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, 2, 2, 2, 2, _, _, 2, 2, _, 2, _, _, 2, _, _, _, 2, 5, _, _, _, 5],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, 2, _, 2, 2, 5, _, _, _, 5],
[6, 6, 6, 6, 6, 6, _, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, _, _, _, _, _, 2, _, _, _, _, 2, 2, _, 2, 2, _, 2, 2, _, _, _, 2, 5, _, 1, _, 5],
[6, 3, _, 4, _, 4, _, _, _, _, _, _, _, _, _, 4, 4, _, 3, 4, 6, _, _, _, 2, _, _, 2, _, 2, 2, _, _, _, 2, 2, _, 2, 2, _, _, 2, 2, 5, _, _, _, 5],
[6, 4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4, 3, 6, _, _, _, 2, 2, _, _, _, _, _, _, _, _, 2, _, _, _, 2, 2, 2, 2, 2, 5, _, _, _, 5],
[6, 4, _, 4, 4, _, 3, _, _, _, _, 6, 6, 6, _, _, 4, _, _, _, 6, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 2, _, 2, _, _, 2, 2, 2, 5, _, 1, _, 5],
[6, _, _, _, _, _, 4, _, 6, 6, 6, _, _, _, _, _, 4, _, _, _, 6, _, _, _, _, _, _, _, 2, _, 2, _, _, _, _, _, _, _, _, _, _, 2, 2, 5, _, _, _, 5],
[6, 4, _, 4, _, _, _, 6, 6, _, _, _, _, 6, _, _, _, _, 4, _, 6, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, 2, _, _, 2, _, _, _, 2, 5, _, _, _, 5],
[6, _, _, _, _, 4, 6, 6, 6, 6, 6, _, _, _, 6, 6, 4, _, 3, _, 6, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, 5, _, 1, _, 5],
[6, 4, 4, _, 3, 6, 3, _, _, 3, 4, _, _, _, 3, _, 6, _, _, _, 6, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, 2, 5, _, _, _, 5],
[6, _, _, _, 6, 6, _, _, _, _, _, _, 3, _, _, _, 3, 6, 4, 4, 6, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, 2, 2, 5, _, _, _, 5],
[6, _, _, 6, 3, 3, _, 3, _, _, _, 3, 3, 3, _, _, 3, 6, 4, 4, 6, _, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, _, 1, _, 5],
[6, 4, 6, _, _, _, _, _, _, _, _, _, 3, 3, 4, _, _, _, 6, 6, 6, _, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, _, _, _, _, 5],
[6, 6, _, _, 3, _, 4, _, _, 3, _, _, _, _, _, _, _, _, _, 3, 6, _, 2, 5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
[6, 3, 3, _, 4, _, _, 6, _, 6, _, 3, 3, _, _, _, 3, _, _, 4, 6, _, 2, 5, _, _, _, _, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 5],
[6, _, _, _, _, _, 6, 7, _, 7, 6, _, _, 3, _, 3, 3, _, _, 3, 6, _, 2, 5, _, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
[6, _, 4, _, _, 6, 7, _, _, _, 7, 6, _, _, _, _, 3, _, _, 3, 6, _, 2, 5, _, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
[6, 3, _, _, 6, 7, _, _, _, _, _, 7, 6, _, 3, _, 3, _, _, 3, 6, _, 2, 5, _, _, _, _, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 5],
[6, 4, _, 3, 6, 7, _, _, _, _, _, 7, 6, _, 3, _, 3, 4, _, _, 6, _, 2, 5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5],
[6, 6, 6, 6, 6, 7, 7, 7, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
]

WORLD_WIDTH, WORLD_HEIGHT = max([len(i) for i in matrix_map]) * TILE, len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
            elif char == 5:
                world_map[(i * TILE, j * TILE)] = 5
            elif char == 6:
                world_map[(i * TILE, j * TILE)] = 6
            elif char == 7:
                world_map[(i * TILE, j * TILE)] = 7
            elif char == 8:
                world_map[(i * TILE, j * TILE)] = 8
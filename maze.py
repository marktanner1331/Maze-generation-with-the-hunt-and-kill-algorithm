import numpy as np
import random
from maze_functions import *


def possible_moves(visited: np.array, cell: (int, int)):
    moves = []

    for direction in [north, south, east, west]:
        new_cell = direction(cell)

        # check the cell is in the bounds
        if not 0 <= new_cell[0] < visited.shape[0]:
            continue
        if not 0 <= new_cell[1] < visited.shape[1]:
            continue

        if visited[new_cell]:
            continue

        moves.append(new_cell)

    return moves


def get_adjacent_visited(visited, cell):
    cells = []
    for direction in [north, south, east, west]:
        new_cell = direction(cell)

        # check the cell is in the bounds
        if not 0 <= new_cell[0] < visited.shape[0]:
            continue
        if not 0 <= new_cell[1] < visited.shape[1]:
            continue

        if visited[new_cell]:
            cells.append(new_cell)

    return cells


def hunt(visited):
    for j in range(visited.shape[1]):
        for i in range(visited.shape[0]):
            if visited[(i, j)]:
                continue
                
            adjacent = get_adjacent_visited(visited, (i, j))
            if len(adjacent) == 0:
                continue
                    
            new_cell = random.choice(adjacent)
            return new_cell, (i, j)


def generate_maze():
    width = 10
    height = 10
    grid = np.zeros((width, height, 2), bool)

    # set the current cell to a random value
    current_cell = (random.randint(0, width - 1), random.randint(0, height - 1))

    # a grid to track if the cell has been visited
    visited = np.zeros((width, height), bool)
    unvisited_count = width * height

    visited[current_cell] = True
    unvisited_count -= 1

    while unvisited_count > 0:
        moves = possible_moves(visited, current_cell)
        
        if len(moves) > 0:
            new_cell = random.choice(moves)
        else:
            current_cell, new_cell = hunt(visited)

        link_cells(grid, current_cell, new_cell)

        visited[new_cell] = True
        unvisited_count -= 1

        current_cell = new_cell

    draw_maze(grid)


generate_maze()

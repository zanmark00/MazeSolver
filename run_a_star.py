# run_a_star.py
from pyamaze import maze, agent, COLOR, textLabel
import time
import random
from prepare_maze import load_maze_params, recreate_and_solve_maze, visualize_path

from queue import PriorityQueue

def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def a_star_solve(m):
    start = (m.rows, m.cols)
    goal = (1, 1)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set([start])

    while not frontier.empty():
        current_cost, current = frontier.get()

        if current == goal:
            break

        for direction in 'ESNW':
            if m.maze_map[current][direction]:
                next_cell = (current[0] + (direction == 'S') - (direction == 'N'), current[1] + (direction == 'E') - (direction == 'W'))
                new_cost = cost_so_far[current] + 1
                if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                    cost_so_far[next_cell] = new_cost
                    priority = new_cost + manhattan_distance(next_cell, goal)
                    frontier.put((priority, next_cell))
                    came_from[next_cell] = current
                    visited.add(next_cell)  # Add to visited when a new node is reached

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from.get(current)
    path.append(start)
    path.reverse()

    # Return the path and the number of nodes expanded
    return path, len(visited)


if __name__ == '__main__':
    # Load maze parameters from the specific file
    params = load_maze_params('maze_params50_50.json')  # Adjusted to the specific file name
    random.seed(params['seed'])  # Ensure reproducibility

    # Recreate the maze based on loaded parameters
    m = maze(params['rows'], params['cols'])
    m.CreateMaze(loopPercent=params['loopPercent'], theme=COLOR.light)

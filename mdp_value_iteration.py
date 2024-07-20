import numpy as np
from pyamaze import maze, agent, COLOR

def get_actions(m, x, y):
    actions = m.maze_map[(x, y)]
    s = []
    for direction, exists in actions.items():
        if exists:
            s.append(direction)
    return s

def value_iteration(m, gamma=0.9, threshold=0.005):
    cell_list = list(m.maze_map.keys())

    rewards = {cell: -1 for cell in cell_list}  # Default reward
    rewards[(1, 1)] = 1000  # Reward for reaching the goal

    value = {cell: 0 for cell in cell_list}  # Initial value function

    policy = {cell: 'E' for cell in cell_list}  # Dummy initial policy

    while True:
        delta = 0
        for cell in cell_list:
            if cell == (1, 1):
                continue  # Skip the goal cell
            v = value[cell]
            value[cell] = max([rewards[cell] + gamma * value[get_next_state(m, cell, action)]
                               for action in get_actions(m, *cell)])
            delta = max(delta, abs(v - value[cell]))

        if delta < threshold:
            break

    for cell in policy.keys():
        best_action = None
        best_value = float('-inf')
        for action in get_actions(m, *cell):
            next_cell = get_next_state(m, cell, action)
            if value[next_cell] > best_value:
                best_value = value[next_cell]
                best_action = action
        policy[cell] = best_action

    return generate_path(policy, m)

def get_next_state(maze, cell, action):
    x, y = cell
    if action == 'N':
        return (x-1, y)
    elif action == 'S':
        return (x+1, y)
    elif action == 'E':
        return (x, y+1)
    elif action == 'W':
        return (x, y-1)
    return cell

def generate_path(policy, maze):
    current_cell = (maze.rows, maze.cols)
    path = [current_cell]
    while current_cell != (1, 1):
        current_cell = get_next_state(maze, current_cell, policy[current_cell])
        path.append(current_cell)
    return path

if __name__ == '__main__':
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=50, theme=COLOR.light)
    path = value_iteration(m)
    print("Optimal path:", path)
    a = agent(m, footprints=True, color=COLOR.green, filled=True)
    m.tracePath({a: path}, delay=100)
    m.run()

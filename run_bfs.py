# run_bfs.py

import json
from prepare_maze import load_maze_params, visualize_path, recreate_and_solve_maze
from collections import deque

def bfs_solve(m):
    start = (m.rows, m.cols)
    frontier = deque([start])  # Queue for BFS
    explored = set([start])  # Set to keep track of explored cells, including start
    came_from = {start: None}  # Dictionary to track the path

    while frontier:
        current = frontier.popleft()
        if current == (1, 1):  # Assuming the goal is at (1, 1)
            break

        for direction in 'ESNW':  # Explore all possible directions
            if m.maze_map[current][direction]:
                if direction == 'E':
                    next_cell = (current[0], current[1]+1)
                elif direction == 'W':
                    next_cell = (current[0], current[1]-1)
                elif direction == 'N':
                    next_cell = (current[0]-1, current[1])
                elif direction == 'S':
                    next_cell = (current[0]+1, current[1])

                if next_cell not in explored:
                    frontier.append(next_cell)
                    explored.add(next_cell)
                    came_from[next_cell] = current

    # Reconstruct the path from start to goal
    current = (1, 1)  # Goal position
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path, len(explored)


if __name__ == '__main__':
    loaded_params = load_maze_params('maze_params50_50.json')

    algorithms = [('BFS', bfs_solve),]
    metrics = []
    for name, algorithm in algorithms:
        execution_time, path_length, m, solution_path = recreate_and_solve_maze(loaded_params, algorithm)
        print(f"{name} Execution Time: {execution_time:.5f} seconds")
        print(f"{name} Path Length: {path_length}")
        metrics.append({
            'Algorithm': name,
            'Execution Time': execution_time,
            'Path Length': path_length
        })
        if solution_path:
            visualize_path(m, solution_path)
        else:
            print(f"{name}: No path found.")
    with open('algorithm_performance_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)

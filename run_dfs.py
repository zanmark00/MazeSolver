# run_dfs.py

from prepare_maze import load_maze_params, recreate_and_solve_maze, visualize_path

def dfs_solve(maze):
    start = (maze.rows, maze.cols)
    goal = (1, 1)
    visited = set([start])
    stack = [start]
    path = {}

    while stack:
        current = stack.pop()
        if current == goal:
            break

        for direction in 'ESNW':
            next_cell = None
            if direction == 'E' and maze.maze_map[current][direction]:
                next_cell = (current[0], current[1] + 1)
            elif direction == 'W' and maze.maze_map[current][direction]:
                next_cell = (current[0], current[1] - 1)
            elif direction == 'N' and maze.maze_map[current][direction]:
                next_cell = (current[0] - 1, current[1])
            elif direction == 'S' and maze.maze_map[current][direction]:
                next_cell = (current[0] + 1, current[1])

            if next_cell and next_cell not in visited:
                visited.add(next_cell)
                stack.append(next_cell)
                path[next_cell] = current

    # Reconstruct the path from the goal to the start
    if goal not in path:
        return [], 0  # No path found and no nodes expanded

    current = goal
    reconstructed_path = [current]
    while current in path:
        current = path[current]
        reconstructed_path.append(current)
    reconstructed_path.reverse()

    # Return both the path and the count of nodes expanded
    return reconstructed_path, len(visited)


if __name__ == '__main__':
    loaded_params = load_maze_params('maze_params50_50.json')  # Adjusted to the specific file name

    execution_time, path_length, m, solution_path = recreate_and_solve_maze(loaded_params, dfs_solve)

    print(f"DFS Execution Time: {execution_time:.5f} seconds")
    print(f"DFS Path Length: {path_length}")

    if solution_path:
        visualize_path(m, solution_path)
    else:
        print("DFS: No path found.")

import json
import time
from prepare_maze import load_maze_params, recreate_and_solve_maze
from pyamaze import maze, COLOR
from run_dfs import dfs_solve
from run_bfs import bfs_solve
from run_a_star import a_star_solve


def measure_algorithm_performance(algorithm, params):
    # Create a new maze object for each algorithm to ensure fairness
    m = maze(params['rows'], params['cols'])
    if 'theme' in params and params['theme'] in COLOR.__members__:
        theme = COLOR.__members__[params['theme']]
    else:
        theme = COLOR.light  # Default theme
    m.CreateMaze(loopPercent=params['loopPercent'], theme=theme)

    start_time = time.time()
    # Capture all returned values as a tuple
    returned_values = algorithm(m)
    execution_time = time.time() - start_time

    # Assuming the first value is the path and the second value is nodes_expanded
    path, nodes_expanded = returned_values[0], returned_values[1]
    path_length = len(path)
    return execution_time, path_length, nodes_expanded


if __name__ == '__main__':
    loaded_params = load_maze_params('maze_params20_20.json')
    algorithms = {
        'DFS': dfs_solve,
        'BFS': bfs_solve,
        'A*': a_star_solve,
    }
    results = []

    for name, algorithm in algorithms.items():
        execution_time, path_length, nodes_expanded = measure_algorithm_performance(algorithm, loaded_params)
        results.append({
            'Algorithm': name,
            'Execution Time': execution_time,
            'Path Length': path_length,
            'Nodes Expanded': nodes_expanded,
        })

    print("Performance Metrics:")
    for result in results:
        print(f"{result['Algorithm']}:")
        print(f" Execution Time: {result['Execution Time']:.5f} seconds")
        print(f" Path Length: {result['Path Length']}")
        print(f" Nodes Expanded: {result['Nodes Expanded']}\n")

    # Optionally, save to a JSON file for further analysis
    with open('algorithm_performance_metrics.json', 'w') as f:
        json.dump(results, f, indent=4)

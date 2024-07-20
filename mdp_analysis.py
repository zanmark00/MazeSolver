import json
import time
from prepare_maze import load_maze_params
from pyamaze import maze, COLOR
from mdp_policy_iteration import policy_iteration
from mdp_value_iteration import value_iteration

def measure_mdp_algorithm_performance(algorithm, params):
    # Create a new maze object for each algorithm to ensure fairness
    m = maze(params['rows'], params['cols'])
    if 'theme' in params and params['theme'] in COLOR.__members__:
        theme = COLOR.__members__[params['theme']]
    else:
        theme = COLOR.light  # Default theme
    m.CreateMaze(loopPercent=params['loopPercent'], theme=theme)

    start_time = time.time()
    path = algorithm(m)
    execution_time = time.time() - start_time

    path_length = len(path) if path else 0

    return execution_time, path_length

if __name__ == '__main__':
    loaded_params = load_maze_params('maze_params20_20.json')
    algorithms = {
        'Policy Iteration': policy_iteration,
        'Value Iteration': value_iteration,
    }
    results = []

    for name, algorithm in algorithms.items():
        execution_time, path_length = measure_mdp_algorithm_performance(algorithm, loaded_params)
        results.append({
            'Algorithm': name,
            'Execution Time': execution_time,
            'Path Length': path_length,
        })

    print("MDP Performance Metrics:")
    for result in results:
        print(f"{result['Algorithm']}:")
        print(f" Execution Time: {result['Execution Time']:.5f} seconds")
        if result['Path Length'] > 0:  # Path length may not be relevant for some MDP analyses
            print(f" Path Length: {result['Path Length']}")
        print()

    with open('mdp_algorithm_performance_metrics.json', 'w') as f:
        json.dump(results, f, indent=4)

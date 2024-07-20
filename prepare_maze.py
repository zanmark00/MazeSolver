import json
from pyamaze import maze, agent, COLOR, textLabel
import random
import time

def visualize_path(m, path):
    """Visualize the path found by the solving algorithm in the maze."""
    a = agent(m, footprints=True, color=COLOR.red, filled=True)
    # Ensure path is a list of tuples for compatibility with pyamaze
    if isinstance(path, dict):
        converted_path = [path[0]]
        while converted_path[-1] in path:
            converted_path.append(path[converted_path[-1]])
        path = converted_path
    m.tracePath({a:path}, delay=100)
    textLabel(m, path[0], 'Start')
    textLabel(m, path[-1], 'Goal')
    m.run()

def load_maze_params(filename):
    """Load maze generation parameters from a file."""
    with open(filename, 'r') as f:
        return json.load(f)

def recreate_and_solve_maze(params, solve_function):
    random.seed(params.get('seed', 0))
    # Adjust based on the actual structure of your JSON
    rows = params.get('rows')
    cols = params.get('cols')
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=params.get('loopPercent', 0), theme=COLOR.light)
    start_time = time.perf_counter()
    solution_path = solve_function(m)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    path_length = len(solution_path) if solution_path else 0
    return execution_time, path_length, m, solution_path
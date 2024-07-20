import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from pyamaze import maze, agent, textLabel
from mdp_policy_iteration import policy_iteration
from mdp_value_iteration import value_iteration

def load_maze_params(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def plot_maze_with_values(m, values, title):
    grid = np.full((m.rows, m.cols), np.nan)
    for (r, c), v in values.items():
        grid[m.rows - r, c - 1] = v  # Invert row index for visualization

    norm = Normalize(vmin=min(values.values()), vmax=max(values.values()))
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='coolwarm', norm=norm)

    # Annotate each cell with the corresponding MDP value
    for (r, c), v in np.ndenumerate(grid):
        if not np.isnan(v):
            plt.text(c, r, f'{v:.2f}', ha='center', va='center',
                     color='white' if v > norm((norm.vmax+norm.vmin)/2) else 'black')

    plt.title(title)
    plt.colorbar(label='MDP Value')
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    params = load_maze_params('maze_params10_10.json')
    m = maze(params['rows'], params['cols'])
    m.CreateMaze(loopPercent=params.get('loopPercent', 0))
    m.goal = (1, 1)  # Set the goal manually if it's not set by pyamaze

    # Run policy iteration and value iteration
    policy, policy_values = policy_iteration(m)
    value_values = value_iteration(m)

    # Visualize the MDP values
    plot_maze_with_values(m, policy_values, 'Policy Iteration MDP Values')
    plot_maze_with_values(m, value_values, 'Value Iteration MDP Values')

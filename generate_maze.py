import json
from pyamaze import maze, COLOR
import random
import matplotlib.pyplot as plt

def save_maze_params(filename, rows, cols, loopPercent, seed, start, end):
    # Save maze configuration parameters to a JSON file
    params = {
        'rows': rows,
        'cols': cols,
        'loopPercent': loopPercent,
        'seed': seed,
        'start': start,
        'end': end
    }
    with open(filename, 'w') as f:
        json.dump(params, f)

def plot_maze(m, filename, start, end):
    # Plot the maze with start and end points and save to a file
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, m.cols)
    ax.set_ylim(0, m.rows)
    ax.invert_yaxis()

    for cell in m.grid:
        if not m.maze_map[cell]['N']:
            ax.plot([cell[1]-1, cell[1]], [cell[0]-1, cell[0]-1], color='k', linewidth=2)
        if not m.maze_map[cell]['S']:
            ax.plot([cell[1]-1, cell[1]], [cell[0], cell[0]], color='k', linewidth=2)
        if not m.maze_map[cell]['E']:
            ax.plot([cell[1], cell[1]], [cell[0]-1, cell[0]], color='k', linewidth=2)
        if not m.maze_map[cell]['W']:
            ax.plot([cell[1]-1, cell[1]-1], [cell[0]-1, cell[0]], color='k', linewidth=2)

    ax.plot(start[1]-0.5, start[0]-0.5, 'go', markersize=10, label='Start')
    ax.plot(end[1]-0.5, end[0]-0.5, 'ro', markersize=10, label='End')
    ax.legend(loc='upper right')
    ax.axis('off')
    plt.savefig(filename)

if __name__ == '__main__':
    # Define maze size and configuration
    rows, cols = 100, 100  # Updated to match the size you might want for solving
    start = [1, 1]  # Updated to list format to match JSON saving/loading
    end = [rows, cols]  # Updated to list format for consistency
    loopPercent = 50
    seed = random.randint(0, 10000)

    # Initialize random seed for reproducible maze generation
    random.seed(seed)

    # Create and display the maze
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=loopPercent, theme=COLOR.light)

    # Save maze parameters to JSON file
    filename = f'maze_params{rows}_{cols}.json'
    save_maze_params(filename, rows, cols, loopPercent, seed, start, end)

    # Plot and save the maze image
    image_filename = f'maze_{rows}_{cols}.png'
    plot_maze(m, image_filename, start, end)

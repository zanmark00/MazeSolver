# MazeSolver

This is a Python project that includes various algorithms for generating and solving mazes. The project provides tools for analyzing the performance of these algorithms.

## Directory Structure

- **analysis.py**: Analyzes the generated mazes and the performance of the algorithms.
- **generate_maze.py**: Generates mazes of various sizes.
- **mdp_algorithms.py**: Contains Markov Decision Process (MDP) algorithms.
- **mdp_analysis.py**: Analyzes the performance of MDP algorithms.
- **mdp_policy_iteration.py**: Implements the policy iteration algorithm for MDP.
- **mdp_values.py**: Stores values related to MDP.
- **mdp_value_iteration.py**: Implements the value iteration algorithm for MDP.
- **prepare_maze.py**: Prepares the maze for algorithmic processing.
- **run_a_star.py**: Runs the A* search algorithm on the maze.
- **run_bfs.py**: Runs the Breadth-First Search (BFS) algorithm on the maze.
- **run_dfs.py**: Runs the Depth-First Search (DFS) algorithm on the maze.
- **search_algorithms.py**: Contains various search algorithms for solving mazes.

## How to Run

1. **Clone the repository**:

   git clone git@github.com:zanmark00/MazeSolver.git
   cd MazeSolver

2. **Install dependencies**:
   Make sure you have Python installed. You may also need to install additional dependencies, which can be managed using pip.

3. **Generate a maze**:

   python generate_maze.py

4. **Solve the maze using a specific algorithm**:

   python run_a_star.py

   Replace run_a_star.py with run_bfs.py or run_dfs.py to use different algorithms.

## Analyzing Performance

You can analyze the performance of the algorithms by running:

   python analysis.py

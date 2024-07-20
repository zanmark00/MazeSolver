import random
import time
from pyamaze import maze, agent, COLOR
from mdp_policy_iteration import policy_iteration
from mdp_value_iteration import value_iteration

def visualize_mdp_solutions(rows, cols, loopPercent=50):
    # Create and generate the maze
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=loopPercent, theme=COLOR.light)

    # Execute and visualize Policy Iteration
    policy_path = policy_iteration(m)
    if policy_path:
        policy_agent = agent(m, footprints=True, color=COLOR.red, filled=True)
        m.tracePath({policy_agent: policy_path}, delay=100)

    # Execute and visualize Value Iteration
    value_path = value_iteration(m)
    if value_path:
        value_agent = agent(m, footprints=True, color=COLOR.blue)
        m.tracePath({value_agent: value_path}, delay=100)

    m.run()

if __name__ == '__main__':
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    loopPercent = 50
    visualize_mdp_solutions(rows, cols, loopPercent)

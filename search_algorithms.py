from pyamaze import maze, agent, COLOR
from run_dfs import dfs_solve
from run_bfs import bfs_solve
from run_a_star import a_star_solve

def run_search_algorithms(rows, cols):
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=50, theme=COLOR.light)

    dfs_path, _ = dfs_solve(m)
    bfs_path, _ = bfs_solve(m)
    a_star_path, _ = a_star_solve(m)

    # Visualize the maze solutions
    dfs_agent = agent(m, footprints=True, color=COLOR.red, filled=True, goal=(1, 1))
    bfs_agent = agent(m, footprints=True, color=COLOR.blue, filled=True, goal=(1, 1))
    a_star_agent = agent(m, footprints=True, color=COLOR.black, filled=False, goal=(1, 1))

    m.tracePath({dfs_agent: dfs_path}, delay=100)
    m.tracePath({bfs_agent: bfs_path}, delay=100)
    m.tracePath({a_star_agent: a_star_path}, delay=100)

    m.run()


if __name__ == '__main__':
    rows = int(input("Enter the number of rows for the maze: "))
    cols = int(input("Enter the number of columns for the maze: "))
    run_search_algorithms(rows, cols)

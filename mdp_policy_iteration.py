from pyamaze import maze, agent, COLOR, textLabel
from timeit import default_timer as timer

def get_actions(m, x, y):
    actions = m.maze_map[(x, y)]
    return [direction for direction, exists in actions.items() if exists]

def policy_evaluation(policy, m, V, gamma, theta):
    while True:
        delta = 0
        for s in m.maze_map.keys():
            v = 0
            for a in get_actions(m, *s):
                prob_a = policy[s].get(a, 0)
                nxt = get_next_state(m, s, a)
                v += prob_a * (m.rewards.get(nxt, -1) + gamma * V[nxt])
            delta = max(delta, abs(v - V[s]))
            V[s] = v
        if delta < theta:
            break

def policy_improvement(m, V, gamma):
    policy = {s: {a: 1/len(get_actions(m, *s)) for a in get_actions(m, *s)} for s in m.maze_map.keys()}
    policy_stable = False

    while not policy_stable:
        policy_evaluation(policy, m, V, gamma, theta=0.005)
        policy_stable = True
        for s in m.maze_map.keys():
            chosen_a = max(policy[s], key=policy[s].get)
            best_a, best_value = None, float('-inf')
            for a in get_actions(m, *s):
                nxt = get_next_state(maze, s, a)
                value = m.rewards.get(nxt, -1) + gamma * V[nxt]
                if value > best_value:
                    best_a, best_value = a, value
            policy[s] = {a: 1 if a == best_a else 0 for a in get_actions(m, *s)}
            if chosen_a != best_a:
                policy_stable = False
    return policy

def get_next_state(m, state, action):
    x, y = state
    if action == 'N':
        return (x-1, y)
    elif action == 'S':
        return (x+1, y)
    elif action == 'W':
        return (x, y-1)
    elif action == 'E':
        return (x, y+1)
    return state

def extract_policy_path(policy, m):
    current = (m.rows, m.cols)
    path = [current]
    while current != (1, 1):
        for action, prob in policy[current].items():
            if prob == 1:
                current = get_next_state(m, current, action)
                path.append(current)
                break
    return path

def policy_iteration(m):
    gamma = 0.9
    maze.rewards = {(1, 1): 1000}
    V = {s: 0 for s in m.maze_map.keys()}

    start_time = timer()
    policy = policy_improvement(m, V, gamma)
    path = extract_policy_path(policy, m)
    end_time = timer()

    print(f"Policy Iteration Time: {end_time - start_time:.4f} seconds")
    return path

if __name__ == "__main__":
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=50, theme=COLOR.light)
    path = policy_iteration(m)
    a = agent(m, footprints=True, color=COLOR.red, filled=True)
    m.tracePath({a: path}, delay=100)
    m.run()

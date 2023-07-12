import queue

# read the input file and store the grid in a list
with open('C:/Users/Rimsha/Desktop/grid.txt', 'r') as f:
    total_cols, total_rows = map(int, f.readline().split())
    start_col, start_row = map(int, f.readline().split())
    goal_col, goal_row = map(int, f.readline().split())
    grid = [[int(cell) for cell in f.readline().split()] for _ in range(total_rows)]

# define the possible actions
actions = [(0, -1, 3), (1, 0, 2), (0, 1, 2), (-1, 0, 3)]
action_costs = [2, 2, 1, 3]

# define a function to get the neighbors of a cell
def get_neighbors(cell):
    neighbors = []
    for action, cost in zip(actions, action_costs):
        neighbor_col = cell[0] + action[0]
        neighbor_row = cell[1] + action[1]
        if (0 <= neighbor_col < total_cols) and (0 <= neighbor_row < total_rows) and (grid[neighbor_row][neighbor_col] != 1):
            neighbors.append(((neighbor_col, neighbor_row), cost))
    return neighbors

# initialize the start and goal cells and the frontier queue
start_cell = (start_col, start_row)
goal_cell = (goal_col, goal_row)
frontier = queue.Queue()
frontier.put(start_cell)

# initialize the came_from and cost_so_far dictionaries
came_from = {}
came_from[start_cell] = None
cost_so_far = {}
cost_so_far[start_cell] = 0

# search for the goal cell using breadth-first search
while not frontier.empty():
    current = frontier.get()
    if current == goal_cell:
        break
    for next_cell, action_cost in get_neighbors(current):
        new_cost = cost_so_far[current] + action_cost
        if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
            cost_so_far[next_cell] = new_cost
            priority = new_cost
            frontier.put(next_cell)
            came_from[next_cell] = (current, actions[action_costs.index(action_cost)][2])

# if the goal cell was reached, reconstruct the path
if goal_cell in came_from:
    path = []
    current = goal_cell
    while current != start_cell:
        path.append(came_from[current][1])
        current = came_from[current][0]
    path.reverse()
    print("Path found: ", path)
    print("Total cost: ", cost_so_far[goal_cell])
    for row in range(total_rows):
        for col in range(total_cols):
            if (col, row) == start_cell:
                print("S", end=" ")
            elif (col, row) == goal_cell:
                print("G", end=" ")
            elif grid[row][col] == 1:
                print("1", end=" ")
            elif (col, row) in came_from:
                print("*", end=" ")
            else:
                print("0", end=" ")
        print()
else:
    print("Path not found")
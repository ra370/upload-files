import heapq
import math
from typing import List, Tuple

def read_input_file(file_name: str) -> Tuple[int, Tuple[int, int], Tuple[int, int], List[List[int]]]:
    with open('C:/Users/Rimsha/Desktop/grid.txt', 'r') as f:
        n = int(f.readline().strip().split()[0])
        start = tuple(map(int, f.readline().strip().split()))
        goal = tuple(map(int, f.readline().strip().split()))
        grid = [list(map(int, f.readline().strip().split('\t'))) for _ in range(n)]

    return n, start, goal, grid

def euclidean_distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star_search(n: int, start: Tuple[int, int], goal: Tuple[int, int], grid: List[List[int]]) -> Tuple[List[Tuple[int, int]], List[str], int, List[List[str]]]:

    # Define possible moves and their costs
    moves = [('up', (-1, 0), 2), ('right', (0, 1), 2), ('down', (1, 0), 1), ('left', (0, -1), 3)]

    # Initialize the priority queue
    pq = [(0, start, [], 0)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, current, path, cost = heapq.heappop(pq)

        if current == goal:
            grid_text = [['*' if (i, j) in path else str(grid[i][j]) for j in range(n)] for i in range(n)]
            actions = [move for move, _ in path[1:]]
            return path, actions, cost, grid_text

        if current in visited:
            continue

        visited.add(current)

        for move, (dx, dy), move_cost in moves:
            x, y = current
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 1 and (nx, ny) not in visited:
                new_cost = cost + move_cost
                heapq.heappush(pq, (new_cost + euclidean_distance((nx, ny), goal), (nx, ny), path + [(move, (nx, ny))], new_cost))

    return [], [], -1, grid

def main(file_name: str):
    n, start, goal, grid = read_input_file(file_name)
    path, actions, total_cost, grid_text = a_star_search(n, start, goal, grid)

    if total_cost == -1:
        print("Failed to find a path.")
    else:
        print("Path:")
        for step in path:
            print(f"{step[0]} -> {step[1]}")
        print("Actions:", ", ".join(actions))
        print("Total Cost:", total_cost)
        print("Grid:")
        for row in grid_text:
            print(" ".join(row))

if __name__== "__main__":
    # Replace 'grid.txt' with your input file name
    file_name = 'C:/Users/Rimsha/Desktop/grid.txt'
    main(file_name)
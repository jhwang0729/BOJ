import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n, m = map(int, input().split())
grid: list[list[int]] = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited: list[list[bool]] = [[False for _ in range(m)] for _ in range(n)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def get_num_island(grid: list[list[int]]):
    out = 0
    for i in range(n):
        for j in range(m):
            out = max(out, grid[i][j])
    return out


def is_valid(i: int, j: int) -> bool:
    return 0 <= i < n and 0 <= j < m and grid[i][j] == 1


def bfs(grid: list[list[int]], queue: deque[tuple[int, int]], visited: list[list[bool]], cnt: int):
    while queue:
        i, j = queue.popleft()
        visited[i][j] = True
        grid[i][j] = cnt
        for dir_ in range(4):
            next_i, next_j = i + di[dir_], j + dj[dir_]
            if is_valid(next_i, next_j) and not visited[next_i][next_j]:
                queue.append((next_i, next_j))
    # print(visited)
    for elem in visited:
        print(elem)


def get_edges(grid: list[list[int]], num_island: int) -> list[list[int]]:
    out = [[0 for _ in range(num_island+1)] for _ in range(num_island+1)]
    for i in range(n):
        for j in range(m):
            # start_island: int = 0
            # end_island: int = 0
            if grid[i][j] != 0:
                island_num = grid[i][j]
                width_dist = 0
                width_end_island = 0
                height_dist = 0
                height_end_island = 0

                for cur_j in range(j + 1, m):
                    if grid[i][cur_j] == island_num:
                        break
                    elif grid[i][cur_j] != 0:
                        width_end_island = grid[i][cur_j]
                        break
                    width_dist += 1

                for cur_i in range(i + 1, n):
                    if grid[cur_i][j] == island_num:
                        break
                    elif grid[cur_i][j] != 0:
                        height_end_island = grid[cur_i][j]
                        break
                    height_dist += 1

                if width_end_island != 0 and width_dist >= 2:
                    if not out[island_num][width_end_island]:
                        out[island_num][width_end_island] = width_dist
                        out[width_end_island][island_num] = width_dist
                    else:
                        out[island_num][width_end_island] = min(out[island_num][width_end_island], width_dist)
                        out[width_end_island][island_num] = min(out[island_num][width_end_island], width_dist)

                if height_end_island != 0 and height_dist >= 2:
                    if not out[island_num][height_end_island]:
                        out[island_num][height_end_island] = height_dist
                        out[height_end_island][island_num] = height_dist
                    else:
                        out[island_num][height_end_island] = min(out[island_num][height_end_island], height_dist)
                        out[height_end_island][island_num] = min(out[island_num][height_end_island], height_dist)
    return out


cnt: int = 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            print(i, j, cnt)
            queue: deque[tuple[int, int]] = deque()
            queue.append((i, j))
            bfs(grid, queue, visited, cnt)
            cnt += 1

for elem in grid:
    print(elem)

print()
print()

V = get_num_island(grid)
INF = float('inf')

edges = get_edges(grid, V)
for elem in edges:
    print(elem)


parent = [i for i in range(V)]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b


# Finds MST using Kruskal's algorithm
def kruskalMST(cost):
    mincost = 0  # Cost of min MST

    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i

    # Include minimum weight edges one by one
    edge_count = 0
    while edge_count < V - 1:
        min = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min

    print("Minimum cost= {}".format(mincost))

kruskalMST(grid)
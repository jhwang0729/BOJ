import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt', 'r')

di: list[int] = [-1, 1, 0, 0, 0, 0]
dj: list[int] = [0, 0, -1, 1, 0, 0]
dk: list[int] = [0, 0, 0, 0, -1, 1]


def find_starting_points(grid: list[list[list[int]]], queue: deque[tuple[int, int, int]],
                         i: int, j: int, k: int) -> deque[tuple[int, int, int]]:
    for a in range(k):
        for b in range(i):
            for c in range(j):
                if grid[a][b][c] == 1:
                    queue.append((a, b, c))

    return queue


def is_valid(grid: list[list[list[int]]], i: int, j: int, k: int) -> bool:
    return (0 <= i < N) and (0 <= j < M) and (0 <= k < H) and grid[k][i][j] == 0 and visited[k][i][j] is False


def is_ripen(grid: list[list[list[int]]], i: int, j: int, k: int) -> bool:
    for a in range(k):
        for b in range(i):
            for c in range(j):
                if grid[a][b][c] == 0:
                    return False
    else:
        return True


def count_days(grid: list[list[list[int]]], i: int, j: int, k: int) -> int:
    max_: int = 0
    for a in range(k):
        for b in range(i):
            for c in range(j):
                max_ = max(grid[a][b][c], max_)
    return max_

def bfs(grid: list[list[list[int]]], visited: list[list[list[int]]], queue: deque[tuple[int, int, int]]) -> None:
    while queue:
        cur_k, cur_i, cur_j, = queue.popleft()
        for dir_ in range(6):
            next_k, next_i, next_j = cur_k + dk[dir_], cur_i + di[dir_], cur_j + dj[dir_],
            if is_valid(grid, next_i, next_j, next_k):
                grid[next_k][next_i][next_j] = grid[cur_k][cur_i][cur_j] + 1
                queue.append((next_k, next_i, next_j))
                visited[next_k][next_i][next_j] = True


M, N, H = list(map(int, sys.stdin.readline().split()))
grid: list[list[list[int]]] = [[] for _ in range(H)]
for h in range(H):
    for _ in range(N):
        grid[h].append(list(map(int, sys.stdin.readline().split())))
visited: list[list[list[bool]]] = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue: deque[tuple[int, int, int]] = deque()

if is_ripen(grid, N, M, H):
    print(0)
else:
    queue = find_starting_points(grid, queue, N, M, H)
    bfs(grid, visited, queue)
    if is_ripen(grid, N, M, H):
        print(count_days(grid, N, M, H) - 1)
    else:
        print(-1)

# print(queue)
print(grid)

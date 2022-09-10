import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N: int = int(input())
grid: list[list[int]] = [list(map(int, input().split())) for _ in range(N)]
visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
di = [0, 1, 1]  # right, down, diag
dj = [1, 0, 1]


def is_valid(grid: list[list[int]], dir_: int, i: int, j: int) -> bool:
    if dir_ == 2:
        return (0 <= i < N) and (0 <= j < N) and grid[i][j] == 0 and grid[i - 1][j] == 0 and grid[i][j - 1] == 0
    else:
        return (0 <= i < N) and (0 <= j < N) and grid[i][j] == 0


def bfs(queue: deque[tuple[int, int, int]], grid: list[list[int]], visited: list[list[bool]]) -> int:
    cnt: int = 0
    while queue:
        i, j, cur_dir = queue.popleft()
        if i == N - 1 and j == N - 1:
            cnt += 1
            continue
        for next_dir in range(3):
            # print(cur_dir, next_dir)
            if cur_dir == 0 and next_dir == 1:
                continue
            elif cur_dir == 1 and next_dir == 0:
                continue
            next_i, next_j = i + di[next_dir], j + dj[next_dir],
            if is_valid(grid, next_dir, next_i, next_j):
                # visited[next_i][next_j] = True
                queue.append((next_i, next_j, next_dir))
                # print(queue)

    return cnt


queue: deque[tuple[int, int, int]] = deque()
queue.append((0, 1, 0))
visited[0][1] = True
ans: int = bfs(queue, grid, visited)
print(ans)

import sys

from collections import namedtuple, deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N: int = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

start_i, start_j = 0, 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            start_i, start_j = i, j
            grid[i][j] = 0
            break


def is_valid(i: int, j: int) -> bool:
    return (0 <= i < N) and (0 <= j < N)


def solve(i: int, j: int) -> int:
    cur_size: int = 2
    cur_eat: int = 0
    tot_dist = 0

    while True:

        next_i, next_j, next_dist = bfs(i, j, cur_size)
        if next_i == -1 and next_j == -1 and next_dist == -1:
            break

        grid[next_i][next_j] = 0
        tot_dist += next_dist
        cur_eat += 1

        if cur_eat == cur_size:
            cur_size += 1
            cur_eat = 0

        i, j = next_i, next_j

    return tot_dist


def bfs(i: int, j: int, size: int) -> tuple[int, int, int]:
    queue = deque()
    out_i, out_j, out_dist, flag = N + 1, N + 1, sys.maxsize, False
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[i][j] = True
    queue.append((i, j, size, 0))

    while queue:
        cur_i, cur_j, cur_size, cur_dist = queue.popleft()

        if cur_dist > out_dist:
            break

        if grid[cur_i][cur_j] != 0 and grid[cur_i][cur_j] < cur_size:  # can eat
            if cur_dist < out_dist:
                out_i, out_j, out_dist = cur_i, cur_j, cur_dist
                flag = True
            elif cur_dist == out_dist:
                if cur_i < out_i:
                    out_i, out_j, out_dist = cur_i, cur_j, cur_dist
                elif cur_i == out_i:
                    if cur_j < out_j:
                        out_i, out_j, out_dist = cur_i, cur_j, cur_dist

        for dir_ in range(4):
            next_i, next_j = cur_i + di[dir_], cur_j + dj[dir_]
            if is_valid(next_i, next_j) and grid[next_i][next_j] <= cur_size and visited[next_i][next_j] == False:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j, cur_size, cur_dist + 1))

    return (out_i, out_j, out_dist) if flag else (-1, -1, -1)


ans: int = solve(start_i, start_j)
print(ans)

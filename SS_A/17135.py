import sys
from collections import deque
from itertools import combinations

sys.stdin = open('input.txt', 'r')

N, M, D = list(map(int, input().split()))
grid = [[int(elem) for elem in input().split()] for _ in range(N)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def is_valid(i: int, j: int) -> bool:
    return (0 <= i < 2) and (0 <= j < 2)


def dfs(grid: list[list[int]], i: int, j: int, depth: int) -> tuple[int, int]:
    tmp = (0, 0)
    print(i, j, depth)
    if depth < 0:
        return (0, 0)
    visited[i][j] = True
    if grid[i][j] == 1:
        return (i, j)
    for dir_ in range(4):
        next_i, next_j = i + di[dir_], j + dj[dir_]
        if is_valid(next_i, next_j) and not visited[next_i][next_j]:
            val = dfs(grid, next_i, next_j, depth - 1)
            tmp = (tmp[0] + val[0], tmp[1] + val[1])
        # return (tmp[0]+val[0], tmp[1]+val[1])
    return tmp

test = [[0, 0], [0, 0]]
visited = [[False for _ in range(2)] for _ in range(2)]
a = dfs(test, 0, 0, 2)
print(f'a is {a}')
print(visited)

# c = combinations(list(range(0, N)), 3)
#
# queue: deque[tuple[int, int, int]] = deque()
# visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]

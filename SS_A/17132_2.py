import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

sys.stdin = open('input.txt', 'r')

N, M, D = list(map(int, input().split()))
# print(N, M, D)
grid_true = [[int(elem) for elem in input().split()] for _ in range(N)]
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]


def is_valid(i: int, j: int) -> bool:
    # print(f'in the is_valid {i, j}')
    return (0 <= i < N) and (0 <= j < M)


def dfs(grid: list[list[int]], i: int, j: int, depth: int) -> tuple[int, int]:
    # print(f'int the dfs {i, j}')
    # print(visited)
    tmp = (0, 0)
    if depth < 0:
        return 0, 0
    visited[i][j] = True
    if grid[i][j] == 1:
        return i, j
    for dir_ in range(4):
        next_i, next_j = i + di[dir_], j + dj[dir_]
        if is_valid(next_i, next_j) and not visited[next_i][next_j]:
            # print(f'about to pass next_i, next_j {next_i, next_j}')
            val = dfs(grid, next_i, next_j, depth - 1)
            tmp = (tmp[0] + val[0], tmp[1] + val[1])
            # if tmp[0] != 0 and tmp[1] != 0:
                # break
        # return (tmp[0]+val[0], tmp[1]+val[1])
    return tmp


def advance(grid: list[list[int]]) -> list[list[int]]:
    out = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if 0 <= i + 1 < N:
                    out[i+1][j] = 1
    return out


# visited = [[False for _ in range(2)] for _ in range(2)]
# a = dfs(test, 0, 0, 2)
# print(f'a is {a}')
# print(visited)

c = combinations(list(range(0, M)), 3)

queue: deque[tuple[int, int, int]] = deque()
global_cnt = 0

for combination in c:

    first, second, third = combination
    first_pos = (N-1, first)
    second_pos = (N-1, second)
    third_pos = (N-1, third)
    # downs = []
    # true_downs = set()
    grid = deepcopy(grid_true)
    cnt = 0


    # while True:
    for turn in range(N):
        downs = []
        # print(grid)
        visited: list[list[bool]] = [[False for _ in range(M)] for _ in range(N)]
        downs.append(dfs(grid, *first_pos, D-1))
        downs.append(dfs(grid, *second_pos, D-1))
        downs.append(dfs(grid, *third_pos, D-1))

        # print(downs)

        print(set(downs))
        for down in set(downs):
            donw_i, down_j = down
            # print(donw_i, down_j)
            if donw_i == 0 and down_j == 0:
                continue
            grid[donw_i][down_j] = 0
            cnt += 1
        grid = advance(grid)

        if turn + 1 == N:
            global_cnt = max(global_cnt, cnt)
            # print()

        # print(grid)
        # if not flag:
        #     break
        # break

    # print(combination, downs)
    # print('\n\n')
print(global_cnt)



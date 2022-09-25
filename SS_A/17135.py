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


def attack(grid: list[list[int]], i: int, j: int, depth: int) -> tuple[int, int]:
    tmp = (0, 0)
    if depth < 0:
        return 0, 0
    visited[i][j] = True
    if grid[i][j] == 1:
        return i, j
    for dir_ in range(4):
        next_i, next_j = i + di[dir_], j + dj[dir_]
        if is_valid(next_i, next_j) and not visited[next_i][next_j]:
            val = attack(grid, next_i, next_j, depth - 1)
            tmp = (tmp[0] + val[0], tmp[1] + val[1])
            if val[0] or val[1]:
                break
        # return (tmp[0]+val[0], tmp[1]+val[1])
    return tmp


def advance(grid: list[list[int]]) -> bool:
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                if i + 1 >= N:
                    return False
                grid[i+1][j] = 1
                grid[i][j] = 0
    else:
        return True

# test = [[0, 0], [1, 0]]
# visited = [[False for _ in range(2)] for _ in range(2)]
# a = attack(test, 0, 0, 2)
# print(f'a is {a}')
# print(visited)
#
c = combinations(list(range(0, N)), 3)

# queue: deque[tuple[int, int, int]] = deque()
# visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
global_cnt = 0

for combination in c:
    visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
    print(combination)
    downs = []
    # local_cnt = 0

    first = (N-1, combination[0])
    second = (N-1, combination[1])
    third = (N-1, combination[2])

    # print(att)
    downs.append(attack(grid, vi))

    # while True:
    #     print(first, second, third)
    #     downs = []
    #     true_downs = set()
    #     downs.append(attack(grid, *first, D))
    #     print(downs)
    #     downs.append(attack(grid, *second, D))
    #     print(downs)
    #     downs.append(attack(grid, *third, D))
    #     print(downs)
    #
    #     for down in downs:
    #         true_downs.add(down)
    #
    #     for true_down in true_downs:
    #         local_cnt += 1
    #         i, j = true_down
    #         grid[i][j] = -1
    #
    #     if not advance(grid):
    #         global_cnt = max(global_cnt, local_cnt)
    #         break
    #
    #     advance(grid)

    # print(true_downs)
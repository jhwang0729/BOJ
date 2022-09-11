import sys

from collections import deque
from copy import deepcopy
from itertools import combinations

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def is_valid(i: int, j: int) -> bool:
    return (0 <= i < N) and (0 <= j < M)


def bfs(i: int, j: int, d: int) -> tuple[int, int]:
    down_i, down_j, down_d, flag = 0, M + 1, D + 1, False
    queue = deque()
    queue.append((i, j, d))
#     # print(f'in the bfs {i}, {j}, {d}')

    while queue:
        cur_i, cur_j, cur_d, = queue.popleft()
        if cur_d > D:
            break

#         # print(f'cur_d -> {cur_i}, {cur_j}, {cur_d}')

        if local_grid[cur_i][cur_j] == 1:
#             # print(f' if ran in {cur_i}, {cur_j}, {cur_d}')
            if cur_d < down_d:
                down_i, down_j, down_d = cur_i, cur_j, cur_d
#                 # print(f'after updating down pos {down_i}, {down_j}, {down_d}')
                flag = True
            elif cur_d == down_d:
                if cur_j < down_j:
                    down_i, down_j, down_d = cur_i, cur_j, cur_d
#                     # print(f'after updating down pos lefter {down_i}, {down_j}, {down_d}')
                    flag = True

        for dir_ in range(4):
            next_i, next_j = cur_i + di[dir_], cur_j + dj[dir_]
            if is_valid(next_i, next_j) and visited[next_i][next_j] == False:
                visited[next_i][next_j] = True
                queue.append((next_i, next_j, cur_d + 1))

    return (down_i, down_j) if flag else (-1, -1)


def advance() -> bool:
    global local_grid
    out = [[0 for _ in range(M)] for _ in range(N)]
    is_over = True
    for i in range(N):
        for j in range(M):
            if local_grid[i][j] == 1:
                if is_valid(i + 1, j):
                    is_over = False
                    out[i + 1][j] = 1
    local_grid = out
    return is_over


def is_over() -> bool:
    is_over = True
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                is_over = False
                break
    return is_over


global_max = 0
archer_positions = list(combinations(range(M), 3))
for archer_pos in archer_positions:

    local_grid = deepcopy(grid)
    # visited = [[False for _ in range(M)] for _ in range(N)]
    local_max = 0

    if is_over():
        continue

    for _ in range(N):
        downs = []
        true_downs = set()

        first_i, first_j = N - 1, archer_pos[0]
        second_i, second_j = N - 1, archer_pos[1]
        third_i, third_j = N - 1, archer_pos[2]

        visited = [[False for _ in range(M)] for _ in range(N)]
        downs.append(bfs(first_i, first_j, 1))

        visited = [[False for _ in range(M)] for _ in range(N)]
        downs.append(bfs(second_i, second_j, 1))

        visited = [[False for _ in range(M)] for _ in range(N)]
        downs.append(bfs(third_i, third_j, 1))

        # print(f'downs are {downs}')

        for down in downs:
            if down[0] == -1 and down[1] == -1:
                continue
            true_downs.add(down)

        # for elem in local_grid:
        #     print(elem)

        # print(f'true downs are {true_downs}')
        # print()

        if true_downs:
            # print('true downs are runnin')
            for down in true_downs:
                down_i, down_j = down
                local_grid[down_i][down_j] = 0
                local_max += 1
            # for elem in local_grid:
            #     print(elem)
            # print()

        result = advance()
        # for elem in local_grid:
        #     print(elem)
        # print()

        if result:
            global_max = max(global_max, local_max)
            break

    else:
        global_max = max(global_max, local_max)

print(global_max)

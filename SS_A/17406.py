import sys
from copy import deepcopy
from itertools import permutations

sys.stdin = open('input.txt', 'r')


def rotate(grid: list[list[int]], s_i, s_j, e_i, e_j) -> None:
    tmp = grid[s_i][s_j]

    # left
    for i in range(s_i, e_i):
        grid[i][s_j] = grid[i+1][s_j]

    # # bottom
    for j in range(s_j, e_j):
        grid[e_i][j] = grid[e_i][j+1]
    #
    # # right
    for i in range(e_i, s_i, -1):
        grid[i][e_j] = grid[i-1][e_j]
    #
    # # top
    for j in range(e_j, s_j, -1):
        grid[s_i][j] = grid[s_i][j-1]

    grid[s_i][s_j+1] = tmp


N, M, K = list(map(int, input().split()))
grid: list[list[int]] = [[int(elem) for elem in input().split()] for _ in range(N)]

if not K:
    least_sum = min([sum(elem) for elem in grid])
    # min_ = min(min_, least_sum)
    print(least_sum)
else:
    k_rotations: list[list[int]] = [[int(elem) for elem in input().split()] for _ in range(K)]
    # print(k_rotations)
    p = permutations(k_rotations)
    min_ = 99999999

    for rotations in p:
        # print(f'rotations is {rotations}')
        tmp_grid = deepcopy(grid)
        least_sum = 0
        for rotation in rotations:
            # print(f'rotation is {rotation}')
            r, c, s = rotation
            start_i = r - s - 1
            start_j = c - s - 1
            end_i = r + s - 1
            end_j = c + s - 1

            num_iter = (end_i - start_i) // 2

            is_ = list(range(start_i, end_i+1))
            js_ = list(range(start_j, end_j+1))
            # is_ = is_[:len(is_)//2]
            # js_ = js_[:len(js_)//2]

            for idx in range(len(is_)//2):
                s_i, e_i = is_[idx], is_[-(idx+1)]
                s_j, e_j = js_[idx], js_[-(idx+1)]

                # print(s_i, s_j, e_i, e_j)
                rotate(tmp_grid, s_i, s_j, e_i, e_j)

        least_sum = min([sum(elem) for elem in tmp_grid])
        min_ = min(min_, least_sum)
        print(tmp_grid)

    print(min_)
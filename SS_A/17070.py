import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

# pipes = [[[1, 1], [0, 0]], [[1, 0], [1, 0]], [[1, 1], [1, 1]]]
pipes = (((1, 1), (0, 0)), ((1, 0), (1, 0)), ((1, 1), (1, 1)))

moves = {pipes[0]: [(pipes[0], 0, 1), (pipes[2], 0, 1)],
         pipes[1]: [(pipes[1], 1, 0), (pipes[2], 1, 0)],
         pipes[2]: [(pipes[0], 0, 1), (pipes[1], 1, 0), (pipes[2], 1, 1)]}


def is_valid(grid: list[list[int]], pipe: tuple[tuple[int, int], tuple[int, int]],
             i: int, j: int, cnt: int) -> bool:
    if (0 <= i < N) and (0 <= j < N):
        return False
    tmp: list[tuple[int, int]] = []
    out: bool = False
    for x in range(2):
        for y in range(2):
            if pipe[x][y] == 1:
                tmp.append((x + 1, y + 1))
    for elem in tmp:
        di, dj = elem
        next_i, next_j = i + di, j + dj
        if not (0 <= next_i < N) or not (0 <= next_j < N) or grid[next_i][next_j] != 1:
            out = False
            break
    else:
        out = True

    if out:
        for elem in tmp:
            di, dj = elem
            next_i, next_j = i + di, j + dj
            if next_i == N - 1 and next_j == N - 1:
                cnt += 1
    return out

    # for di in range(2):
    #     for dj in range(2):


def bfs(grid: list[list[int]], queue: deque[tuple[tuple[tuple[int, int], tuple[int, int]], int, int]],
        cnt: int) -> None:
    while queue:
        cur_pipe, cur_i, cur_j = queue.popleft()
        for move in moves[pipe]:
            next_pipe, di, dj = move
            next_i, next_j = cur_i + di, cur_j + dj
            if is_valid(grid, next_pipe, next_i, next_j, cnt):
                queue.append((next_pipe, di, dj))


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
pipe = pipes[0]
queue: deque[tuple[tuple[tuple[int, int], tuple[int, int]], int, int]] = deque()
queue.append((pipe, 0, 0))
cnt = 0
bfs(grid, queue, cnt)
print(cnt)
# print(moves)

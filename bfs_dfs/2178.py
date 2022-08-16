import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
# map(int, list(input()))

# map = [
#     # [list(map(int, input().split()))] for _ in range(N)
#     [int(elem) for elem in input().split()] for _ in range(N)
# ]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

grid = [list(map(int, list(input()))) for _ in range(N)]
visited = [
    [False for _ in range(M)]
    for _ in range(N)
]
queue: deque[tuple[int, int]] = deque()


def is_valid(grid: list[list[int]], i: int, j: int) -> bool:
    return (0 <= i < N) and (0 <= j < M) and grid[i][j] == 1


def bfs(grid: list[list[int]], visited: list[list[bool]], queue: deque[tuple[int, int]], N: int, M: int) -> None:
    # cnt = 1
    while queue:
        root = queue.popleft()
        # cnt += 1

        cur_i, cur_j = root
        # grid[cur_i][cur_j] = cnt
        # if cur_i == N - 1 and cur_j == M - 1:
        #     print(cnt)

        # cnt += 1
        for direction in range(4):
            next_i = cur_i + di[direction]
            next_j = cur_j + dj[direction]
            if is_valid(grid, next_i, next_j) and not visited[next_i][next_j]:
                if next_i == N - 1 and next_j == M - 1:
                    print(cnt+1)
                # cnt += 1
                visited[next_i][next_j] = True
                grid[next_i][next_j] = grid[cur_i][cur_j] + 1
                queue.append((next_i, next_j))

    print(grid)
    for elem in grid:
        print(elem)

visited[0][0] = True
cnt = 1
queue.append((0, 0))
print(grid)
for elem in grid:
    print(elem)
print('\n\n')
bfs(grid, visited, queue, N, M)

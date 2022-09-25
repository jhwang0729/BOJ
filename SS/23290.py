import sys

from copy import deepcopy

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

m, s = map(int, input().split())
fishes = [list(map(int, input().split())) for _ in range(m)]
sx, sy = map(int, input().split())
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

fish_grid = {}

for fish in fishes:
    x, y, d = fish
    if (x, y) not in fish_grid:
        fish_grid[(x, y)] = []
    fish_grid[(x, y)].append(d)

print(fish_grid)


def is_valid(i, j):
    return (1 <= i <= 4) and (1 <= j <= 4)


def fish_move():
    global fish_grid

    temp = deepcopy(fish_grid)
    fish_grid = {}
    fish_idxs = temp.keys()

    for fish_idx in fish_idxs:
        x, y = fish_idx
        fishes = temp[(x, y)]
        while fishes:
            fish = fishes.pop(0)
            next_i, next_j = x + di[fish - 1], y + dj[fish - 1]
            if not is_valid(next_i, next_j):
                while is_valid(next_i, next_j):
                    fish = (fish + 1) % 8
                    next_i, next_j = x + di[fish - 1], y + dj[fish - 1]
            if (next_i, next_j) not in fish_grid:
                fish_grid[(next_i, next_j)] = []
            print(fish_grid)
            fish_grid[(next_i, next_j)].append(fish)

    print(fish_grid)

def shark_move():
    pass


def remove_smell():
    pass


def solve():
    fish_move()
    shark_move()
    remove_smell()

# print(fishes)
fish_move()
# ans = solve()
# print(ans)

import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
grid = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
]

print(grid)
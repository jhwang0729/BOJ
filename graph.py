import sys

sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
grid: list[list[int]] = [list(map(int, sys.stdin.readline().split()))]


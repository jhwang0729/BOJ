import sys

sys.stdin = open('input.txt', 'r')

# a = list(map(int, input))

T = int(input())
arr = []

for i in range(T):
    arr.append(list(map(int, sys.stdin.readline().split())))

print( )
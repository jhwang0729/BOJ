import sys
from collections import deque

sys.stdin = open('./input.txt', 'r')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(graph: list[list[int]], visited: list[bool], start: int, out: list[int]) -> list[int]:
    # visited[start] = True
    # out.append(graph[start][0])

    for root in graph[start]:
        if not visited[root]:
            visited[root] = True
            out.append(root + 1)

            dfs(graph, visited, root, out)
            # out += dfs(graph, visited, start, out)

    return out


def bfs(graph: list[list[int]], visited: list[bool], start: int, out: list[int], queue: deque[int]) -> None:
    while queue:
        root = queue.popleft()

        for child in graph[root]:
            if not visited[child]:
                out.append(child + 1)
                visited[child] = True
                queue.append(child)

    # print(out)
    print(' '.join([str(elem) for elem in out]))

N, M, V = list(map(int, sys.stdin.readline().split()))
graph: list[list[int]] = [[] for _ in range(N)]
visited: list[bool] = [False for _ in range(N)]
queue: deque[int] = deque()
out: list[int] = []
for _ in range(M):
    s, e = list(map(int, sys.stdin.readline().split()))
    graph[s - 1].append(e - 1)
    graph[e - 1].append(s - 1)

for i in range(N):
    graph[i].sort()

out.append(V)
visited[V - 1] = True

out = dfs(graph, visited, V - 1, out)
print(' '.join([str(elem) for elem in out]))

out = []
out.append(V)
visited = [False for _ in range(N)]
visited[V - 1] = True
queue.append(V - 1)

bfs(graph, visited, V - 1, out, queue)

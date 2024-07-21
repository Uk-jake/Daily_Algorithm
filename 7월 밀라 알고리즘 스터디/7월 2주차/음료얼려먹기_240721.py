import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(graph, i, j):

    if i < 0 or i >= N or j < 0 or j >= M:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(graph, i+1, j)
        dfs(graph, i-1, j)
        dfs(graph, i, j+1)
        dfs(graph, i, j-1)
        return True
    return False


input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = []
count = 0

for _ in range(N):
    graph.append(list(map(int, input().strip())))

# print(graph)

for i in range(N):
    for j in range(M):
        if dfs(graph, i, j) == True:
            count += 1

print(count)
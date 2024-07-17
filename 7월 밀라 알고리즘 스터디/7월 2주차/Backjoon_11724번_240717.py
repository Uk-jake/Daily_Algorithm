from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(node):
    que = deque()

    que.append(node)
    visited[node] = True

    while que:
        tmp = que.popleft()
        for item in graph[tmp]:
            if not visited[item]:
                que.append(item)
                visited[item] = True


# n(정점의 개수), m(간선의 개수) 입력
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

print(count)
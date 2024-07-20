import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    
    que = deque()
    que.append((x, y))
    
    while que:
        mx, my = que.popleft()
        
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[mx][my] + 1
                que.append((nx, ny))

n, m = map(int, sys.stdin.readline().strip().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))
    
print(graph)

# bfs(0,0)

# print(graph)

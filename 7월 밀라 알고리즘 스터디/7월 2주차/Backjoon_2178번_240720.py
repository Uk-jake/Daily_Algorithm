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
            
            # 초과 인덱스 처리
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            # 0이면 벽이므로 이동 불가
            if graph[nx][ny] == 0:
                continue
            # 1이면 이동할 수 있는 곳
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[mx][my] + 1
                que.append((nx, ny))

# n과 m 입력
n, m = map(int, sys.stdin.readline().strip().split())

graph = []

# 미로 입력
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# bfs 시작
bfs(0,0)

# 마지막 그래프 수 출력
print(graph[n-1][m-1])

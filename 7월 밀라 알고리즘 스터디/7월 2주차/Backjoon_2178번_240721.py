import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i, j):
    
    que = deque()
    que.append((i,j))
    visited[i][j] = 1
    
    while que:
        x , y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx,ny))
    
    

input = sys.stdin.readline

# N - 미로의 가로 크기, M - 미로의 세로 크기
N, M = map(int, input().strip().split())

graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    graph.append(list(map(int, input().strip())))
    
bfs(0,0)

for line in visited:
    print(line)
    
print(visited[N-1][M-1])
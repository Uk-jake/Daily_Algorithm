import sys
from collections import deque

def bfs(x, y):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    que = deque()
    que.append((x,y))
    graph[x][y] = 0
    count = 1
    
    while que:
        # print(que)
        mx , my = que.popleft()
        
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 1:
                que.append((nx, ny))
                
                graph[nx][ny] = 0 
                count += 1
    return count


# n 세로 길이
# m 가로 길이
# k 음식물 쓰레기 개수
n, m, k, = map(int, sys.stdin.readline().strip().split())

# 2차원 배열 선언
graph = [[0 for _ in range(m)] for _ in range(n)]

# 음식물 쓰레기 좌표 입력
for _ in range(k):
    r, c = map(int, sys.stdin.readline().strip().split())
    graph[r - 1][c - 1] = 1

# for line in graph :
#     print(line)

answer = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))
        
# for line in graph :
#     print(line)
print(max(answer))
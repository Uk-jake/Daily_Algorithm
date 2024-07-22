import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS 함수
def bfs(i, j):
    que = deque()
    # 시작 인덱스 que에 deque
    que.append((i, j))
    # 시작 인덱스 방문 처리
    visited[i][j] = 1

    # que에 데이터가 없을 때까지 반복
    while que:
        x, y = que.popleft()

        for i in range(4):
            # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            # 초과 인덱스 처리
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 인접한 데이터가 이동할 수 있고 방문하지 않은 곳이라면
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))


input = sys.stdin.readline

# N - 미로의 가로 크기, M - 미로의 세로 크기
N, M = map(int, input().strip().split())

# 미로 리스트 선언
graph = []

# 방문 여부 및 최단 거리 리스트 선언
visited = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    graph.append(list(map(int, input().strip())))

# (0,0)에서 bfs 시작
bfs(0, 0)

print(visited[N-1][M-1])
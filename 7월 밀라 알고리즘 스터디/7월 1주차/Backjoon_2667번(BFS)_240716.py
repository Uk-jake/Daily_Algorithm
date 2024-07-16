from collections import deque

def bfs(graph, i, j):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


# 정수 N 입력
n = int(input().strip())

graph = []

# N * N 개의 자료 입력
for i in range(n):
    input_row = input().strip()
    row = [int(char) for char in input_row]
    graph.append(row)

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # 집(1)이 있다면 bfs를 통해 주변에 몇개의 집이 있는지 확인
            answer.append(bfs(graph, i, j))

answer.sort()

print(len(answer))
for item in answer:
    print(item)
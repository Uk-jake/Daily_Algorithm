
# 정수 N 입력
n = int(input().strip())

graph = []
count = 0

# N * N 개의 자료 입력
for i in range(n):
    input_row = input().strip()
    row = [int(char) for char in input_row]
    graph.append(row)

answer = []


def dfs(i, j):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    
    if graph[i][j] == 1:
        global count
        count += 1
        graph[i][j] = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            dfs(nx, ny)
        return True
    return False
        


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            answer.append(count)
            count = 0

answer.sort()
print(len(answer))
for item in answer:
    print(item)
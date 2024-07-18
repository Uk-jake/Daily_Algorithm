import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

def dfs(graph, x, y):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    if x < 0 or x >= n or y < 0 or y >= m :
        return False 
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        for i in range(4):
            dfs(graph, x + dx[i], y + dy[i])
            
        return True
    return False
    


# 테스트 케이스 개수
T = int(sys.stdin.readline())

for _ in range(T):
    
    # m = 밭 가로 길이
    # n = 밭 세로 길이
    # k = 배추의 개수
    m, n, k = map(int, sys.stdin.readline().strip().split())
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1
    
    # for line in graph:
    #     print(line)
    
    # 연결 요소 개수
    count = 0
    
    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j):
                count += 1
    
    print(count)

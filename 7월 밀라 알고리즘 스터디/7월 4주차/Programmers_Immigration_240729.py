import sys

input = sys.stdin.readline

# 백트래킹 함수
def backtracking( length, tmp_list ):
    # 순열의 개수가 M개이면 answer에 추가
    if length == M:
        answer.append(tmp_list)
        return
    
    # 이전의 사용한 값
    prev = 0
    # N번 반복
    for i in range(N):
        # 방문하지 않은 곳이고 이전 사용한 값이 같이 않으면 순열 추가
        if visited[i] == 0 and prev != input_list[i]:
            prev = input_list[i]
            visited[i] = 1
            backtracking(length + 1, tmp_list+[input_list[i]])
            visited[i] = 0
        
# N과 M 입력
N, M = map(int, input().strip().split())

# 자연수 N개 입력
input_list = list(map(int, input().strip().split()))

# 오름차순 정렬
input_list.sort()

# 방문 여부
visited = [0] * N
answer = []

# 백트래킹 시작
backtracking(0, [])

# 순열 출력
for line in answer:
    print(*line)
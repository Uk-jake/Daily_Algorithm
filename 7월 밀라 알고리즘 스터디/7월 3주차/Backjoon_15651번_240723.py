import sys
input = sys.stdin.readline

# 백트래킹 함수
# length = 수열의 길이
# tmp_list = 만들어지고 있는 수열
def backtracking( length , tmp_list ):
    
    # 수열의 길이가 M이 된다면 answer에 수열 삽입
    if length == M:
        answer.append(tmp_list)
        return
    
    # for 문을 이용하여 수열의 길이가 M이 될때까지
    # 1 ~ N 자연수를 차례대로 tmp_list 뒤에 추가한다.
    for i in range(1, N+1):
        backtracking(length + 1, tmp_list+[num[i]])

# N - 1부터 N까지 자연수 , M - 수열의 길이
N, M = map(int, input().strip().split())

# 자연수 1 ~ N 리스트 선언
num = [i for i in range(0, N + 1)]

# 정답 리스트 선언
answer = []

# print(f"N : {N}, M : {M}")
# print(f"num : {num}")

# 백트래킹 시작 : 처음 시작은 길이 0, 리스트는 null 값으로 시작
backtracking(0 , [])

# 정답 리스트에 있는 데이터를 한 줄 씩 출력
for line in answer:
    print(*line)